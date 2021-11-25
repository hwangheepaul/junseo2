import pyrealsense2 as rs
import numpy as np
import cv2
import os

# Configure depth and color streams
pipeline = rs.pipeline()
config = rs.config()
# Get device product line for setting a supporting resolution
pipeline_wrapper = rs.pipeline_wrapper(pipeline)
pipeline_profile = config.resolve(pipeline_wrapper)
device = pipeline_profile.get_device()
device_product_line = str(device.get_info(rs.camera_info.product_line))
found_rgb = False
for s in device.sensors:
    if s.get_info(rs.camera_info.name) == 'RGB Camera':
        found_rgb = True
        break
if not found_rgb:
    print("The demo requires Depth camera with Color sensor")
    exit(0)

config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config.enable_stream(rs.stream.depth, 320, 240, rs.format.z16, 30)

if device_product_line == 'L500':
    config.enable_stream(rs.stream.color, 960, 540, rs.format.bgr8, 30)
    config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
else:
    config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

# Start streaming
pipeline.start(config)

while True:
    # Wait for a coherent pair of frames: depth and color
    frames = pipeline.wait_for_frames()
    depth_frame = frames.get_depth_frame()
    color_frame = frames.get_color_frame()

    pipeline.stop()

    if not depth_frame or not color_frame:
        continue
    # Convert images to numpy arrays
    depth_image = np.asanyarray(depth_frame.get_data())
    color_image = np.asanyarray(color_frame.get_data(),dtype=np.uint8)
    # Apply colormap on depth image (image must be converted to 8-bit per pixel first)
    depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)
    depth_colormap_dim = depth_colormap.shape
    color_colormap_dim = color_image.shape
    # If depth and color resolutions are different, resize color image to match depth image for display
    if depth_colormap_dim != color_colormap_dim:
        resized_color_image = cv2.resize(color_image, dsize=(depth_colormap_dim[1], depth_colormap_dim[0]), interpolation=cv2.INTER_AREA)
        images = np.hstack((resized_color_image, depth_colormap))
    else:
        images = np.hstack((color_image, depth_colormap))
    
    imggray=cv2.cvtColor(color_image,cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(imggray,(5,5),cv2.BORDER_DEFAULT)
    cv2.imshow('Blur',blur)

    canny = cv2.Canny(blur, 100,175)
    cv2.imshow('Canny Edges', canny)

    ret, thresh = cv2.threshold(imggray,75, 255, cv2.THRESH_BINARY) # threshold는 이미지를 binary하게 만든다. 행렬값중 원소가 125보다 작으면 0으로, 125보다 크면 255로 만든다 -> thresh에 변경된 행렬이 저장됨

    cv2.imshow('Thresh',thresh)

    # #imggray = np.float32(imggray)
    # corners=cv2.cornerHarris(imggray,2,3,0.04)
    # corners=cv2.dilate(corners,None)
    # color_image[corners>0.01*corners.max()]=[0,0,255]
    # #cv2.imshow('corner',color_image)
    
    # contours,hierarchy=cv2.findContours(imggray,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_TC89_KCOS)
    # for contour in contours:
    #     color_image=cv2.drawContours(color_image,[contour],-1,(0,0,255),2)
    # cv2.imshow('color_image',color_image)
    
    contours, cnts ,hierarchies = cv2.findContours(canny,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    print(len(cnts))
    cv2.drawContours(color_image,cnts,-1,(0,255,0),1) 
    
    
    
    cv2.imshow('tree',color_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()