import cv2
import numpy as np
import matplotlib.pyplot as plt
import pyrealsense2 as rs
from PIL import Image
from Essential_module import *
from Studentclass import *

# 높이 값을 받아오게 된다.
def TakePhoto(student):

    pipe = rs.pipeline()
    cfg = rs.config()
    cfg.enable_stream(rs.stream.depth, 320, 240, rs.format.z16, 30)
    cfg.enable_stream(rs.stream.color, 640,480, rs.format.bgr8,30)



    profile = pipe.start(cfg)
    while True:
        for x in range(5):
            pipe.wait_for_frames()

        frameset = pipe.wait_for_frames()
        depth_frame = frameset.get_depth_frame()
        color_frame = frameset.get_color_frame()

        color_image = np.asanyarray(color_frame.get_data())

        cv2.imshow('Picture of a food', color_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        Input = input("위 사진을 사용하시겠습니까? (Y/N): ")
        
        if Input == 'Y':
            break
    if student is not None:
        student.Firstimage = color_image

    pipe.stop()
    print('Frame Captured')
    
    
    # 사진 돌리기



    matrix = [[0]*height]*width
    for i in range(width):
        for j in range(height):
            matrix[i][j]=depth_frame.get_distance(i,j)
    return matrix


def showPhoto(student):
    cv2.imshow('Picture of a food' , student.Firstimage)
    cv2.waitKey(0)