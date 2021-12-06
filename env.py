import numpy as np
import cv2
from track import track
from ego import vehicle
from render import renderer
import time
import json

class swarm_env():
    def __init__(self,num_ego):
        self.num_ego = num_ego

        # Loading all the cars and their params from the json file
        self.vehicles = []
        with open('swarmBots.json', 'r') as f:
            swarmBots = json.load(f)
        
        # Adding the cars to the env
        for bot in swarmBots.keys():
            car = vehicle(swarmBots[bot][0],swarmBots[bot][1],gains=[swarmBots[bot][2],swarmBots[bot][3]])
            self.vehicles.append(car)

        # Loading the track
        self.__track = track()
        self.__track_image = self.__track.gen_track()

        self.sim_delay = 0.01
        self.x_offset = self.__track.win_size_x//2
        self.y_offset = self.__track.win_size_y//2 

        # initializing the renderer
        self.renderer = renderer(self.__track_image,self.x_offset,self.y_offset)

    def run(self,):
        
        # Setting the target value for set point tracking
        target = [0,400]
        st = time.time()
        dt = self.sim_delay

        # Main loop
        while(True):


            # Moving the cars
            for car in self.vehicles:
                car.move(target,dt)
            
            
            # trackpoint for the only rendering purpose
            track_point = [target[1] + self.x_offset, -target[0] + self.y_offset]
            self.renderer.render_swarm(self.vehicles,track_point)

            time.sleep(self.sim_delay)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            dt = time.time() - st - self.sim_delay
            st = time.time()
        
e= swarm_env(1)
e.run()