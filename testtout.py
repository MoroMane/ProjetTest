# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 18:52:56 2017

@author: 3520543
"""

import toolbox

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
    def __init__(self,name="ma strategie"):
        Strategy.__init__(self,name)
    def compute_strategy(self,state,idteam,idplayer):
        #faire qqe chose d intelligent
    
        mystate = toolbox.MyState(state,idteam,idplayer)
        
        vb=mystate.ball_position()
        vp=mystate.my_position()
        vb2=Vector2D(settings.GAME_WIDTH,settings.GAME_HEIGHT/2.)
        vb1=Vector2D(0,settings.GAME_HEIGHT/2.)
        if idteam%2==0:
            if state.ball.position.x>settings.GAME_WIDTH-110:
                return SoccerAction(vb - vp,Vector2D(-1,0))
            else :
                return SoccerAction(vb-vp,vb1-vp)
        else :
            if state.ball.position.x<settings.GAME_WIDTH-40:
                return SoccerAction(vb - vp,Vector2D(1,0))
            else :
                return SoccerAction(vb-vp,0.1*(vb2-vp))
        #return SoccerAction(vecteur_vitesse,vecteur_shoot)


team1 = SoccerTeam(name="team1",login="etu1")
team2 = SoccerTeam(name="team2",login="etu2")
team1.add("Cavani",Attaque2Strategie()) #Strategie qui ne fait rien
team2.add("Paul",RandomStrategy())   #Strategie aleatoire

#Creation d'une partie
simu = Simulation(team1,team2)
#Jouer et afficher la partie
show_simu(simu)