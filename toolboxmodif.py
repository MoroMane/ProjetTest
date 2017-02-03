# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 18:31:09 2017

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

class MyState(object):
    def __init__(self,state,idteam,idplayer):
        self.state = state
        self.idteam=idteam
        self.idplayer= idplayer
        self.key = (idteam,idplayer)
    def my_position(self):
        return self.state.player_state(self.key[0], self.key[1]).position
        #equivalent a self.player_state(self.key[0],self.key[1])
    def ball_position(self):
        return self.state.ball.position
   
 
        
    # début des modifications
    def ball_positionX(self):
        return self.state.ball.position.x
        
    def ball_positionY(self):
        return self.state.ball.position.y
        
    def position_but_adv(self):
        if self.idteam == 1:
            return Vector2D(settings.GAME_WIDTH,settings.GAME_HEIGHT/2.)
        else :
            return Vector2D(0,settings.GAME_HEIGHT/2.)
        
  
        
#    def position_coop_proche_team1(self):
#        pos=self.position_but_adv()
#        for (it,ip) in self.state.players:
#            if it == 1:
#        #[ (it, ip) for (it, ip) in state.players if it ==1]
#                if self.state.players[it,ip].position().norm() <pos.norm():
#                    pos=(it,ip).my_position()
#        return pos
#
#    def position_coop_proche_team2(self):
#        pos=self.position_but_adv()
#        for (it,ip) in self.state.players:
#            if it == 2:
#        #[ (it, ip) for (it, ip) in state.players if it ==1]
#                if ((it,ip).my_position()-ball).norm() <pos.norm():
#                    pos=(it,ip).my_position()
#        return pos
#            #return self.key[1].my_position()
#    
#    


class MyAction(object):
    def __init__(self,state):
        self.state = state
#    def __getattr__(self, name):
#        return getattr(self.state, name)
    
    def aller(self,p):
        return SoccerAction(p-self.state.my_position(),Vector2D())
    def aller_vers_balle(self):
        return self.aller(self.state.ball_position())
    def shoot(self,p):
        return SoccerAction(Vector2D(0,0),0.1*(p-self.state.my_position()))
    def shoot_but(self):
        return self.aller_vers_balle() + self.shoot(self.state.position_but_adv())
    def dribble_team1(self):
        return self.aller_vers_balle()+SoccerAction(Vector2D(),Vector2D(1,0.2))
    def dribble_team2(self):
             return self.aller_vers_balle()+SoccerAction(Vector2D(),Vector2D(-1,-0.2))
    def action_attaquant(self):
        if self.state.idteam==1:
            if self.state.ball_positionX()<settings.GAME_WIDTH-40:
                return self.dribble_team1()
            else : 
                return self.shoot_but()
        else :
            if self.state.ball_positionX()>settings.GAME_WIDTH-110:
                return self.dribble_team2()
            else :
                return self.shoot_but()
                
    
    def degagement(self): #p=position du dégagement
        return self.aller_vers_balle()+self.shoot_but()
        
    def action_def(self):
        if self.state.idteam==1:
            if self.state.ball_positionX()<75:
                return self.degagement()
        else :
            if self.state.ball_positionX()>75:
                return self.degagement()