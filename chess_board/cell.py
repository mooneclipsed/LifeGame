import random


class Cell:
    """Store the information of every cell"""
    def __init__(self):
        self.status = random.choice([True, False])
        self.x = ''
        self.y = ''

    def show_status(self):
        print(self.status)