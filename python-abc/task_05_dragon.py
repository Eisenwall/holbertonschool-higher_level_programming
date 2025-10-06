#!/usr/bin/env python3
"""
Module demonstrating mixins with Dragon class
"""


class SwimMixin:
    """Mixin providing swimming ability"""

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Mixin providing flying ability"""

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class combining swim and fly abilities"""

    def roar(self):
        print("The dragon roars!")
