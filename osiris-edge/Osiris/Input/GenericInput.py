from Osiris.Input.BaseOsirisInput import BaseOsirisInput
import cv2


class GenericInput(BaseOsirisInput):

    def open(self):
        pass

    def read(self):
        pass

    def is_opened(self) -> bool:
        pass

    def release(self):
        pass
