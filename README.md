# 🔔 Reminder Microservice (Microservice A)

This microservice provides **randomized reminder messages** using **ZeroMQ**.  
It follows a simple **request-response** pattern to deliver motivational and task reminders.

📌 **Key Features**
- ✅ Uses **ZeroMQ** for lightweight communication.
- ✅ Provides **random motivational reminders** on request.
- ✅ Simple **command-line interface (CLI)**.
- ✅ Easy to set up and run locally.

---

## 🚀 **How to Install & Run**
Follow these steps to set up and run the microservice on your local machine.

### **📥 1. Install Required Dependencies**
Ensure you have **Python** installed, then install the required package:
```bash
pip install pyzmq

```
🖥️ 2. Start the Microservice
Run the microservice server:

```bash
python reminder_service.py
```
Expected Output:
```bash
Reminder microservice is running on localhost:5555...
```
Run the Test Client
```bash
python test_client.py
```
Example output: 
```bash
📌 Requesting a reminder...
🔔 Reminder Received: "Time flies! Get back to work!"
```
How to Request a Reminder
```bash
"get_reminder"
```
Example response
```bash
"message": "Time flies! Get back to work!"
```
## UML Diagram
![UML Sequence Diagram](UML.png)

