## 2-DOF Arm 

In this Module, I've added the client-server model for live streaming the data from the camera along with the object tracking code which also moves the servos according to the object position

Run the arm.py file in Raspi using the command `python3 arm.py`
Run the client.py file in the system with the command `python3 client.py <HOST-IP> -p 8080 --no-bgr2rgb`