#!/usr/bin/env python
#
# *********     Ping Example      *********
#
#
# Available lydevs model on this example : All models using Protocol SCS
# This example is tested with a lydevs(node)
#

import sys
import os

sys.path.append("..")
from lydevs_sdk import *                   # Uses lydevs_sdk library


def read(SCS_ID):
    while 1:
        # Read the current position of TTLSD(SCS_ID)
        scs_present_position, scs_present_speed, scs_comm_result, scs_error = packetHandler.ReadPosSpeed(SCS_ID)
        if scs_comm_result != COMM_SUCCESS:
            print(packetHandler.getTxRxResult(scs_comm_result))
        else:
            print("[ID:%03d] PresPos:%d PresSpd:%d" % (SCS_ID, scs_present_position, scs_present_speed))
        if scs_error != 0:
            print(packetHandler.getRxPacketError(scs_error))

        # Read moving status of TTLSD(SCS_ID)
        moving, scs_comm_result, scs_error = packetHandler.ReadMoving(SCS_ID)
        if scs_comm_result != COMM_SUCCESS:
            print(packetHandler.getTxRxResult(scs_comm_result))

        if moving==0:
            break
    return
        
# Initialize PortHandler instance
# Set the port path
# Get methods and members of PortHandlerLinux or PortHandlerWindows
portHandler = PortHandler('/dev/ttyUSB0')# ex) Windows: "COM1"   Linux: "/dev/ttyUSB0" Mac: "/dev/tty.usbserial-*"

# Initialize PacketHandler instance
# Get methods and members of Protocol
packetHandler = TTLSDClass(portHandler)
    
# Open port
if portHandler.openPort():
    print("Succeeded to open the port")
else:
    print("Failed to open the port")
    quit()

# Set port baudrate 1000000
if portHandler.setBaudRate(1000000):
    print("Succeeded to change the baudrate")
else:
    print("Failed to change the baudrate")
    quit()

while 1:
    # TTLSD (ID1) runs at a maximum speed of V=600 * 0.9375=562.5rpm and an acceleration of A=250*4 until it reaches position P1=3200
    # Goal Current=150
    scs_comm_result, scs_error = packetHandler.WritePosEx(1, 3200, 600, 0, 150)
    if scs_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(scs_comm_result))
    elif scs_error != 0:
        print("%s" % packetHandler.getRxPacketError(scs_error))

    read(1)# Read the status of the servo (ID1) until the servo runs to the target position
    time.sleep(0.2)
    
    # TTLSD (ID1) runs at a maximum speed of V=600 * 0.9375=562.5rpm and an acceleration of A=250*4 until it reaches position P1=0
    # Goal Current=150
    scs_comm_result, scs_error = packetHandler.WritePosEx(1, 0, 600, 0, 150)
    if scs_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(scs_comm_result))
    elif scs_error != 0:
        print("%s" % packetHandler.getRxPacketError(scs_error))
    
    read(1)# Read the status of the servo (ID1) until the servo runs to the target position
    time.sleep(0.2)

# Close port
portHandler.closePort()

