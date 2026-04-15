#!/usr/bin/env python

from .lydevs_def import *
from .protocol_packet_handler import *
from .group_sync_read import *
from .group_sync_write import *

#波特率定义
LY_TTLSD_1M = 0
LY_TTLSD_0_5M = 1
LY_TTLSD_250K = 2
LY_TTLSD_128K = 3
LY_TTLSD_115200 = 4
LY_TTLSD_76800 = 5
LY_TTLSD_57600 = 6
LY_TTLSD_38400 = 7

#内存表定义
#-------EPROM(只读)--------
LY_TTLSD_MODEL_L = 3
LY_TTLSD_MODEL_H = 4

#-------EPROM(读写)--------
LY_TTLSD_ID = 5
LY_TTLSD_BAUD_RATE = 6
LY_TTLSD_MIN_ANGLE_LIMIT_L = 9
LY_TTLSD_MIN_ANGLE_LIMIT_H = 10
LY_TTLSD_MAX_ANGLE_LIMIT_L = 11
LY_TTLSD_MAX_ANGLE_LIMIT_H = 12
LY_TTLSD_MODE = 33
#-------SRAM(读写)--------
LY_TTLSD_TORQUE_ENABLE = 40
LY_TTLSD_ACC = 41
LY_TTLSD_GOAL_POSITION_L = 42
LY_TTLSD_GOAL_POSITION_H = 43
LY_TTLSD_GOAL_CURRENT_L = 44
LY_TTLSD_GOAL_CURRENT_H = 45
LY_TTLSD_GOAL_SPEED_L = 46
LY_TTLSD_GOAL_SPEED_H = 47
LY_TTLSD_LOCK = 55

#-------SRAM(只读)--------
LY_TTLSD_PRESENT_POSITION_L = 56
LY_TTLSD_PRESENT_POSITION_H = 57
LY_TTLSD_PRESENT_SPEED_L = 58
LY_TTLSD_PRESENT_SPEED_H = 59
LY_TTLSD_PRESENT_LOAD_L = 60
LY_TTLSD_PRESENT_LOAD_H = 61
LY_TTLSD_PRESENT_VOLTAGE = 62
LY_TTLSD_PRESENT_TEMPERATURE = 63
LY_TTLSD_MOVING = 66
LY_TTLSD_PRESENT_CURRENT_L = 69
LY_TTLSD_PRESENT_CURRENT_H = 70

class TTLSDClass(protocol_packet_handler):
    def __init__(self, portHandler):
        protocol_packet_handler.__init__(self, portHandler, 0)
        self.groupSyncWrite = GroupSyncWrite(self, LY_TTLSD_ACC, 7)

    def WritePosEx(self, scs_id, position, speed, acc, torque):
        txpacket = [acc, self.scs_lobyte(position), self.scs_hibyte(position), self.scs_lobyte(torque), self.scs_hibyte(torque), self.scs_lobyte(speed), self.scs_hibyte(speed)]
        return self.writeTxRx(scs_id, LY_TTLSD_ACC, len(txpacket), txpacket)
    
    def ReadPos(self, scs_id):
        scs_present_position, scs_comm_result, scs_error = self.read2ByteTxRx(scs_id, LY_TTLSD_PRESENT_POSITION_L)
        scs_present_position = scs_present_position & 0xFFFF
        return scs_present_position, scs_comm_result, scs_error

    def ReadSpeed(self, scs_id):
        scs_present_speed, scs_comm_result, scs_error = self.read2ByteTxRx(scs_id, LY_TTLSD_PRESENT_SPEED_L)
        return self.scs_tohost(scs_present_speed, 15), scs_comm_result, scs_error

    def ReadPosSpeed(self, scs_id):
        scs_present_position_speed, scs_comm_result, scs_error = self.read4ByteTxRx(scs_id, LY_TTLSD_PRESENT_POSITION_L)
        scs_present_position = self.scs_loword(scs_present_position_speed) & 0xFFFF
        scs_present_speed = self.scs_hiword(scs_present_position_speed)
        return scs_present_position, self.scs_tohost(scs_present_speed, 15), scs_comm_result, scs_error

    def ReadMoving(self, scs_id):
        moving, scs_comm_result, scs_error = self.read1ByteTxRx(scs_id, LY_TTLSD_MOVING)
        return moving, scs_comm_result, scs_error

    def SyncWritePosEx(self, scs_id, position, speed, acc, torque):
        txpacket = [acc, self.scs_lobyte(position), self.scs_hibyte(position), self.scs_lobyte(torque), self.scs_hibyte(torque), self.scs_lobyte(speed), self.scs_hibyte(speed)]
        return self.groupSyncWrite.addParam(scs_id, txpacket)

    def RegWritePosEx(self, scs_id, position, speed, acc, torque):
        txpacket = [acc, self.scs_lobyte(position), self.scs_hibyte(position), self.scs_lobyte(torque), self.scs_hibyte(torque), self.scs_lobyte(speed), self.scs_hibyte(speed)]
        return self.regWriteTxRx(scs_id, LY_TTLSD_ACC, len(txpacket), txpacket)

    def RegAction(self):
        return self.action(BROADCAST_ID)

    def WheelMode(self, scs_id):
        return self.write1ByteTxRx(scs_id, LY_TTLSD_MODE, 1)

    def WriteSpec(self, scs_id, speed, acc, torque):
        speed = self.scs_toscs(speed, 15)
        txpacket = [acc, 0, 0, self.scs_lobyte(torque), self.scs_hibyte(torque), self.scs_lobyte(speed), self.scs_hibyte(speed)]
        return self.writeTxRx(scs_id, LY_TTLSD_ACC, len(txpacket), txpacket)

    def LockEprom(self, scs_id):
        return self.write1ByteTxRx(scs_id, LY_TTLSD_LOCK, 1)

    def unLockEprom(self, scs_id):
        return self.write1ByteTxRx(scs_id, LY_TTLSD_LOCK, 0)
