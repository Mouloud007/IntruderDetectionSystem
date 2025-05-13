# Intruder Detection System

This project is a real-time intruder detection system that uses **YOLO object detection**, **face recognition**, and **mask detection** to identify individuals and determine if they are wearing masks. The system sends alerts via **MQTT** and **email notifications** and streams the video feed through a **Flask web server**.

---

## Features

- **Person Detection**: Detects people in the video feed using a YOLO model.
- **Mask Detection**: Identifies whether a person is wearing a mask or not using a custom YOLO model.
- **Face Recognition**: Matches detected faces with a database of known faces to identify intruders.
- **Alerts**:
  - Sends intruder alerts via MQTT.
  - Sends email notifications when an intruder is detected.
- **Real-Time Video Streaming**: Streams the video feed through a Flask web server.
- **Face Database Management**:
  - Create and reset a face database.
  - Add new faces to the database.

---

## Installation

### Prerequisites
- **Python 3.8+**
- **Raspberry Pi Camera** (or any compatible camera)
- **YOLOv8** pre-trained model
- **Custom YOLO model** for mask detection
- **SQLite** for face database
- **MQTT Broker** (e.g., Mosquitto)
- **SMTP Email Account** for sending alerts

### Required Python Libraries
Install the required libraries using `pip`:

```bash
pip install opencv-python flask ultralytics paho-mqtt face_recognition smtplib numpy sqlite3 picamera2

## File Descriptions

### **1. `face_mask_detetion.py`**
This is the main script that runs the intruder detection system.

#### Key Features:
- **Person and Mask Detection**: Uses YOLO models to detect people and masks.
- **Face Recognition**: Matches detected faces with known faces in the database.
- **Alerts**:
  - Sends MQTT alerts to the configured broker.
  - Sends email notifications to the configured recipient.
- **Video Streaming**: Streams the video feed via Flask at `http://<RASPBERRY_PI_IP>:5000/video_feed`.

#### How to Run:
```bash
python face_mask_detetion.py
```

---

### **2. `create_face_database.py`**
This script creates and resets the SQLite database for storing known faces.

#### How to Run:
```bash
python create_face_database.py
```

---

### **3. `add_faces_to_database.py`**
This script adds new faces to the database. It processes images from a specified folder and stores their encodings in the database.

#### How to Use:
1. Place images of a person in a folder (e.g., `known_faces/Person_Name`).
2. Update the `image_directory` and `person_name` variables in the script.
3. Run the script:
   ```bash
   python add_faces_to_database.py
   ```

---

## Configuration

### **MQTT Configuration**
Update the following variables in `face_mask_detetion.py`:
```python
mqtt_broker = "192.168.1.000"  # Replace with your MQTT broker's IP address
mqtt_port = 1883  # MQTT port
mqtt_topic_intruder = "home/intruder_alert"  # Topic for intruder alerts
```

### **Email Configuration**
Set up your email credentials in `face_mask_detetion.py`:
```python
EMAIL_SENDER = os.getenv("your_email@gmail.com")  # Sender's email address
EMAIL_PASSWORD = os.getenv("your_app_password")  # App password for the sender's email
EMAIL_RECEIVER = os.getenv("receiver_email@gmail.com")  # Recipient's email address
EMAIL_COOLDOWN = 10  # Minimum time (in seconds) between email alerts
```

### **YOLO Models**
- **General Object Detection**: Place the YOLOv8 model file (`yolov8n.pt`) in the project directory.
- **Mask Detection**: Place the custom YOLO model (`best.pt`) in the specified path.

---

## Usage

1. **Set Up the Face Database**:
   - Run `create_face_database.py` to create/reset the database.
   - Run `add_faces_to_database.py` to add known faces to the database.

2. **Start the Intruder Detection System**:
   - Run `face_mask_detetion.py`:
     ```bash
     python face_mask_detetion.py
     ```
   - Access the video feed at `http://<RASPBERRY_PI_IP>:5000/video_feed`.

3. **Monitor Alerts**:
   - MQTT alerts will be sent to the configured broker.
   - Email notifications will be sent for intruder detections.

---

## Project Structure

```
Intruder Detection System/
├── face_mask_detetion.py         # Main script for intruder detection
├── create_face_database.py       # Script to create/reset the face database
├── add_faces_to_database.py      # Script to add faces to the database
├── known_faces/                  # Folder containing images of known faces
├── faces.db                      # SQLite database for storing face encodings
├── yolov8n.pt                    # YOLOv8 model for general object detection
├── best.pt                       # Custom YOLO model for mask detection
```

---

## Future Improvements
- Add support for multiple cameras.
- Enhance mask detection accuracy with additional training data.
- Implement a web-based dashboard for managing the face database and monitoring alerts.

---

## License
This project is licensed under the MIT License. Feel free to use and modify it as needed.

---

## Acknowledgments
- **YOLOv8** by [Ultralytics](https://github.com/ultralytics/yolov8).
- **Face Recognition** library by [Adam Geitgey](https://github.com/ageitgey/face_recognition).
- **Flask** for web streaming.
- **Paho MQTT** for MQTT communication.
```

---
