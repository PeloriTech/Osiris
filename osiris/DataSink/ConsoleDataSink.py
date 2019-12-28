from .DataSink import DataSink

class ConsoleDataSink(DataSink):

    def __init__(self):
        DataSink.__init__(self)

    def start(self):
        print("Starting ConsoleDataSink")

    def stop(self):
        print("Stopping ConsoleDataSink")

    def push_data(self, data):
        print(data)