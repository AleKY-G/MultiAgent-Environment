import numpy as np
from controller import Controller

class vehicle():
    # A template code for a PID based controller
    # gains --> PID Gains
    def __init__(self,init_loc=[0,0],yaw=0,gains = [[0.8,0.0,0.5,0],
                                                    [1.4,0.0,0,0.0]]):

        self.x_loc,self.y_loc = init_loc # forward, left-right
        self.yaw_angle = yaw

        self.vel = 0
        self.omega = 0
    
        self.car_controller = Controller(gains)
    
    def move(self,target_loc,dt):
        x_error = target_loc[0] - self.x_loc
        y_error = target_loc[1] - self.y_loc

        # ---------USING CONTROLLER -------------------------
        '''Values from the controller'''
        # self.vel, self.omega = self.car_controller.track([x_error,y_error], self.yaw_angle)

        # --------DEFAULT THROTTLE -------------------------
        '''Default values to run the environment, use your controller code as stated above to get the velocity commands.
           Comment the line below while using your controller.'''
        self.vel,self.omega = 10,0


        self.yaw_angle = self.yaw_angle + self.omega*dt

        self.x_loc = self.x_loc + self.vel*np.cos(self.yaw_angle)*dt
        self.y_loc = self.y_loc + self.vel*np.sin(self.yaw_angle)*dt









