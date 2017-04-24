from soccersimulator import GolfState,Golf,Parcours1,Parcours2,Parcours3,Parcours4
from soccersimulator import SoccerTeam,show_simu
from soccersimulator import Strategy,SoccerAction,Vector2D,settings
import toolboxmodif1

GOLF = 0.001
SLALOM = 10.


class DemoStrategy(Strategy):
    def __init__(self):
        super(DemoStrategy,self).__init__("Demo")
    def compute_strategy(self,state,id_team,id_player):
        """ zones : liste des zones restantes a valider """
        zones = state.get_zones(id_team)
        if len(zones)==0:
            """ shooter au but """
            return SoccerAction(state.ball.position-state.player_state(id_team,id_player).position,\
                    Vector2D((2-id_team)*settings.GAME_WIDTH,settings.GAME_HEIGHT/2.)-state.ball.position)
        """ zone : carre de zone avec z.position angle bas,gauche et z.l longueur du cote
            centre du carre : zone.position+Vector2D(z.l/2.,z.l/2.)
            zone.dedans(point) : teste si le point est dans la zone
        """
        zone = zones[0]
        """ si la ball est dans une zone a valider """
        if zone.dedans(state.ball.position):
            return SoccerAction()
        """ sinon """
        distance = state.player_state(id_team,id_player).position.distance(zone.position+zone.l/2.)
        return SoccerAction()


class Golfeur1(Strategy):
    def __init__(self,name="Golfeur"):
         Strategy.__init__(self,name)
    def compute_strategy(self,state,idteam,idplayer):
        mystate = toolboxmodif1.MyState(state,idteam,idplayer)
        myaction= toolboxmodif1.MyAction(mystate)
        zones=state.get_zones(idteam)
        if not mystate.peut_frapper():
            return myaction.aller_vers_balle()
        elif len(zones)==0:
            return SoccerAction(Vector2D(),0.08*(mystate.position_but_adv()-mystate.my_position()))
        else:
            cpt=0
            for i in range (1,len(zones)):
                if state.player_state(idteam,idplayer).position.distance(zones[cpt].position+zones[cpt].l/2.)>state.player_state(idteam,idplayer).position.distance(zones[i].position+zones[i].l/2.):
                    cpt=i
            zone=zones[cpt]
            if zone.dedans(state.ball.position):
                return myaction.aller_vers_balle()
            return SoccerAction(Vector2D(),0.08*((zone.position+zone.l/2.)-mystate.my_position()))

class Golfeur2(Strategy):
    def __init__(self,name="Golfeur"):
         Strategy.__init__(self,name)
    def compute_strategy(self,state,idteam,idplayer):
        mystate = toolboxmodif1.MyState(state,idteam,idplayer)
        myaction= toolboxmodif1.MyAction(mystate)
        zones=state.get_zones(idteam)
        if not mystate.peut_frapper():
            return myaction.aller_vers_balle()
        elif len(zones)==0:
            return SoccerAction(Vector2D(),0.08*(mystate.position_but_adv()-mystate.my_position()))
        else:
            cpt=0
            for i in range (1,len(zones)):
                if state.player_state(idteam,idplayer).position.distance(zones[cpt].position+zones[cpt].l/2.)>state.player_state(idteam,idplayer).position.distance(zones[i].position+zones[i].l/2.):
                    cpt=i
            zone=zones[cpt]
            if zone.position.x < state.ball.position.x+state.ball.vitesse.x and zone.position.x + zone.l > state.ball.position.x+state.ball.vitesse.x and zone.position.y < state.ball.position.y+state.ball.vitesse.y and zone.position.y + zone.l > state.ball.position.y+state.ball.vitesse.y:         
            #if zone.dedans(state.ball.position+state.ball.vitesse):
                return myaction.aller_vers_balle()
            return SoccerAction(Vector2D(),0.04*((zone.position+zone.l/2.)-mystate.my_position()))


#team1 = SoccerTeam()
#team2 = SoccerTeam()
#team1.add("John",Golfeur2())
#team2.add("John",DemoStrategy())
#simu = Parcours1(team1=team1,vitesse=GOLF)
#show_simu(simu)
#simu = Parcours2(team1=team1,vitesse=GOLF)
#show_simu(simu)
#simu = Parcours3(team1=team1,vitesse=SLALOM)
#show_simu(simu)
#simu = Parcours4(team1=team1,team2=team2,vitesse=SLALOM)
#show_simu(simu)
