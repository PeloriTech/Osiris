from abc import ABC, abstractmethod


class BaseOsirisProcessor:

    def __init__(self):
        pass

    def detect(self, frame):
        pass

    def preprocess(self, frame):
        pass

    def annotate(self, frame, results):
        pass

