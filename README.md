# python-assesment1

There are five files contained in my repositorie: data.csv, agentframework.py, data.py, in.txt, main.py.

It is necessary to run data.py and agentframework.py before main.py since they are important modules for running the main program.
(They were imported in the main.py)

This program realises a simple animation of sheep eating grass. When running the program, 10 random point are the sheeps, they can move on
a figur--that is grass.

The background of this program is a "grassland" of 100*100. Sheeps(the random point)can  move on the grassland(function move) and can eat grass(function eat).
Besides, there is a function "distance_between" which is used to judge whether the distance of sheeps are shorter than a certain value(the neiighbour set here is 20).
They will share with their neighbourhood when they get close(function share_with_neighbours).

Most of the behaviour function are wrapped in class Agent which is stored in agentframework.py,
therefore the main program only needs to call this class through the establishment of objects.

The data (figure) is wrapped in data.py. The data is read from the txt file and written to the CSV file. The main program calls the data and draws the background map.

Two windows will pop up when running main.py, one is figure(try to eliminate it but failed), the other is model. Click Run model on the model window to start running.

After testing, the program can run normally. 
The possible direction of development: refine the animation, and control the lamb's moving track through the user's keyboard or mouse, in the form of a game of many people greedy snake.

Most of the codes were from minerva, and no other origin.

Template of license: MIT License
