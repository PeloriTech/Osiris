import cv2
import time

from Osiris.Input.BaseOsirisInput import BaseOsirisInput
from Osiris.Processor.BaseOsirisProcessor import BaseOsirisProcessor
from Osiris.Output.BaseOsirisOutput import BaseOsirisOutput


class Osiris:

    def __init__(self, processor: BaseOsirisProcessor, input: BaseOsirisInput, output: BaseOsirisOutput):
        self.processor = processor
        self.input = input
        self.output = output

    def run(self):

        print("capsend: ", self.input.is_opened())

        if not self.input.is_opened():
            print('VideoCapture or VideoWriter not opened')
            exit(0)

        while True:
            ret, frame = self.input.read()
            if ret:

                processed_frame = self.processor.preprocess(frame)
                results = self.processor.detect(processed_frame)
                del processed_frame

                frame = self.processor.annotate(frame, results)

                cv2.imshow('send', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        self.input.release()
