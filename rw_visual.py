import matplotlib.pyplot as plt
from random import choice
from randomwalk import RandomWalk


# to keep the program running
while True: 
    rw = RandomWalk()
    rw.fill_walk()
    plt.scatter(rw.x_values, rw.y_values,c = choice(['red','black','blue']), s=3)
    plt.title("random walk with 5000 steps", fontsize = 10)
    plt.show()
    
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
    
    
