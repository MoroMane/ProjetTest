# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 19:21:53 2017

@author: 3520543
"""

from soccersimulator import SoccerTeam
from OrNoir import Attaque2Strategie,DefenseStrategie,GardienStrategie,MilieuStrategie,Attaque4Strategie

def get_team(i):
    if i==1:
        team1 = SoccerTeam(name="Toho",login="etu1")
        team1.add("Landers",Attaque2Strategie())
        return team1
    elif i==2:
        team2 = SoccerTeam(name="Réserve",login="etu2")
        team2.add("Micro-Ice",DefenseStrategie())
        team2.add("D-Joke",Attaque4Strategie())
        return team2
    else : 
        team4 = SoccerTeam(name="Snow Kids",login="etu4")
        team4.add("Ahito",GardienStrategie())        
        team4.add("Thran",DefenseStrategie())
        team4.add("Rocket",MilieuStrategie())        
        team4.add("D'Jok",Attaque4Strategie())
        return team4

 #Strategie qui ne fait rien
