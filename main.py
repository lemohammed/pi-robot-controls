from fastapi import FastAPI
from robot import unlockRobot, runAutomation, connect, robot
from valves import ValveManager
import json

app = FastAPI()

@app.get('/open-all')
def open_all(): 
    ValveManager.init()
    ValveManager.all_on()

@app.get('/close-all')
def close_all():
    ValveManager.init()
    ValveManager.all_off()

@app.get("/unlock-robot")
def read_root():
    connect()
    unlockRobot()


@app.get("/run")
def run():
    runAutomation()


@app.get("/off")
def deactivateRobot():
    robot.DeactivateRobot()

@app.get('/record/joints')
def record_joins():
    l = robot.GetJoints()

    with open('seq.json','r') as f:
        data = json.read(f)

    with open('seq.json','w') as f:
        json.dump(l,[*data,f])

    return l


@app.get('/run/seq')
def run_sequence():
    with open('seq.json','r') as f:
        data = json.read(f)
    for joint in joins:
        robot.MoveJoints(*joints)