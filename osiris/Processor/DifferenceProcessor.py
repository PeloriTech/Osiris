import cv2
import numpy as np
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA 
from collections import Counter
from .Processor import Processor

class DifferenceProcessor(Processor):

    def __init__(self):
        pass

    def start(self):
        pass

    def process_frame(self, frame, output_annotated :bool):
        # split the frame down the center vertically,
        # then compare the left side with the right side

        left_frame, right_frame = DifferenceProcessor.split_frame_vertically(frame)

        output = DifferenceProcessor.find_PCAKmeans(left_frame, right_frame)

        return output

    def stop(self):
        pass

    def check_health(self):
        pass

    @staticmethod
    def split_frame_vertically(frame):
        height, width = frame.shape[:2]
        # Let's get the starting pixel coordiantes (top left of cropped top)
        start_row, start_col = int(0), int(0)
        # Let's get the ending pixel coordinates (bottom right of cropped top)
        end_row, end_col = int(height), int(width * .5)
        cropped_left = frame[start_row:end_row , start_col:end_col]

        # Let's get the starting pixel coordiantes (top left of cropped bottom)
        start_row, start_col = int(0), int(width *.5)
        # Let's get the ending pixel coordinates (bottom right of cropped bottom)
        end_row, end_col = int(height), int(width)
        cropped_right = frame[start_row:end_row , start_col:end_col]

        return (cropped_left, cropped_right)

    @staticmethod
    def find_vector_set(diff_image, new_size):
    
        i = 0
        j = 0
        vector_set = np.zeros((int(new_size[0] * new_size[1] / 25), 25))

        print('\nvector_set shape',vector_set.shape)
        
        while i < vector_set.shape[0]:
            while j < new_size[0]:
                k = 0
                while k < new_size[1]:
                    block   = diff_image[j:j+5, k:k+5]
                    feature = block.ravel()
                    vector_set[i, :] = feature
                    k = k + 5
                j = j + 5
            i = i + 1
            
                
        mean_vec   = np.mean(vector_set, axis = 0)    
        vector_set = vector_set - mean_vec
        
        return vector_set, mean_vec
        
    @staticmethod
    def find_FVS(EVS, diff_image, mean_vec, new):
        
        i = 2 
        feature_vector_set = []
        
        while i < new[0] - 2:
            j = 2
            while j < new[1] - 2:
                block = diff_image[i-2:i+3, j-2:j+3]
                feature = block.flatten()
                feature_vector_set.append(feature)
                j = j+1
            i = i+1
        FVS = np.dot(feature_vector_set, EVS)
        FVS = FVS - mean_vec
        return FVS

    @staticmethod
    def clustering(FVS, components, new):
        
        kmeans = KMeans(components, verbose = 0)
        kmeans.fit(FVS)
        output = kmeans.predict(FVS)
        count  = Counter(output)

        least_index = min(count, key = count.get)            
        print(new[0],new[1])
        change_map  = np.reshape(output,(new[0] - 4, new[1] - 4))
        
        return least_index, change_map

    @staticmethod
    def find_PCAKmeans(imagepath1, imagepath2):
        
        image1 = cv2.imread(imagepath1)
        image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
        image2 = cv2.imread(imagepath2)
        image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
        new_size = np.asarray(image1.shape) / 5
        new_size = new_size.astype(int) * 5
        resize_new_size = (new_size[1], new_size[0])
        image1 = cv2.resize(image1, resize_new_size).astype(np.int16)
        image2 = cv2.resize(image2, resize_new_size).astype(np.int16)
        
        diff_image = abs(image1 - image2)   
        cv2.imwrite('diff.jpg', diff_image)
            
        vector_set, mean_vec = DifferenceProcessor.find_vector_set(diff_image, new_size)
        
        pca = PCA()
        pca.fit(vector_set)
        EVS = pca.components_
            
        FVS     = DifferenceProcessor.find_FVS(EVS, diff_image, mean_vec, new_size)
        
        components = 3
        least_index, change_map = DifferenceProcessor.clustering(FVS, components, new_size)
        
        change_map[change_map == least_index] = 255
        change_map[change_map != 255] = 0
        
        change_map = change_map.astype(np.uint8)
        kernel     = np.asarray(((0,0,1,0,0),
                                (0,1,1,1,0),
                                (1,1,1,1,1),
                                (0,1,1,1,0),
                                (0,0,1,0,0)), dtype=np.uint8)
        cleanChangeMap = cv2.erode(change_map,kernel)
        # cv2.imwrite("changemap.jpg", change_map)
        # cv2.imwrite("cleanchangemap.jpg", cleanChangeMap)
        return cleanChangeMap
