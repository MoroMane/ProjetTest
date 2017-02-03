# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 18:52:56 2017

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

#class DefenseStrategie(Strategy):
#    def __init__(self,name="defnse"):
#        Strategy.__init__(self,name)
#    def compute_strategy(self,state,idteam,idplayer):
#        
#        if state.ball.position.x>75:
#            return SoccerAction(state.ball.position - state.player_state(idteam,idplayer).position,Vector2D(-50,-50))
class DefenseStrategie(Strategy):
    def __init__(self,name="defnse"):
        Strategy.__init__(self,name)
    def compute_strategy(self,state,idteam,idplayer):
        mystate = toolboxmodif.MyState(state,idteam,idplayer)
        myaction= toolboxmodif.MyAction(mystate)
        return myaction.action_def()

team1 = SoccerTeam(name="team1",login="etu1")
team2 = SoccerTeam(name="team2",login="etu2")
team1.add("Cavani",Attaque2Strategie())
#team1.add("Murasakibara",Attaque2Strategie())
 #Strategie qui ne fait rien
team2.add("Paul",Attaque2Strategie())
#team2.add("Kagami",Attaque2Strategie())   #Strategie aleatoire

#Creation d'une partie
simu = Simulation(team1,team2)
#Jouer et afficher la partie
show_simu(simu)