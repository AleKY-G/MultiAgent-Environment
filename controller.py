import numpy as np

class Controller():

    def __init__(self,gains=[[0.8,0.0,0.5,0],
                             [1.4,0.0,0,0.0]]):

        self.Gains = np.array(gains)

        self.vels = np.array([0,0])

    def track(self,error, heading_angle):
        # Write your controller here. Template is made for PID. 
        # For other controllers, change the shape of the gains in the __init__ function
        outputs = [0,0] # Default values
        return outputs

