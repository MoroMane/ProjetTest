# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 19:35:31 2017

@author: 3520543
"""


import toolboxmodif

from soccersimulator.strategies  import Strategy
from soccersimulator.mdpsoccer import SoccerTeam, Simulation
from soccersimulator.gui import SimuGUI,show_state,show_simu

from soccersimulator import Vector2D, SoccerState, SoccerAction
from soccersimulator import Simulation, SoccerTeam, Player, show_simu
from soccersimulator import Strategy
from soccersimulator import settings
import math


## Strategie aleatoire
class RandomStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Random")
    def compute_strategy(self,state,id_team,id_player):
        return SoccerAction(Vector2D.create_random(-1,1),Vector2D.create_random(-1,1))

class Attaque2Strategie(Strategy):
    def __init__(self,name="Attaque"):
        Strategy.__init__(self,name)
    def compute_strategy(self,state,idteam,idplayer):
        #faire qqe chose d intelligent
    
        mystate = toolboxmodif.MyState(state,idteam,idplayer)
        myaction= toolboxmodif.MyAction(mystate)
        return myaction.action_attaquant()
        #return SoccerAction(vecteur_vitesse,vecteur_shoot)

class DefenseStrategie(Strategy):
    def __init__(self,name="defense"):
        Strategy.__init__(self,name)
    def compute_strategy(self,state,idteam,idplayer):
        mystate = toolboxmodif.MyState(state,idteam,idplayer)
        myaction= toolboxmodif.MyAction(mystate)
        return myaction.action_def()

