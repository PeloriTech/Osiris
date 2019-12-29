from threading import Thread
import cv2
import websockets
import asyncio


class BaseProcessor:

    def __init__(self):
        self.message_queue = []

    def start(self, cap_send, out_send, websocket_port):
        t = Thread(target=self.start_websocket, args=(websocket_port,))
        t.start()
        self.run_processor(cap_send, out_send)

    def start_websocket(self, websocket_port):
        asyncio.set_event_loop(asyncio.new_event_loop())
        asyncio.get_event_loop().run_until_complete(websockets.serve(
            self.run_websocket, 'localhost', websocket_port))
        asyncio.get_event_loop().run_forever()

    async def run_websocket(self, websocket, path):
        while True:
            if len(self.message_queue) > 0:
                message = self.message_queue.pop()
                await websocket.send(message)
                await asyncio.sleep(1)

    def run_processor(self, cap_send, out_send):

        while True:
            ret, frame = cap_send.read()
            if ret:
                frame = cv2.resize(frame, (640, 480))
                cv2.imshow('send', frame)
                out_send.write(frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    exit(0)
