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
def record_joints():
    l = robot.GetJoints()

    with open('seq.json','r') as f:
        data = json.load(f)

    with open('seq.json','w') as f:
        json.dump([*data,l],f,)

    return l



@app.get('/record/valve')
def record_valves(valve:int, state: int,delay:int):
    l=[valve,state,delay]
    with open('seq.json','r') as f:
        data = json.load(f)

    with open('seq.json','w') as f:
        json.dump([*data,l],f,)
    return l


@app.get('/connect')
def connect_robot():
    connect()

@app.get('/clear')
def clear_seq():
    with open('seq.json','w') as f:
        json.dump([],f,)


@app.get('/run/seq')
def run_sequence():
    connect()

    unlockRobot()

    with open('seq.json','r') as f:
        data = json.load(f)
        
    for seq in data:
        if (len(seq) == 3):
            ValveManager.run(*seq)
        else:
            robot.MoveJoints(*seq)