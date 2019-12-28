import cv2


class CV2ImshowOutput:

    def __init__(self):
        pass

    def start(self):
        pass

    def stop(self):
        pass

    def push_frame(self, frame):
        cv2.imshow('Output', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            return