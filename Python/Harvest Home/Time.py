import pygame

class time:
    def __init__(self,length,value = None):
        self.length=length
        self.value=value
        self.timeInit=0
        self.init=False

    def Initialize(self):
        self.init=True
        self.timeInit= pygame.time.get_ticks()

    def Uninitialize(self):
        self.init=False
        self.timeInit=0

    def check(self):
        realTime=pygame.time.get_ticks()
        if realTime - self.timeInit >= self.length:
            self.Uninitialize()
            if self.value:
                self.value()