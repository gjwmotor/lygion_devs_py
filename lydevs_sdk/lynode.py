#!/usr/bin/env python

from .lydevs_def import *
from .protocol_packet_handler import *
from .group_sync_read import *
from .group_sync_write import *

#波特率定义
LY_NODE_1M = 0
LY_NODE_0_5M = 1
LY_NODE_250K = 2
LY_NODE_128K = 3
LY_NODE_115200 = 4
LY_NODE_76800 = 5
LY_NODE_57600 = 6
LY_NODE_38400 = 7

#内存表定义
#-------EPROM(只读)--------
LY_NODE_MODEL_L = 3
LY_NODE_MODEL_H = 4

#-------EPROM(读写)--------
LY_NODE_ID = 5
LY_NODE_BAUD_RATE = 6

#-------SRAM(读写)--------
LY_NODE_PWM_CH1 = 34
LY_NODE_PWM_CH2 = 36
LY_NODE_RGB_CTL = 42
LY_NODE_RGB_CH1 = 43
LY_NODE_RGB_CH2 = 44
LY_NODE_LOCK  = 51

#-------SRAM(只读)--------
LY_NODE_SBUS_STATUS = 67
LY_NODE_ADC_CH1 = 100

class NodeClass(protocol_packet_handler):
    def __init__(self, portHandler):
        protocol_packet_handler.__init__(self, portHandler, 0)
        self.groupSyncWrite = GroupSyncWrite(self, LY_NODE_PWM_CH1, 11)
        self.sbus_frame = [0] * 17

    #根据led的ch将rgb(0~7)颜色传输至node模块缓存
    def ledSingleCtrl(self, node_id, led_ch, r, g, b):
        rgb = ((r<<6)|(g<<3)|(b<<1) & 0xFF)
        ch = led_ch + LY_NODE_RGB_CH1 - 1
        return self.write1ByteTxRx(node_id, ch, rgb)

    #刷新node模块点亮相应led灯
    def ledFlush(self, node_id, led_num):
         return self.write1ByteTxRx(node_id, LY_NODE_RGB_CTL, led_num)

    #全部led写入相同rgb(0~7)颜色传输至node模块缓存
    def ledAllCtrl(self, node_id, num, r, g, b):
        rgb = ((r<<6)|(g<<3)|(b<<1) & 0xFF)
        txpacket = [num] + [rgb] * num
        return self.writeTxRx(node_id, LY_NODE_RGB_CTL, len(txpacket), txpacket)

    #将node模块中sbus数据通过总线缓存至内存
    def sbusFlush(self, node_id):
        self.sbus_frame, result, error = self.readTxRx(node_id, LY_NODE_SBUS_STATUS, len(self.sbus_frame))
        return result, error

    #解码sbus缓存返回通道数据
    def sbusGetch(self, ch):
        return self.sbus_frame[1+(ch-1)]

    #解码sbus缓存返回状态
    def sbusStatus(self):
        return self.sbus_frame[0]

    #subs通道数
    def subsGetNum(self):
        return len(self.sbus_frame) - 1

    #控制node的PWM通道输出:0~1000
    def pwmCtl(self, node_id, pwm_ch, pwm_val):
        return self.write2ByteTxRx(node_id, LY_NODE_PWM_CH1+(pwm_ch-1)*2, pwm_val)

    #获取adc_ch的adc值(0~4095)
    def adcGetch(self, node_id, adc_ch):
        return self.read2ByteTxRx(node_id, LY_NODE_ADC_CH1+(adc_ch-1)*2)

    #adc通道值(adc_ch1)转电源电压
    def adcPowVol(self, node_id):
        adc_val, result, error = self.adcGetch(node_id, 1)
        pow_vol = 0.0
        if result == COMM_SUCCESS:
            pow_vol = ((5.0/4096)*adc_val*(10.0+1.0))
        return pow_vol, result, error

    def LockEprom(self, scs_id):
        return self.write1ByteTxRx(scs_id, LY_NODE_LOCK, 1)

    def unLockEprom(self, scs_id):
        return self.write1ByteTxRx(scs_id, LY_NODE_LOCK, 0)

