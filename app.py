import pyautogui
from flask import Flask, jsonify, request
from flask_cors import CORS

currentCursorX = 0
currentCursorY = 0

variable = 2

app = Flask(__name__)

CORS(app)


@app.route('/start', methods=['POST'])
def Start():
    global currentCursorX
    global currentCursorY
    currentCursorX = request.json['x']
    currentCursorY = request.json['y']
    return 'ok'


@app.route('/stop', methods=['POST'])
def Stop():
    Comparar(request.json)
    return 'ok'


def Comparar(Obj):
    x = currentCursorX-Obj['x']
    y = currentCursorY-Obj['y']
    if(abs(y) < 0.1 and abs(x) < 0.1):
        pyautogui.click()
    else:
        screenWidth, screenHeight = pyautogui.size()
        currentMouseX, currentMouseY = pyautogui.position()
        moveX = currentMouseX - (x * screenWidth / variable)
        moveY = currentMouseY - (y * screenHeight / variable)
        pyautogui.moveTo(moveX, moveY)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
