# ------
# Robot.py class
# This runs the robot.
# Copyright 2015. Pioneers in Engineering.
# ------
from grizzly import *
#import hibike.hibike as sensors
from Gamepads import *
#import Motors


motor = {}
name_to_grizzly = {}
runtime_ansible = None
allData = {} 

def init():
    addrs = Grizzly.get_all_ids()
    addrs = Grizzly.get_all_ids()
#    runtime_ansible = Ansible('runtime')

    #h = hibike.Hibike()
    #connectedDevices = h.getEnumeratedDevices() #get list of devices
    #h.subscribeToDevices(connectedDevices) #subscribe to devices

    # Brute force to find all
    for index in range(len(addrs)):
        # default name for motors is motor0, motor1, motor2, etc
        grizzly_motor = Grizzly(addrs[index])
        grizzly_motor.set_mode(ControlMode.NO_PID, DriveMode.DRIVE_COAST)
        grizzly_motor.limit_acceleration(142)
        grizzly_motor.limit_current(10)
        grizzly_motor.set_target(0)

        name_to_grizzly['motor' + str(index)] = grizzly_motor
        #motor['motor' + str(index)] = grizzly_motor.get_target()

    #print(name_to_grizzly, addrs)

def get_motor(name):
    #return motor[name]
    return None

def set_motor(name, value):
    #print(name_to_grizzly)
    grizzly = name_to_grizzly[name]
    grizzly.set_target(value)
    #motor[name] = value

# TODO: implement


def update():
    command =student_ansible.recv()
    if command:
	msg_type, content = command['header']['msg_type'], command['content']
	if msg_type == "sensor_value":
            allData = content 
            print(allData)

def get_sensor(name):
    if name in allData:
        return allData[name]
    return 'Error'#searched list

def get_all_motors():
    return motors
