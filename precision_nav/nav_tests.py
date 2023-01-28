import matplotlib.pyplot as plt
import sys

sys.path.append("..")
from navigation_helper import *
from navigation_utilites import *


class PrecisionTest:

    def __init__(self):
        print("Starting test for precision navigation.")

        self.waypoints = [(205, 96.5), (205, 93.5), (248, 120), (248, 70)]

        plt.figure()
        xs = [w[0] for w in self.waypoints]
        ys = [w[1] for w in self.waypoints]
        plt.plot(xs, ys, 'o', color="orange")

        gen_waypoints = precisionNavigationImpl(self.waypoints)
        xs = [w[0] for w in gen_waypoints]
        ys = [w[1] for w in gen_waypoints]
        colors = [
            'lime', 'g', 'aqua', 'deepskyblue', 'indigo', 'darkviolet',
            'magenta', 'r', 'pink'
        ]
        labels = [
            'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh',
            'eighth', 'ninth'
        ]
        for i in range(len(xs)):
            plt.plot(xs[i], ys[i], 'x', color=colors[i], label=labels[i])
            plt.annotate(labels[i], # this is the text
                 (xs[i],ys[i]), # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center')

            

        plt.show()