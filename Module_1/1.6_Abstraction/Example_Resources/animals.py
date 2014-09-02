from abc import ABCMeta, abstractmethod

class Animal:
    
    __metaclass__ = ABCMeta

    name = ""
    location = ""

    def __init__(self, name, location):
        self.name = name
        self.location = location

    @abstractmethod
    def talk():
        pass

    @abstractmethod
    def move():
        pass

    @abstractmethod
    def breathe():
        pass