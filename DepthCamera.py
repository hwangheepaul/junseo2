import cv2
import numpy as np
import matplotlib.pyplot as plt
import pyrealsense2 as rs
from Essential_module import *

# 높이 값을 받아오게 된다.
def TakePhoto():
    pipe = rs.pipeline()
    cfg = rs.config()
    cfg.enable_stream(rs.stream.depth, 320, 240, rs.format.z16, 30)



    profile = pipe.start(cfg)

    for x in range(5):
        pipe.wait_for_frames()

    frameset = pipe.wait_for_frames()
    depth_frame = frameset.get_depth_frame()

    pipe.stop()
    print('Frame Captured')

    # 사진 돌리기

    matrix = [[0]*height]*width
    for i in range(width):
        for j in range(height):
            matrix[i][j]=depth_frame.get_distance(i,j)
    return matrix