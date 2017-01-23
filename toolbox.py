# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 18:31:09 2017

@author: 3520543
"""


from soccersimulator.strategies  import Strategy
from soccersimulator.mdpsoccer import SoccerTeam, Simulation
from soccersimulator.gui import SimuGUI,show_state,show_simu

from soccersimulator import Vector2D, SoccerState, SoccerAction
from soccersimulator import Simulation, SoccerTeam, Player, show_simu
from soccersimulator import Strategy
from soccersimulator import settings
import math

class MyState(object):
    def __init__(self,state,idteam,idplayer):
        self.state = state
        self.idteam=idteam
        self.idplayer= idplayer
        self.key = (idteam,idplayer)
    def my_position(self):
        return self.state.player_state(self.key[0], self.key[1]).position
        #equivalent a self.player_state(self.key[0],self.key[1])
    def ball_position(self):
        return self.state.ball.position
    def aller(self,p):
        return SoccerAction(p-self.my_position(),Vector2D())
    def shoot(self,p):
        return SoccerAction(Vector2D(),p-self.state.my_position())
