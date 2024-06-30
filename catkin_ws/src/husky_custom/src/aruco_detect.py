#! /usr/bin/env python3
import rospy
from std_msgs.msg import String, Float32
import numpy as np
import time
import cv2
import pyrealsense2 as rs
import cv2

## This portion is for the realsense
class DepthCamera:
    def __init__(self):
        # Configure depth and color streams
        self.pipeline = rs.pipeline()
        config = rs.config()

        # Get device product line for setting a supporting resolution
        pipeline_wrapper = rs.pipeline_wrapper(self.pipeline)
        pipeline_profile = config.resolve(pipeline_wrapper)
        device = pipeline_profile.get_device()
        device_product_line = str(device.get_info(rs.camera_info.product_line))

        config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
        config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

        # Start streaming
        self.pipeline.start(config)

    def get_frame(self):
        align_to = rs.stream.color
        align = rs.align(align_to)

        frames = self.pipeline.wait_for_frames()
        aligned_frames = align.process(frames)
        aligned_depth_frame = rs.decimation_filter(2.0).process(aligned_frames.get_depth_frame())
        aligned_depth_frame = rs.spatial_filter().process(aligned_depth_frame)
        aligned_depth_frame = rs.temporal_filter().process(aligned_depth_frame)
        aligned_depth_frame = rs.hole_filling_filter().process(aligned_depth_frame)
        aligned_depth_frame = aligned_frames.get_depth_frame()
        color_frame = aligned_frames.get_color_frame()
        depth_frame = aligned_frames.get_depth_frame()

        # depth_frame = frames.get_depth_frame()
        # color_frame = frames.get_color_frame()

        depth_image = np.asanyarray(depth_frame.get_data())
        color_image = np.asanyarray(color_frame.get_data())
        if not depth_frame or not color_frame:
            return False, None, None
        return True, depth_image, color_image

    def release(self):
        self.pipeline.stop()

class Aruco:

    def calc_midpoint(self, x1, x2, y1, y2):
        return int((x1 + x2)/2), int((y1 + y2)/2)

    ARUCO_DICT = {
        "DICT_4X4_50": cv2.aruco.DICT_4X4_50,
        "DICT_4X4_100": cv2.aruco.DICT_4X4_100,
        "DICT_4X4_250": cv2.aruco.DICT_4X4_250,
        "DICT_4X4_1000": cv2.aruco.DICT_4X4_1000,
        "DICT_5X5_50": cv2.aruco.DICT_5X5_50,
        "DICT_5X5_100": cv2.aruco.DICT_5X5_100,
        "DICT_5X5_250": cv2.aruco.DICT_5X5_250,
        "DICT_5X5_1000": cv2.aruco.DICT_5X5_1000,
        "DICT_6X6_50": cv2.aruco.DICT_6X6_50,
        "DICT_6X6_100": cv2.aruco.DICT_6X6_100,
        "DICT_6X6_250": cv2.aruco.DICT_6X6_250,
        "DICT_6X6_1000": cv2.aruco.DICT_6X6_1000,
        "DICT_7X7_50": cv2.aruco.DICT_7X7_50,
        "DICT_7X7_100": cv2.aruco.DICT_7X7_100,
        "DICT_7X7_250": cv2.aruco.DICT_7X7_250,
        "DICT_7X7_1000": cv2.aruco.DICT_7X7_1000,
        "DICT_ARUCO_ORIGINAL": cv2.aruco.DICT_ARUCO_ORIGINAL,
        "DICT_APRILTAG_16h5": cv2.aruco.DICT_APRILTAG_16h5,
        "DICT_APRILTAG_25h9": cv2.aruco.DICT_APRILTAG_25h9,
        "DICT_APRILTAG_36h10": cv2.aruco.DICT_APRILTAG_36h10,
        "DICT_APRILTAG_36h11": cv2.aruco.DICT_APRILTAG_36h11
    }

    tags = rospy.Publisher("/aruco_tag_info", String, queue_size=10)

    aruco_type = "DICT_4X4_50"

    arucoDict = cv2.aruco.getPredefinedDictionary(ARUCO_DICT[aruco_type])

    arucoParams = cv2.aruco.DetectorParameters()

if __name__ == "__main__":
    rospy.init_node("aruco_detect")

    aruco = Aruco()
    depth_cam = DepthCamera()

    # aruco_reached_pub = rospy.Publisher("/aruco_reached", Float32, queue_size=10)

    try:
        data_string = None
        while not rospy.is_shutdown():
            state, depth_frame, img = depth_cam.get_frame()
            corners, ids, rejected = cv2.aruco.detectMarkers(img, aruco.arucoDict, parameters=aruco.arucoParams)
        
            if len(corners) > 0:
                aruco_state = "1"
                topleft = corners[0][0][0]
                topright = corners[0][0][1]
                bottomright = corners[0][0][2]
                bottomleft = corners[0][0][3]
                x, y = aruco.calc_midpoint(topleft[0], bottomright[0], topleft[1], bottomright[1])
                distance = depth_frame[y, x]
                data_string = aruco_state + " " + str(distance) + " " + str(x) + " " + str(y) + " " + str(ids)

                cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
                cv2.rectangle(img, (int(topleft[0]), int(topleft[1])), (int(bottomright[0]), int(bottomright[1])), (255, 0, 0), 5)

                print(f"Aruco tag ID: {ids}")
                print(f"Center: {x}, {y}")
                print(f"Distance: {distance}")
            else:
                aruco_state = "0"
                data_string = aruco_state
                # aruco_reached_pub.publish(0.0)
            aruco.tags.publish(data_string)  
            cv2.imshow("RGB Frame", img)    

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break   
        
    finally:
        print("shutting dowb")
        depth_cam.release()