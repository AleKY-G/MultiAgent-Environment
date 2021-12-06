import numpy as np
import cv2

class track():
    def __init__(self,):
        self.win_size_x = 1000
        self.win_size_y = 1000

    def gen_track(self,):

        # simple black screen
        trk = np.zeros((self.win_size_x, self.win_size_y,3))

        return trk