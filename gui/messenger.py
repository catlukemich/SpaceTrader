from pygame.mixer import Sound
from game.dock import *
from gui.gui import *
from queue import Queue

class Messenger(Text, DockListener):
    ''' Class responsible form maintaining state and displaying of messages at the bottom of the UI '''

    def __init__(self):
        Text.__init__(self, pygame.font.Font("assets/gui/LCD14.ttf", 15))
        self.setPosition(300, 770)
        self.setText("Messenger")
        self.queue = Queue()
        self.duration = 3000 # Message display duration in milliseconds.
        self.time = 0
        self.message = None

    def update(self, clock):
        if self.message != None:
            delta_time_ms = clock.get_time()
            self.time += delta_time_ms
            if self.time > self.duration:
                self.message = None
        elif not self.queue.empty():
            message = self.queue.get()
            self.message = message
            self.setText(message)
            beep = Sound("assets/sounds/beep.ogg")
            beep.play()
            self.time = 0
        else:
            self.setText("")


    def onDockCargoProduced(self, dock, cargo):
        if cargo.amount == cargo.capacity:
            message = cargo.name + " is full at " + dock.name
            self.putMessage(message)
        pass

    def onDockCargoConsumed(self, dock, cargo):
        if cargo.amount == 0:
            message = cargo.name + " has depleted at " + dock.name
            self.putMessage(message)
        pass


    def putMessage(self, message):
        self.queue.put(message)