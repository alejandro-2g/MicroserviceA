import zmq
import json
import random

# List of randomized reminder messages
reminder_messages = [
    "Don't forget to take a break!",
    "Stay focused! You're doing great!",
    "Time flies! Get back to work!",
    "Procrastination won't finish your tasks!",
    "Just a friendly reminder to keep going!"
]

def reminder_service():
    """Simple ZeroMQ microservice that sends a random reminder message when requested."""
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://127.0.0.1:5555")  # Local use only

    print("🔔 Reminder microservice is running on localhost:5555...")

    while True:
        request = socket.recv().decode()
        print(f"📥 Received request: {request}")

        if request == "get_reminder":
            message = random.choice(reminder_messages)
            response = json.dumps({"message": message})
        else:
            response = json.dumps({"error": "Invalid request"})

        socket.send_string(response)
        print(f"📤 Sent response: {response}")

if __name__ == "__main__":
    reminder_service()
