import os
import numpy as np
import cv2
import tensorflow as tf

from pipeline_manager.VideoProcessor.SimpleObjectDetection.object_detection.utils import label_map_util
from pipeline_manager.VideoProcessor.SimpleObjectDetection.object_detection.utils import visualization_utils as vis_util

from pipeline_manager.VideoProcessor.BaseProcessor import BaseProcessor

CWD_PATH = os.getcwd()

# Path to frozen detection graph. This is the actual model that is used for the object detection.
MODEL_NAME = 'ssd_mobilenet_v1_coco_11_06_2017'
PATH_TO_CKPT = os.path.join(CWD_PATH, 'pipeline_manager', 'VideoProcessor', 'SimpleObjectDetection', 'object_detection', MODEL_NAME, 'frozen_inference_graph.pb')

# List of the strings that is used to add correct label for each box.
PATH_TO_LABELS = os.path.join(CWD_PATH, 'pipeline_manager', 'VideoProcessor', 'SimpleObjectDetection', 'object_detection', 'data', 'mscoco_label_map.pbtxt')

NUM_CLASSES = 90

# Loading label map
label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES,
                                                            use_display_name=True)
category_index = label_map_util.create_category_index(categories)


class SimpleObjectDetectionProcessor(BaseProcessor):

    def run_processor(self, cap_send, out_send):

        detection_graph = tf.Graph()
        with detection_graph.as_default():
            od_graph_def = tf.GraphDef()
            with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
                serialized_graph = fid.read()
                od_graph_def.ParseFromString(serialized_graph)
                tf.import_graph_def(od_graph_def, name='')
            with tf.Session(graph=detection_graph) as sess:

                while True:
                    ret, frame = cap_send.read()
                    if ret:
                        frame = cv2.resize(frame, (640, 480))

                        # Only measure the time taken by YOLO and API Call overhead
                        frame, results = SimpleObjectDetectionProcessor.detect_objects(frame, sess, detection_graph)
                        self.message_queue.append(str(dict(results)))

                        cv2.imshow('send', frame)
                        out_send.write(frame)
                        if cv2.waitKey(1) & 0xFF == ord('q'):
                            exit(0)

    @staticmethod
    def detect_objects(image_np, sess, detection_graph):
        # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
        image_np_expanded = np.expand_dims(image_np, axis=0)
        image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')

        # Each box represents a part of the image where a particular object was detected.
        boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
        # Each score represent how level of confidence for each of the objects.
        # Score is shown on the result image, together with the class label.
        scores = detection_graph.get_tensor_by_name('detection_scores:0')
        classes = detection_graph.get_tensor_by_name('detection_classes:0')
        num_detections = detection_graph.get_tensor_by_name('num_detections:0')
        # Actual detection.
        (boxes, scores, classes, num_detections) = sess.run(
            [boxes, scores, classes, num_detections],
            feed_dict={image_tensor: image_np_expanded})
        # Visualization of the results of a detection.
        results = vis_util.visualize_boxes_and_labels_on_image_array(
            image_np,
            np.squeeze(boxes),
            np.squeeze(classes).astype(np.int32),
            np.squeeze(scores),
            category_index,
            use_normalized_coordinates=True,
            line_thickness=8)
        return image_np, results
