#!/usr/bin/env python3
"""
Module demonstrating Abstract Base Class (ABC) usage
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class representing an animal"""

    @abstractmethod
    def sound(self):
        """Abstract method to be implemented by subclasses"""
        pass


class Dog(Animal):
    """Dog subclass of Animal"""

    def sound(self):
        """Return the sound a dog makes"""
        return "Bark"


class Cat(Animal):
    """Cat subclass of Animal"""

    def sound(self):
        """Return the sound a cat makes"""
        return "Meow"
