import cv2
import numpy as np

class renderer():
    def __init__(self,track,x_offset,y_offset):
        self.track = track
        self.x_offset = x_offset
        self.y_offset = y_offset

    def carBody(self,x_loc,y_loc,yaw_angle,trk):

        y0 = -int(x_loc)+self.x_offset
        x0 =  int(y_loc)+self.y_offset

        b = np.cos(yaw_angle) * 10
        a = np.sin(yaw_angle) * 10
        pt0 = (int(x0 - a - b), int(y0 + b - a))
        pt1 = (int(x0 + a - b), int(y0 - b - a))
        pt2 = (int(2 * x0 - pt0[0]), int(2 * y0 - pt0[1]))
        pt3 = (int(2 * x0 - pt1[0]), int(2 * y0 - pt1[1]))

        cv2.line(trk, pt1, pt2, (0, 0, 255), 2) # Car front
        cv2.line(trk, pt0, pt1, (0,255,255), 2) # Car color
        cv2.line(trk, pt2, pt3, (0,255,255), 2)
        cv2.line(trk, pt3, pt0, (0,255,255), 2)

        return trk
    
    def render_swarm(self,vehicles,track_point):
        trk = self.track.copy()
        trk = cv2.circle(trk, tuple(track_point), 5, (255,0,0), -1)
        trk = cv2.circle(trk, tuple(track_point), 10, (255,0,0), 2)
        
        for car in vehicles:
            trk = self.carBody(car.x_loc,car.y_loc,car.yaw_angle,trk)

        cv2.imshow('swarm',trk)
        cv2.waitKey(1)