# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 19:35:31 2017

@author: 3520543
"""


import toolboxmodif1

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

class Fonceur(Strategy):
    def __init__(self,name="ma strategie"):
        Strategy.__init__(self,name)

    def compute_strategy(self,state,idteam,idplayer):
        #faire qqe chose d intelligent
        vb= state.ball.position                             #position du ballon (vecteur 2d)
        v1= state.player_state(idteam,idplayer).position    #position du joueur (vecteur 2d)
        if (idteam==1):
            v2= Vector2D(150,45)
        if (idteam==2):
            v2= Vector2D(0,45)
        if (vb-v1).norm <= settings.PLAYER_RADIUS + settings.BALL_RADIUS:
            return SoccerAction(Vector2D(),v2-vb)
        else :
            return SoccerAction((vb-v1)+state.ball.vitesse,Vector2D())

class Attaque2Strategie(Strategy):
    def __init__(self,name="Attaque"):
        Strategy.__init__(self,name)
    def compute_strategy(self,state,idteam,idplayer):
        #faire qqe chose d intelligent
    
        mystate = toolboxmodif1.MyState(state,idteam,idplayer)
        myaction= toolboxmodif1.MyAction(mystate)
        return myaction.action_attaquant()
        #return SoccerAction(vecteur_vitesse,vecteur_shoot)

class DefenseStrategie_2v2(Strategy):
    def __init__(self,name="defense"):
        Strategy.__init__(self,name)
    def compute_strategy(self,state,idteam,idplayer):
        mystate = toolboxmodif1.MyState(state,idteam,idplayer)
        myaction= toolboxmodif1.MyAction(mystate)
        return myaction.action_def_2v2()

class DefenseStrategie_4v4(Strategy):
    def __init__(self,name="defense"):
        Strategy.__init__(self,name)
    def compute_strategy(self,state,idteam,idplayer):
        mystate = toolboxmodif1.MyState(state,idteam,idplayer)
        myaction= toolboxmodif1.MyAction(mystate)
        return myaction.action_def_4v4()

class GardienStrategie(Strategy):
    def __init__(self,name="Gardien"):
        Strategy.__init__(self,name)
    def compute_strategy(self,state,idteam,idplayer):
        mystate = toolboxmodif1.MyState(state,idteam,idplayer)
        myaction= toolboxmodif1.MyAction(mystate)
        return myaction.action_gardien()

class MilieuStrategie(Strategy):
    def __init__(self,name="Milieu"):
        Strategy.__init__(self,name)
    def compute_strategy(self,state,idteam,idplayer):
        mystate = toolboxmodif1.MyState(state,idteam,idplayer)
        myaction= toolboxmodif1.MyAction(mystate)
        return myaction.action_milieu()
        
        
class Attaque4Strategie(Strategy):
    def __init__(self,name="Attaque"):
        Strategy.__init__(self,name)
    def compute_strategy(self,state,idteam,idplayer):
        #faire qqe chose d intelligent
    
        mystate = toolboxmodif1.MyState(state,idteam,idplayer)
        myaction= toolboxmodif1.MyAction(mystate)
        return myaction.action_attaquant4()