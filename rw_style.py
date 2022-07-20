import matplotlib.pyplot as plt
from randomwalk import RandomWalk


# to keep the program running
while True: 
    rw = RandomWalk()
    rw.fill_walk()
    
    #set the size of the plotting window
    #plt.figure(figsize=(6, 6))
    
    '''
    use a colormap to show the order of the points in the walk and then 
    remove the black outline from each dot so the color of the dots will be 
    clearer
    '''
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values,c=point_numbers,
                cmap=plt.cm.Blues, edgecolor='none', s=3)
    plt.title("simulating the shape of clouds", fontsize = 10)  
    
    #remove the axes
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    
    plt.show()
    
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
    
    
