# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 19:21:53 2017

@author: 3520543
"""

from soccersimulator import SoccerTeam
from OrNoir import Attaque2Strategie,DefenseStrategie

team1 = SoccerTeam(name="team1",login="etu1")
team2 = SoccerTeam(name="team2",login="etu2")
team1.add("Cavani",Attaque2Strategie()) #Strategie qui ne fait rien
team2.add("Paul",DefenseStrategie())
team2.add("Cavani",Attaque2Strategie()) 
