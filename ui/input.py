from tkinter import *
from tkinter.ttk import *

class InputWindow:

    def __init__(self):
        super().__init__()

        self.title("Generation: Settings")
        self.geometry('325x164+375+258')
        self.terrain = StringVar()
        self.algorithm = StringVar()

    def build(self):
        frame = Frame(self)
        # heading label
        Label(frame, text='Configure Settings', font=(None,'10', 'bold')).grid(row=0, column=0, columnspan=2, pady=10) 
        Label(frame, text='Terrain:').grid(row=2, column=0, sticky=W, pady=5) # terrain label 
        terrains = [             # list of generation algorithms
            "Terrains..",
            "Blank",
            "Mine Field",
            "Pre-Made Maze"
        ]
        OptionMenu(frame, self.terrain, *terrains).grid(row=2, column=1, sticky=E) # terrain dropdown
        Label(frame, text='Finding:').grid(row=3, column=0, sticky=W)
        Button(frame, text='Open Grid', width=30, command=self.open_grid).grid(row=4, column=0, columnspan=2, pady=10)
        search_algos = [             # list of generation algorithms
            "Algorithms..",
            "A*",
            "Dijkstra"
        ]
        OptionMenu(frame, self.algorithm, *search_algos).grid(row=3, column=1, sticky=E) # pathfinding algorithm dropdown
        frame.pack()

    def getTerrain(self):
        return self.terrain.get()

    def getAlgorithm(self):
        return self.algorithm.get()