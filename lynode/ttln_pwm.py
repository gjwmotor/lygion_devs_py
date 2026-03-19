#!/usr/bin/env python
#
# *********     Gen Write Example      *********
#
#
# Available lydevs model on this example : All models using Protocol SCS
# This example is tested with a lydevs(node)
#

import sys
import os
import time

sys.path.append("..")
from lydevs_sdk import *                      # Uses lydevs SDK library


# Initialize PortHandler instance
# Set the port path
# Get methods and members of PortHandlerLinux or PortHandlerWindows
portHandler = PortHandler('/dev/ttyUSB0')# ex) Windows: "COM1"   Linux: "/dev/ttyUSB0" Mac: "/dev/tty.usbserial-*"

# Initialize PacketHandler instance
# Get methods and members of Protocol
packetHandler = NodeClass(portHandler)
    
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
    # node_id=1 pwm_ch=1 pwm_val = 0
    scs_comm_result, scs_error = packetHandler.pwmCtl(1, 1, 0)
    if scs_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(scs_comm_result))
    elif scs_error != 0:
        print("%s" % packetHandler.getRxPacketError(scs_error))
    else :
        print("node_id=1 pwm_ch=1 pwm_val = 0")
    
    # node_id=1 pwm_ch=2 pwm_val = 0
    scs_comm_result, scs_error = packetHandler.pwmCtl(1, 2, 0)
    if scs_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(scs_comm_result))
    elif scs_error != 0:
        print("%s" % packetHandler.getRxPacketError(scs_error))
    else :
        print("node_id=1 pwm_ch=2 pwm_val = 0")
    time.sleep(0.5)

     # node_id=1 pwm_ch=1 pwm_val = 500
    scs_comm_result, scs_error = packetHandler.pwmCtl(1, 1, 500)
    if scs_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(scs_comm_result))
    elif scs_error != 0:
        print("%s" % packetHandler.getRxPacketError(scs_error))
    else :
        print("node_id=1 pwm_ch=1 pwm_val = 500")
    
    # node_id=1 pwm_ch=2 pwm_val = 500
    scs_comm_result, scs_error = packetHandler.pwmCtl(1, 2, 500)
    if scs_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(scs_comm_result))
    elif scs_error != 0:
        print("%s" % packetHandler.getRxPacketError(scs_error))
    else :
        print("node_id=1 pwm_ch=2 pwm_val = 500")
    time.sleep(0.5)

    # node_id=1 pwm_ch=1 pwm_val = 1000
    scs_comm_result, scs_error = packetHandler.pwmCtl(1, 1, 1000)
    if scs_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(scs_comm_result))
    elif scs_error != 0:
        print("%s" % packetHandler.getRxPacketError(scs_error))
    else :
        print("node_id=1 pwm_ch=1 pwm_val = 1000")
    
    # node_id=1 pwm_ch=2 pwm_val = 1000
    scs_comm_result, scs_error = packetHandler.pwmCtl(1, 2, 1000)
    if scs_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(scs_comm_result))
    elif scs_error != 0:
        print("%s" % packetHandler.getRxPacketError(scs_error))
    else :
        print("node_id=1 pwm_ch=2 pwm_val = 1000")
    time.sleep(0.5)

# Close port
portHandler.closePort()
