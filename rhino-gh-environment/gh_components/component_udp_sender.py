import json
import socket

import Grasshopper
import System


def send_data(data):
    # Create a UDP socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ("localhost", 12347)
    udp_socket.sendto(data, server_address)
    # s.send(data)
    udp_socket.close()


class MyComponent(Grasshopper.Kernel.GH_ScriptInstance):
    def RunScript(self,
            messages: System.Collections.Generic.List[object],
            obj_str: System.Collections.Generic.List[str]):
        if messages is None:
            return None

        script_log_data = "\n".join(messages)
        # obj_data = obj_str.encode()
        data = {
            "script_log": script_log_data,
            "obj_file_paths": list(obj_str),
        }
        data = json.dumps(data)
        send_data(data.encode())
        a = data
        return data
