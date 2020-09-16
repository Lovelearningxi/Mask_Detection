#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/31 13:49
# @Author  : WangXi
# @Site    :
# @File    : detection.py
# @Software: PyCharm

import cv2
import paddlehub as hub


def Mask_detect(image):
    state = '未戴口罩'
    module = hub.Module(name="pyramidbox_lite_mobile_mask")
    input_dict = {"data": [image]}

    results = module.face_detection(data=input_dict)
    result = results[0]
    for i in result['data']:
        x1 = i['left']
        y1 = i['top']
        x2 = i['right']
        y2 = i['bottom']
        kz = i['label']

        image = cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 2)
        cv2.putText(image, str(kz), (x1 - 5, y1 - 10), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0, 0, 255), 1)
        if kz == 'MASK':
            state = '已戴口罩'

        return image, len(result['data']), state
