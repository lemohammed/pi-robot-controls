from fastapi import FastAPI
from robot import unlockRobot, runAutomation


app = FastAPI()


@app.get("/unlock-robot")
def read_root():
    unlockRobot()


@app.get("/run")
def read_root():
    runAutomation()


@app.get("/off")
def read_root():
    robot.DeactivateRobot()
