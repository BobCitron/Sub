# -*- coding:utf-8 -*-
# Define global constants to identify events
EVT_NEW_ROUND = 0
EVT_NEW_HAND = 1
EVT_UI_GET_CARD = 2
EVT_CARD_PLAYED = 3
EVT_UI_PLAYER_LEFT = 4
EVT_END_OF_TRICK = 5

class EventEngine(object):


    def __init__(self, game):
        self.game = game
        # Define the function of the event manager that the 
        # game engine should call at each new round
        self.game.set_method(EVT_NEW_ROUND, self.new_round)
        self.game.set_method(EVT_NEW_HAND, self.new_hand)
        self.game.set_method(EVT_CARD_PLAYED, self.card_played)
        self.game.set_method(EVT_END_OF_TRICK, self.end_of_trick)
        self.ui = list()


    def add_ui(self, ui, p = None):
        """
            Add a user interface to the list of interfaces
            to whom events must be notified
            p is a list of players that play through this interface

        """
        if ui not in [ui[0] for ui in self.ui]:
            self.ui.append((ui, p))
            # Players handled by the ui
            for player in p:
                ui.add_player(player)
            # Define the reference player
            if not p is None:
                ui.set_reference_player(p[0])
            # Set the event methods
            ui.set_method(EVT_UI_PLAYER_LEFT, self.player_left)
        for player in p:
            self.game.players[player].set_method(EVT_UI_GET_CARD, ui.get_card)


    def new_round(self):
        """
            Notify all interfaces that a new round has begun

        """
        for ui in self.ui:
            ui[0].new_round()


    def end_of_trick(self, p):
        """
            Notify all interfaces that the current trick is over
            @param p    player that wins the trick

        """
        for ui in self.ui:
            ui[0].end_of_trick(p)


    def new_hand(self, p, h):
        """
            Notify interfaces that a new hand has beend given to player p
            @param p player concerned by the hand
            @param h new hand for player p

        """
        for ui in self.ui:
            if p in ui[1]:
                ui[0].new_hand(p, h)


    def card_played(self, p, c):
        for ui in self.ui:
            ui[0].card_played(p, c)


    def player_left(self, p):
        """
            Notify game that a player has left the game
            @param p    played who left

        """
        pass

