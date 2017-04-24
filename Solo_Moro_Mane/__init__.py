# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 11:55:44 2017

@author: 3520543
"""
from soccersimulator import GolfState,Golf,Parcours1,Parcours2,Parcours3,Parcours4
from soccersimulator import SoccerTeam,show_simu
from soccersimulator import Strategy,SoccerAction,Vector2D,settings
from golf import Golfeur1,Golfeur2

from soccersimulator import SoccerTeam


def get_golf_team():
    team1 = SoccerTeam()
    team1.add("John",Golfeur1())
    return team1
def get_slalom_team1():
    team1 = SoccerTeam()
    team1.add("John",Golfeur2())
    return team1
