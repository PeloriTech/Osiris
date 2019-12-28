import netifaces as ni
import nmap
from Osiris.utils.CameraStream import CameraStream


class Scanner:

    def scan(self):
        interfaces = ni.interfaces()
        # iterate through interfaces
        camera_streams = []
        for iface in interfaces:
            ip = ni.ifaddresses(iface)[ni.AF_INET][0]['addr']
            port_scanner = nmap.PortScanner()
            output = port_scanner.scan(ip + '/24', '554')
            for device_key in output['scan'].keys():
                device = output['scan'][device_key]
                status = device['status']['state']
                is_opened = device['tcp'][554]['state'] == 'open'
                if is_opened:
                    camera_stream = CameraStream(device_key, status, iface)
                    camera_streams += [camera_stream]
        for camera_stream in camera_streams:
            pass
        return camera_streams
