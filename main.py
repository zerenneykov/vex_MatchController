import PySimpleGUI as sg
import time

global autoTimer
global opTimer
global autOn
global opOn

autoTimer = 0
autOn = False
opTimer = 0
opOn = False



# creates elements

progAuto = sg.ProgressBar(15,orientation='horizontal',size=(50,7), border_width=2, key='-APROGRESS_BAR-',bar_color=('White','Black'))
progOp = sg.ProgressBar(60,orientation='horizontal',size=(50,7), border_width=2, key='-OPROGRESS_BAR-',bar_color=('White','Black'))
startAuto = sg.Button("Start Auto")
startOp = sg.Button("Start Op")
reset = sg.Button("Reset")
setStateOp = sg.Button("Set Driver Control")
setStateAuto = sg.Button("Set Autonomous Control")
setStateDis = sg.Button("Set State Disabled")

# defines layout
lyt = [[sg.Text("Autonomous Period",size=(15,1))] ,[progAuto], [sg.Text("Driver Period",size=(15,1),justification='center')], [progOp], [startAuto, startOp, reset, ], [setStateAuto, setStateOp, setStateDis]]


# functions for keeping track of time and updating progress bar
def autoPro():
    global autoTimer
    while autOn:
        if autoTimer == 15:
            break
        autoTimer = autoTimer + 1
        window['-APROGRESS_BAR-'].update(autoTimer)
        time.sleep(1)

def opPro():
    global opTimer
    while opOn:
        opTimer = opTimer + 1
        window['-OPROGRESS_BAR-'].update(opTimer)
        time.sleep(1)
        

# creates window

window = sg.Window("Match Controller", lyt, size=(580,200), element_justification='center')


# window loop

while True:
    event, values=window.read()

    # if start auto button is pressed
    if event=="Start Auto":
        autOn = True
        window.perform_long_operation(autoPro, '-END_AUTO-')
    
    if event=="Start Op":
        opOn = True
        window.perform_long_operation(opPro, '-END_OP-')
    
    # once long op is done, placeholder, all math is done inside the function
    if event=='-END_AUTO-':
        print(autoTimer)
        autOn = False
    
    if event=='-END_OP-':
        autOn = False

    if event=="Reset":
        autOn = False
        autoTimer = 0
        window['-APROGRESS_BAR-'].update(autoTimer)
        opOn = False
        opTimer = 0
        window['-OPROGRESS_BAR-'].update(opTimer)

    if event== sg.WIN_CLOSED:
        break
window.close()
