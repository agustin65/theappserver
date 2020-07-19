import pyautogui
from flask import Flask, jsonify, request
from flask_cors import CORS

pyautogui.FAILSAFE = False

variable = 3

X0 = -1
Y0 = -1
StartCoords = False

app = Flask(__name__)

CORS(app)

@app.route('/move', methods=['POST'])
def Move():
    X = request.json['x']
    Y = request.json['y']
    if(-1 < X and X < 1 and -1 < Y and Y < 1):
        screenWidth, screenHeight = pyautogui.size()
        currentMouseX, currentMouseY = pyautogui.position()
        moveX = currentMouseX + (X * screenWidth / variable)
        moveY = currentMouseY + (Y * screenHeight / variable)
        if(0 > moveY):
            moveY = 0
        if(0 > moveX):
            moveX = 0
        if(moveY > screenHeight):
            moveY = screenHeight-1
        if(moveX > screenWidth):
            moveX = screenWidth-1
        pyautogui.moveTo(moveX,moveY)
    return 'ok'

@app.route('/click')
def Click():
    pyautogui.click()
    return 'ok'


@app.route('/api', methods=['POST'])
def Api():
    global StartCoords
    global X0
    global Y0
    Touches = request.json
    if(StartCoords):
        if(len(Touches) == 0):
            StartCoords = False
        elif(len(Touches) == 1):
            X = Touches[0]['x']
            Y = Touches[0]['y']
            if(0 < X and X < 1 and 0 < Y and Y < 1):
                screenWidth, screenHeight = pyautogui.size()
                currentMouseX, currentMouseY = pyautogui.position()
                moveX = currentMouseX + ((X-X0) * screenWidth / variable)
                moveY = currentMouseY + ((Y-Y0) * screenHeight / variable)
                if(0 < moveY and moveY < screenHeight and 0 < moveX and moveX < screenWidth ):
                    pyautogui.moveTo(moveX, moveY)
                elif(0 < moveY and moveY < screenHeight):
                    pyautogui.moveTo(0, moveY)
                elif(0 < moveX and moveX < screenWidth):
                    pyautogui.moveTo(moveX, 0)
    else:
        X0 = Touches[0]['x']
        Y0 = Touches[0]['y']
        StartCoords = True
    return 'ok'



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
