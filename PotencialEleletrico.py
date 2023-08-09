import matplotlib.pyplot as plt
import numpy as np

class Charge:
    def __init__(self, position, value, color):
        self.position = position
        self.value = value
        self.color = color 
        
class ElectricFieldApp:
    def __init__(self):
        self.charges = []
        self.colors = ['red', 'blue', 'green', 'purple']
        self.fig, self.ax = plt.subplots()
        self.ax.set_aspect('equal')
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-10, 10)
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.grid(True)
        self.cid = self.fig.canvas.mpl_connect('button_press_event', self.on_click)
        self.selected_point = None
        