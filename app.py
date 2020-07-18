import pyautogui
from flask import Flask, jsonify, request
from flask_cors import CORS

variable = 2

X0 = -1
Y0 = -1
StartCoords = False

app = Flask(__name__)

CORS(app)


@app.route('/api', methods=['POST'])
def Api():
    if(StartCoords):
        Touches = request.json
        if(len(Touches) == 1):
            X = Touches[0]['x']
            Y = Touches[0]['y']
            if(0 < X and X < 1 and 0 < Y and Y < 1):
                screenWidth, screenHeight = pyautogui.size()
                currentMouseX, currentMouseY = pyautogui.position()
                moveX = currentMouseX + ((X-X0) * screenWidth / variable)
                moveY = currentMouseY + ((Y-Y0) * screenHeight / variable)
                print(moveX)
                pyautogui.moveTo(moveX, moveY)

    return 'ok'

@app.route('/start',methods=['POST'])
def Start():
    global StartCoords
    if not (StartCoords):
        global X0
        global Y0
        X0 = request.json['x']
        Y0 = request.json['y']
        StartCoords = True
    return 'ok'

@app.route('/stop', methods=['POST'])
def Stop():
    global StartCoords
    StartCoords = False
    return 'ok'


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
