# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 20:38:44 2019

@author: ZHOU_YuZHAO
"""

import random
import operator
import agentframework
import data
import matplotlib
import matplotlib.pyplot
import matplotlib.animation 
import tkinter
import requests
import bs4

matplotlib.use('TkAgg')

r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
#print(td_ys)
#print(td_xs)


num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20
agents = [] 

environment = data.environment

# Make the agents.


#for i in range(num_of_agents):
#    agents.append(agentframework.Agent(environment, agents))

for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(environment, agents, y, x))
    
# Create the figure
fig = matplotlib.pyplot.figure()

root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)



# Every time it runs, update the window
def update(frame_number):
    fig.clear()
    # Move the agents.
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
    
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.imshow(environment)

    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
        
        
# Run this model
def run():
    
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=num_of_iterations, repeat=False)
    canvas.draw()


# Create the model,and the GUI
menu = tkinter.Menu(root)
root.config(menu=menu)
model_menu = tkinter.Menu(menu)
menu.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)

tkinter.mainloop()


# Another method
#animation = matplotlib.animation.FuncAnimation(fig, update, frames=num_of_iterations, repeat=False)
#matplotlib.pyplot.show()
    
#    matplotlib.pyplot.clf()
#    matplotlib.pyplot.xlim(0, 99)
#    matplotlib.pyplot.ylim(0, 99)
#    matplotlib.pyplot.imshow(environment)
#
#    for i in range(num_of_agents):
#        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
#    matplotlib.pyplot.draw()
#    matplotlib.pyplot.pause(0.1)
#
#
#matplotlib.pyplot.show()