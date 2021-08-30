import zmq,time

def set_up_socket():
    context = zmq.Context()
    pull_socket = context.socket(zmq.PULL)
    
    #ip needs to be adjusted
    #now running with localhost
    pull_socket.connect("tcp://localhost:5555")

    return pull_socket

def start_receiving_loop(socket):

    while True:
        time.sleep(1)
        message = socket.recv()
        print(message)

pull_socket = set_up_socket()
start_receiving_loop(pull_socket)