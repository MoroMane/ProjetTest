# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 18:52:56 2017

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
#Stratégie Fonceur
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
        return SoccerAction(vb-v1,v2-vb)    
        #return SoccerAction(vitesse,shoot)

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
    
        mystate = toolboxmodif1.MyState(state,idteam,idplayer)
        myaction= toolboxmodif1.MyAction(mystate)
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
    def __init__(self,name="defense"):
        Strategy.__init__(self,name)
    def compute_strategy(self,state,idteam,idplayer):
        mystate = toolboxmodif1.MyState(state,idteam,idplayer)
        myaction= toolboxmodif1.MyAction(mystate)
        return myaction.action_def()


class GardienStrategie(Strategy):
    def __init__(self,name="gardien"):
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
        
team1 = SoccerTeam(name="team1",login="etu1")
team2 = SoccerTeam(name="team2",login="etu2")
#
#team1.add("Murasakibara",GardienStrategie())
team1.add("Thran",DefenseStrategie())
team1.add("pastore",MilieuStrategie())
#team1.add("Cavani",Attaque2Strategie())
team1.add("D'Jok",Attaque4Strategie())
#team1.add("Fonceur",Fonceur())
# #Strategie qui ne fait rien
team2.add("Paul",GardienStrategie())
#team2.add("Rocket",DefenseStrategie())
#team2.add("Kagami",MilieuStrategie())   #Strategie aleatoire
#team2.add("Landers",Attaque2Strategie())
#team2.add("Landers",Attaque4Strategie())
#team2.add("Landers",Fonceur())
#team2.add("Landers",RandomStrategy())
#Creation d'une partie
simu = Simulation(team1,team2)
#Jouer et afficher la partie
show_simu(simu)