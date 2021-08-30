import time, zmq

def set_up_socket():
        context = zmq.Context()
        push_socket = context.socket(zmq.PUSH)

        #ip needs to be adjusted to consumer ip
        #now running with localhost
        push_socket.bind("tcp://*:5555")

        return push_socket

def send_message(socket, message):
        socket.send_string(message)

push_socket = set_up_socket()

while True:
        time.sleep(1)
        send_message(push_socket, "Test")

