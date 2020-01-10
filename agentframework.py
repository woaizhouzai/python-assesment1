# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 20:09:22 2019

@author: ZHOU_YuZHAO
"""

import random
class Agent():
    lists=[]
    def __init__(self, environment, agents, y, x):
        if (x == None):
            self.x = random.randint(0,100)
        else:
            self.x = x
        if (y == None):
            self.y = random.randint(0,100)
        else:
            self.y = y
        self.environment = environment
        self.agents = agents
        self.store = 0 # To judge whether share or not
    
    def move(self):
        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100

        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100
    def eat(self): 
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10


# When sheeps come close, they should share their food!            
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) +
                ((self.y - agent.y)**2))**0.5
                
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            distance = self.distance_between(agent)
            if distance <= neighbourhood:
                Sum = self.store + agent.store
                average = Sum / 2
                self.store = agent.store = average