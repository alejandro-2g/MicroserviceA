import zmq
import json

def request_reminder():
    """Requests a reminder from the microservice."""
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://127.0.0.1:5555")

    print("\n📌 Requesting a reminder...")

    socket.send_string("get_reminder")
    response = socket.recv().decode()
    
    data = json.loads(response)
    print(f"🔔 Reminder Received: {data['message']}")

if __name__ == "__main__":
    request_reminder()

