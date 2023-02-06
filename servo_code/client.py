import cv2 as cv
import requests
import numpy as np

#servo constants
#serverIP = "10.5.0.211"
serverIP = "localhost"
#serverPort = "2233"
serverPort = "8080"
serverURL = f"http://{serverIP}:{serverPort}"

#servo constants
UD_delta = 100
UD_speed = 100

LR_delta = 100
LR_speed = 100

def makeRequest(endpoint):
    res = requests.get(f"{serverURL}/" + endpoint)
    return res.text

print("Server start status: ", makeRequest("start"))
pin = 1
while True:
    cv.imshow("dummy image", np.zeros([8,8,3], dtype=np.uint8))
    key = cv.waitKey(0)


    if key == 81:
        print(makeRequest(f"update_pos?delta={LR_delta}&speed={LR_speed}&dir=left&pin={pin}"))
        print("Pin 1 servo: " + makeRequest(f"get_pos?pin=1"))
        print("Pin 2 servo: " + makeRequest(f"get_pos?pin=2"))
        print("Pin 3 servo: " + makeRequest(f"get_pos?pin=3"))
        print("Pin 4 servo: " + makeRequest(f"get_pos?pin=4"))
    elif key == 83:
        print(makeRequest(f"update_pos?delta={LR_delta}&speed={LR_speed}&dir=right&pin={pin}"))
        print("Pin 1 servo: " + makeRequest(f"get_pos?pin=1"))
        print("Pin 2 servo: " + makeRequest(f"get_pos?pin=2"))
        print("Pin 3 servo: " + makeRequest(f"get_pos?pin=3"))
        print("Pin 4 servo: " + makeRequest(f"get_pos?pin=4"))

    elif key ==  ord("s"):
        k = cv.waitKey(0)
        if k in [ord("1"), ord("2"), ord("3"), ord("4")]:
            pin = k - ord("0")

    elif key == ord("q"):
        break
    else:
        print("You have entered a wrong key. Do press the correct key")
        continue


cv.destroyAllWindows()