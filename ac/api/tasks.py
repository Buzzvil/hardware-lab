# -*- coding:utf-8 -*-
import logging
from celery import shared_task

from api.utils import LightSensor

logger = logging.getLogger(__name__)

THRESHOLD_LIGHT_LEVEL = 5
WINDOW_RANGE = 100
MIN_COUNT = 70

@shared_task
def check_light():
    light_sensor = LightSensor()
    count = 0
    for _ in range(WINDOW_RANGE):
        light_level = light_sensor.read_light()
        if light_level < 0:
            # Invalid - fail to read light
            continue
        if light_level < THRESHOLD_LIGHT_LEVEL:
            count += 1

    if count > MIN_COUNT:
        logger.info('Light is off - Turn off the AC (count : {0}/{1})'.format(count, WINDOW_RANGE))
        # TODO : turn off the AC
    else:
        logger.info('Light is on')