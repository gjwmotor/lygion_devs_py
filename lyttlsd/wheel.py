#!/usr/bin/env python
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

scs_comm_result, scs_error = packetHandler.WheelMode(1)
if scs_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(scs_comm_result))
elif scs_error != 0:
    print("%s" % packetHandler.getRxPacketError(scs_error))

while 1:
    # TTLSD (ID1) accelerates to a maximum speed of V=600 * 0.9375=562.5rpm and an acceleration of A=250*4, forward rotation
    # Goal Current=150
    scs_comm_result, scs_error = packetHandler.WriteSpec(1, 600, 0, 150)
    if scs_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(scs_comm_result))
    elif scs_error != 0:
        print("%s" % packetHandler.getRxPacketError(scs_error))
    else :
        print("V=600 * 0.9375=562.5rpm and an acceleration of A=250*4, forward rotation", flush=True)

    time.sleep(5);

    # TTLSD (ID1) decelerates to speed 0 and stops rotating at an acceleration of A=250*4
    # Goal Current=150
    scs_comm_result, scs_error = packetHandler.WriteSpec(1, 0, 0, 150)
    if scs_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(scs_comm_result))
    elif scs_error != 0:
        print("%s" % packetHandler.getRxPacketError(scs_error))
    else :
        print("stops rotating at an acceleration of A=250*4")
        
    time.sleep(2);

    # TTLSD (ID1/ID2) accelerates to a maximum speed of V=600 * 0.9375=562.5rpm and an acceleration of A=250*4, reverse rotation
    # Goal Current=150
    scs_comm_result, scs_error = packetHandler.WriteSpec(1, -600, 0, 150)
    if scs_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(scs_comm_result))
    elif scs_error != 0:
        print("%s" % packetHandler.getRxPacketError(scs_error))
    else :
        print("V=600 * 0.9375=562.5rpm and an acceleration of A=250*4, reverse rotation")
    
    time.sleep(5);

    # TTLSD (ID1) decelerates to speed 0 and stops rotating at an acceleration of A=250*4
    # Goal Current=150
    scs_comm_result, scs_error = packetHandler.WriteSpec(1, 0, 0, 150)
    if scs_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(scs_comm_result))
    elif scs_error != 0:
        print("%s" % packetHandler.getRxPacketError(scs_error))
    else :
        print("stops rotating at an acceleration of A=250*4")
    
    time.sleep(2);
    
# Close port
portHandler.closePort()
