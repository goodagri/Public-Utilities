#!/usr/bin/env python
# coding: utf-8
# 2021 12 18 arimoto
#前提　AWSキー等は持たせている

import time
while True:
    try:
        import yaml
        import glob
        import numpy as np
        import logging
        import logging.handlers
        import boto3
        import cv2
        import os
        import datetime
        from boto3.dynamodb.conditions import Key, Attr
        break
    except:
        time.sleep(10)


def shooting():
    deviceid = 0
    width = 1640
    height = 1232
    nframes = 15
    interval = 4
    time.sleep(1)
    saved_dir = "./data\\temp\\"
    savename = "./data\\temp\\img_" 
    # saved_dir = "./data/temp/"
    # savename = "./data/temp/img_" 
    cap = cv2.VideoCapture(deviceid)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,height)  
    cap.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*"JPEG"))
    os.makedirs(saved_dir, exist_ok=True)
    x = 0
    while True:
        ret, img = cap.read()
        cv2.imwrite(savename + str(x) + ".jpg", img)
        time.sleep(0.5)
        if x == nframes-1:
            break
        else:
            x = x + 1
            time.sleep(interval-0.5) 
    cap.release()
    cv2.destroyAllWindows()
    time.sleep(3)    
try:
        shooting()
except:
    print("Error")
