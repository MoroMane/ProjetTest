# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 19:21:53 2017

@author: 3520543
"""

from soccersimulator import SoccerTeam
from OrNoir import Attaque2Strategie,DefenseStrategie

def get_team(i):
    if i==1:
        team1 = SoccerTeam(name="Toho",login="etu1")
        team1.add("Landers",Attaque2Strategie())
    elif i==2:
        team2 = SoccerTeam(name="team2",login="etu2")
        team2.add("Micro-Ice",DefenseStrategie())
        team2.add("D-Joke",Attaque2Strategie())
    else : 
        team4 = SoccerTeam(name="Snow Kids",login="etu4")
        team4.add("Thran",DefenseStrategie())
        team4.add("D'Jok",Attaque2Strategie())
        team4.add("Micro-Ice",DefenseStrategie())
        team4.add("Ahito",GardienStrategie())


 #Strategie qui ne fait rien
