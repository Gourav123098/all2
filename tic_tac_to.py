import math
import random

class player:
    def __init__(self,letter):
        #letter # or o
        self.letter = letter
    def get_move(self,game):
        #every player getting their next move
        pass
    
class computerplayer(player):
    def __init__(self,letter):
        super().__init__(letter)
    def get_move(self,game):
        pass

class humanplayer(player):
    def __init__(self,letter):
        super().__init__(letter)
    def get_move(self,game):
        pass