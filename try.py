# import time

# bar = [
#     " [=     ]",
#     " [ =    ]",
#     " [  =   ]",
#     " [   =  ]",
#     " [    = ]",
#     " [     =]",
#     " [    = ]",
#     " [   =  ]",
#     " [  =   ]",
#     " [ =    ]",
# ]
# i = 0

# while True:
#     print(bar[i % len(bar)], end="\r")
#     time.sleep(.2)
#     i += 1
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
i=0
im = plt.imshow(arr[0], animated=True)
def updatefig(*args):
    global i
    if (i<99):
        i += 1
    else:
        i=0
    im.set_array(arr[i])
    return im,
ani = animation.FuncAnimation(fig, updatefig,  blit=True)
plt.show()