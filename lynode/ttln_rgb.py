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
    # node_id=1, rgb_ch=1, rgb=3:0:0
    scs_comm_result, scs_error = packetHandler.ledSingleCtrl(1, 1, 3, 0, 0)
    # node_id=1, rgb_ch=2, rgb=3:0:0
    scs_comm_result, scs_error = packetHandler.ledSingleCtrl(1, 2, 0, 0, 3)
    # node_id=1, led_num=2, flush rgb
    scs_comm_result, scs_error = packetHandler.ledFlush(1, 2)
    if scs_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(scs_comm_result))
    elif scs_error != 0:
        print("%s" % packetHandler.getRxPacketError(scs_error))
    time.sleep(1)

   # node_id=1, rgb_ch=all, rgb=0:0:0
    scs_comm_result, scs_error = packetHandler.ledAllCtrl(1, 2, 0, 0, 0)
    if scs_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(scs_comm_result))
    elif scs_error != 0:
        print("%s" % packetHandler.getRxPacketError(scs_error))
    time.sleep(1);

    # node_id=1, rgb_ch=1, rgb=0:7:0
    scs_comm_result, scs_error = packetHandler.ledSingleCtrl(1, 1, 3, 0, 0)
    # node_id=1, rgb_ch=2, rgb=0:7:0
    scs_comm_result, scs_error = packetHandler.ledSingleCtrl(1, 2, 0, 0, 3)
    # node_id=1, led_num=2, flush rgb
    scs_comm_result, scs_error = packetHandler.ledFlush(1, 2)
    if scs_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(scs_comm_result))
    elif scs_error != 0:
        print("%s" % packetHandler.getRxPacketError(scs_error))
    time.sleep(1)

   # node_id=1, rgb_ch=all, rgb=0:0:0
    scs_comm_result, scs_error = packetHandler.ledAllCtrl(1, 2, 0, 0, 0)
    if scs_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(scs_comm_result))
    elif scs_error != 0:
        print("%s" % packetHandler.getRxPacketError(scs_error))
    time.sleep(1)

    # node_id=1, rgb_ch=1, rgb=0:0:3
    scs_comm_result, scs_error = packetHandler.ledSingleCtrl(1, 1, 0, 0, 3)
    # node_id=1, rgb_ch=2, rgb=0:0:3
    scs_comm_result, scs_error = packetHandler.ledSingleCtrl(1, 2, 3, 0, 0)
    # node_id=1, led_num=2, flush rgb
    scs_comm_result, scs_error = packetHandler.ledFlush(1, 2)
    if scs_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(scs_comm_result))
    elif scs_error != 0:
        print("%s" % packetHandler.getRxPacketError(scs_error))
    time.sleep(1)

   # node_id=1, rgb_ch=all, rgb=0:0:0
    scs_comm_result, scs_error = packetHandler.ledAllCtrl(1, 2, 0, 0, 0)
    if scs_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(scs_comm_result))
    elif scs_error != 0:
        print("%s" % packetHandler.getRxPacketError(scs_error))
    time.sleep(1)

# Close port
portHandler.closePort()
