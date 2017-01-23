# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 19:05:56 2017

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

## Strategie aleatoire
class RandomStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Random")
    def compute_strategy(self,state,id_team,id_player):
        return SoccerAction(Vector2D.create_random(-1,1),Vector2D.create_random(-1,1))


class AttaqueStrategie(Strategy):
    def __init__(self,name="ma strategie"):
        Strategy.__init__(self,name)
    def compute_strategy(self,state,idteam,idplayer):
        #faire qqe chose d intelligent
        vb=state.ball.position
        vp=(state.player_state(idteam,idplayer).position)
        vb2=Vector2D(settings.GAME_WIDTH,settings.GAME_HEIGHT/2.)
        vb1=Vector2D(0,settings.GAME_HEIGHT/2.)
        if idteam%2==0:
            return SoccerAction(vb-vp,vb2-vp)
        else :
            return SoccerAction(vb-vp,vb2-vp)
        #return SoccerAction(vecteur_vitesse,vecteur_shoot)

class DefenseStrategie(Strategy):
    def __init__(self,name="defnse"):
        Strategy.__init__(self,name)
    def compute_strategy(self,state,idteam,idplayer):
        if state.ball.position.x>75:
            return SoccerAction(state.ball.position - state.player_state(idteam,idplayer).position,Vector2D(-45,-100))
    
    
    
class Attaque2Strategie(Strategy):
    def __init__(self,name="ma strategie"):
        Strategy.__init__(self,name)
    def compute_strategy(self,state,idteam,idplayer):
        #faire qqe chose d intelligent
        vb=state.ball.position
        vp=(state.player_state(idteam,idplayer).position)
        vb2=Vector2D(settings.GAME_WIDTH,settings.GAME_HEIGHT/2.)
        vb1=Vector2D(0,settings.GAME_HEIGHT/2.)
        if idteam%2==0:
            if state.ball.position.x>settings.GAME_WIDTH-110:
                return SoccerAction(state.ball.position - state.player_state(idteam,idplayer).position,Vector2D(-1,0))
            else :
                return SoccerAction(vb-vp,vb1-vp)
        else :
            if state.ball.position.x<settings.GAME_WIDTH-40:
                return SoccerAction(state.ball.position - state.player_state(idteam,idplayer).position,Vector2D(1,0))
            else :
                return SoccerAction(vb-vp,0.1*(vb2-vp))
        #return SoccerAction(vecteur_vitesse,vecteur_shoot)


## Creation d'une equipe
team1 = SoccerTeam(name="team1",login="etu1")
team2 = SoccerTeam(name="team2",login="etu2")
team1.add("Cavani",Attaque2Strategie()) #Strategie qui ne fait rien
team2.add("Paul",DefenseStrategie())   #Strategie aleatoire

#Creation d'une partie
simu = Simulation(team1,team2)
#Jouer et afficher la partie
show_simu(simu)
