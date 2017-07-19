# -*- coding:utf-8 -*-
import logging
from smbus import SMBus

logger = logging.getLogger(__name__)


class LightSensor(object):

    I2C_BUS_ID = 1  # Default: 1 for RPI 2, RPI 3
    DEVICE = 0x23  # Default device I2C address

    # Start measurement at 4lx resolution. Time typically 16ms.
    CONTINUOUS_LOW_RES_MODE = 0x13
    # Start measurement at 1lx resolution. Time typically 120ms
    CONTINUOUS_HIGH_RES_MODE_1 = 0x10
    # Start measurement at 0.5lx resolution. Time typically 120ms
    CONTINUOUS_HIGH_RES_MODE_2 = 0x11
    # Start measurement at 1lx resolution. Time typically 120ms
    # Device is automatically set to Power Down after measurement.
    ONE_TIME_HIGH_RES_MODE_1 = 0x20
    # Start measurement at 0.5lx resolution. Time typically 120ms
    # Device is automatically set to Power Down after measurement.
    ONE_TIME_HIGH_RES_MODE_2 = 0x21
    # Start measurement at 1lx resolution. Time typically 120ms
    # Device is automatically set to Power Down after measurement.
    ONE_TIME_LOW_RES_MODE = 0x23

    def __init__(self):
        self.bus = SMBus(LightSensor.I2C_BUS_ID)

    def read_light(self):
        try:
            data = self.bus.read_i2c_block_data(LightSensor.DEVICE, LightSensor.ONE_TIME_HIGH_RES_MODE_1)
            return LightSensor.convert_to_number(data)
        except Exception as e:
            logger.info(e.message)
            return -1

    @staticmethod
    def convert_to_number(data):
        # Simple function to convert 2 bytes of data into a decimal number
        return (data[1] + (256 * data[0])) / 1.2
