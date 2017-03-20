# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 18:55:37 2017

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
import logging
logging.basicConfig(level = 10)

class FrappeStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Frappe")
    def compute_strategy(self,state,idteam,idplayer):
        mystate = toolboxmodif1.MyState(state,idteam,idplayer)
        myaction= toolboxmodif1.MyAction(mystate)
        if mystate.peut_frapper():
            return myaction.shoot_but()
        else :
            return myaction.aller_vers_balle()
        
class DribbleStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Dribble")
    def compute_strategy(self,state,idteam,idplayer):
        mystate = toolboxmodif1.MyState(state,idteam,idplayer)
        myaction= toolboxmodif1.MyAction(mystate)
        if (mystate.peut_frapper()):
            return myaction.pousse_ball()
        else :    
            return myaction.aller_vers_balle()
            

class PasseStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Passe")
    def compute_strategy(self,state,idteam,idplayer):
        mystate = toolboxmodif1.MyState(state,idteam,idplayer)
        myaction= toolboxmodif1.MyAction(mystate)
        if (mystate.peut_frapper()):
            return myaction.passe_2v2()
        else :    
            return myaction.aller_vers_balle()

class Replacement_attaquant_Strategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Replacement offensif")
    def compute_strategy(self,state,idteam,idplayer):
        mystate = toolboxmodif1.MyState(state,idteam,idplayer)
        myaction= toolboxmodif1.MyAction(mystate)
        return myaction.replacement_attaquant4()

class Replacement_defense_Strategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Replacement defensif")
    def compute_strategy(self,state,idteam,idplayer):
        mystate = toolboxmodif1.MyState(state,idteam,idplayer)
        myaction= toolboxmodif1.MyAction(mystate)
        return myaction.replacement_def()
