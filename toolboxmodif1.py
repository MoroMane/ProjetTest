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
    
    def ball_vitesse(self):
        return self.state.ball.vitesse

#====================================================================================================================================
#        Position
    def my_position(self):
        return self.state.player_state(self.key[0], self.key[1]).position

    def ball_position(self):
        return self.state.ball.position
        
    # début des modifications
    def ball_positionX(self):
        return self.state.ball.position.x
        
    def ball_positionY(self):
        return self.state.ball.position.y
        
    def position_but_adv(self):
        if self.domicile():
            return Vector2D(settings.GAME_WIDTH,settings.GAME_HEIGHT/2.)
        else :
            return Vector2D(0,settings.GAME_HEIGHT/2.)
    def position_mon_but(self):
        if self.domicile():
            return Vector2D(0,settings.GAME_HEIGHT/2.)
        else :
            return Vector2D(settings.GAME_WIDTH,settings.GAME_HEIGHT/2.)
        
    
    
    def ball_position_future(self):
        if self.ball_vitesse().norm > 2 or self.ball_vitesse().norm < -2:
            return self.ball_position()+self.ball_vitesse()*10
        else :
            return self.ball_position()

    def position_coop_2v2(self):
        nb_coop=len([idp for (idt, idp) in self.state.players if idt == self.idteam])
        return self.state.player_state(self.key[0],(1+self.key[1])%(nb_coop)).position
        
    def vector_placement_gardien(self):
        return Vector2D(self.get_dir_jeu().x*10,0)+self.position_mon_but()
    
    def distance_balle (self): 
        return (self.my_position()-self.ball_position()).norm()
    
    def distance_balle_adv_proche(self):
#        return (self.position_adv_proche(1)-self.ball_position()).norm()
        idproche=self.idplayer
        for (idt, idp) in self.state.players:
            if idt!=self.idteam :
                if (self.state.player_state(idt,idp).position-self.ball_position()).norm < (self.state.player_state(idt,idproche).position-self.ball_position()).norm:
                    idproche=idp
        return (self.state.player_state(idt,idproche).position-self.ball_position()).norm
        
    def adv_plus_proche_ball(self):
        return (self.distance_balle() > self.distance_balle_adv_proche())
        
    def get_dir_jeu(self):
        return  (self.position_but_adv()-self.position_mon_but()).normalize()
        

#===================================================================================================================================
#        Test : True/False
    def domicile(self):
        return self.key[0] == 1

    def peut_frapper(self):
        return (self.ball_position()-self.my_position()).norm <= settings.PLAYER_RADIUS + settings.BALL_RADIUS        
            
    def carre_central(self):
        return ((self.ball_positionX()>74 and self.ball_positionX()<76) and (self.ball_positionY()<46 and self.ball_positionY()>44))

    def def_position_action(self):

        return abs((self.ball_position()-self.position_mon_but()).x) < (Vector2D(self.get_dir_jeu().x*75,0)+self.position_mon_but()).x

    
    def attaquant4_position_dribble(self):
        return abs((self.ball_position()-self.position_mon_but()).x)>=75
        
    def frappe_position(self):
        return abs((self.ball_position()-self.position_but_adv()).x)<=45
            
    def milieu_position_action(self):
        return (abs((self.ball_position()-self.position_mon_but()).x)<80) and (abs((self.ball_position()-self.position_mon_but()).x)>25) 

    def balle_dans_encadrement_but(self):
        return (self.ball_positionY()>40 and self.ball_positionY()<50) 

    def zone_action_gardien(self):
        return abs((self.ball_position()-self.position_mon_but()).x)<=40
#==================================================================================================================================
class MyAction(object):
    def __init__(self,state):
        self.state = state
    
    def aller(self,p):
        return SoccerAction((p-self.state.my_position()),Vector2D())
    
    def aller_vers_balle(self):
        return self.aller(self.state.ball_position()+self.state.ball_vitesse()*5)
    
    def shoot(self,p):
        return SoccerAction(Vector2D(),0.1*(p-self.state.my_position()))
    
    def shoot_but(self):
        return self.shoot(self.state.position_but_adv())

    def pousse_ball(self):
        return SoccerAction(Vector2D(),(self.state.position_but_adv() - self.state.ball_position_future())*0.03) # 0.02 constante pour le dribble

    def pousse_ball_centre(self):
        if self.state.domicile():
            return SoccerAction(Vector2D(),(Vector2D(1,2)))
        else :
            return SoccerAction(Vector2D(),(Vector2D(-1,-2)))
    
    def degagement(self):
        return self.shoot_but()

    def passe_2v2(self):
        return self.shoot(self.state.position_coop_2v2())

#====================================================================================================================================
#            Replacement 

    def replacement_gardien_devant_but(self):
        return  self.aller(self.state.vector_placement_gardien())
        
    def placement_gardien_entre_poteaux(self):
        return self.aller(Vector2D(self.state.vector_placement_gardien().x,self.state.ball_position().y))

    def replacement_def(self):
        return  self.aller(Vector2D(self.state.get_dir_jeu().x*30+self.state.position_mon_but().x,self.state.ball_position().y))
        
    def replacement_milieu(self):
        return self.aller(Vector2D(self.state.get_dir_jeu().x*45+self.state.position_mon_but().x,45))

    def replacement_attaquant4(self):
        return self.aller(Vector2D(self.state.get_dir_jeu().x*80+self.state.position_mon_but().x,45))
#====================================================================================================================================
#                 Action Joueur    
 
    def action_attaquant(self):
        if not (self.state.peut_frapper()):
            return self.aller_vers_balle()
        else :
            if self.state.carre_central():
                return self.pousse_ball_centre()   
            elif not (self.state.frappe_position()):
                return self.pousse_ball()
            else :
                return self.shoot_but()
                              
    def action_def(self):
        if self.state.def_position_action():
            if not self.state.peut_frapper():
                return self.aller_vers_balle()
            else:
                return self.passe_2v2()
        else :
            return self.replacement_def()

    def action_milieu(self):
         if self.state.milieu_position_action():
            if not self.state.peut_frapper():
                return self.aller_vers_balle()
            else:
                return self.passe_2v2()
         else :
            return self.replacement_milieu()

    def action_attaquant4(self):
        if self.state.attaquant4_position_dribble():
            if not self.state.peut_frapper():
                return self.aller_vers_balle()
            elif not (self.state.frappe_position()):
                return self.pousse_ball()
            else :
                return self.shoot_but()
        else :
            return self.replacement_attaquant4()
    
    def action_gardien(self):
        if self.state.zone_action_gardien():
            if not self.state.peut_frapper():
                return self.aller_vers_balle()
            else :
                return self.shoot_but()
        elif self.state.balle_dans_encadrement_but():
            return self.placement_gardien_entre_poteaux()
        else :
            return self.replacement_gardien_devant_but()
                
