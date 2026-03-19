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


# Initialize PortHandler instance
# Set the port path
# Get methods and members of PortHandlerLinux or PortHandlerWindows
portHandler = PortHandler('/dev/ttyUSB0') #ex) Windows: "COM1"   Linux: "/dev/ttyUSB0" Mac: "/dev/tty.usbserial-*"

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
    # TTLSD (ID1~10) runs at a maximum speed of V=600 * 0.9375=562.5rpm and an acceleration of A=250*4 until it reaches position P1=3200
    # Goal Current=150
    for scs_id in range(1, 11):
        scs_comm_result, scs_error = packetHandler.RegWritePosEx(scs_id, 3200, 600, 0, 150)
        if scs_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(scs_comm_result))
        if scs_error != 0:
            print("%s" % packetHandler.getRxPacketError(scs_error))
    packetHandler.RegAction()
    
    time.sleep(((3200-0)/(60*50) + (60*50)/(1000*100) + 0.05))#[(P1-P0)/(V*50)] + [(V*50)/(A*100)] + 0.05
    
    # TTLSD (ID1~10) runs at a maximum speed of V=600 * 0.9375=562.5rpm and an acceleration of A=250*4 until it reaches position P1=0
    # Goal Current=150
    for scs_id in range(1, 11):
        scs_comm_result, scs_error = packetHandler.RegWritePosEx(scs_id, 0, 600, 0, 150)
        if scs_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(scs_comm_result))
        if scs_error != 0:
            print("%s" % packetHandler.getRxPacketError(scs_error))
    packetHandler.RegAction()
    
    time.sleep(((3200-0)/(60*50) + (60*50)/(1000*100) + 0.05))#[(P1-P0)/(V*50)] + [(V*50)/(A*100)] + 0.05

# Close port
portHandler.closePort()
