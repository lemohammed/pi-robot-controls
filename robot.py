from valves import ValveManager
import mecademicpy.robot as mdr
import json
from time import sleep


robot = mdr.Robot()

def connect():
    robot.Connect(address='192.168.0.100',
                  disconnect_on_exception=False, enable_synchronous_mode=True)
    robot.ActivateRobot()
    robot.Home()


def home():
    robot.MoveJoints(0, 0, 0, 0, 0, 0)

def unlockRobot():
    robot.DeactivateRobot()
    robot.ActivateRobot()

def disconnect():
    robot.DeactivateRobot()
    robot.Disconnect()

def pick():
    robot.MoveLinRelWrf(0, 0, -200, 0, 0, 0)
    robot.MoveLinRelWrf(0, 0, 200, 0, 0, 0)


def goToAssemblyLocation(location):
    robot.MoveJoints(*location)


def save_locations(locations):
    with open('joint-locations.json', 'w') as f:
        json.dump(locations, f)


def load_locations():
    with open('joint-locations.json',) as f:
        locations = json.load(f)
    return locations


def moveTo(location):
    print(location)
    robot.MoveJoints(*location)


def runAutomation():
    P1, P2, P3 = load_locations()
    connect()
    unlockRobot()
    sleep(1)
    moveTo([0, 0, 0, 0, 0, 0])
    for _ in range(3):
        robot.MoveJoints(*P1)
        robot.MoveJoints(*P2)

    moveTo([0, 0, 0, 0, 0, 0])
    moveTo(P3)
    home()
