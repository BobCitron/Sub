#-*- coding: utf-8 -*-

from src.utils.notify import Notify
from src.game.hand import Hand 
from src.game.coinche import COINCHE_CODE
from src.event.event_engine import EVT_UI_COINCHE 

class UIPlayerMind(Notify):


    def __init__(self, pid, ui):
        Notify.__init__(self)
        self._ui = ui
        self.event = dict()
        self.id = pid


    def get_card(self, played, playable):
        # Get the card
        card = self._ui.get_card(self.id, playable)
        # Return the card
        return card


    def get_coinche(self):
        return self._ui.get_coinche()


    def get_bid(self, bidded, biddable):
        return self._ui.get_bid(self.id, bidded, biddable)


    def bidded(self, bid):
        pass


    def played(self, pid, card):
        pass


    def is_removable(self):
        return false 


    def set_method(self, evt, method):
        """
            Overwriting set_method 

        """
        self._event[evt] = method
        if evt == COINCHE_CODE:
            self.coinche = method
            self._ui._table._bidding.set_method(EVT_UI_COINCHE, self.coinche) 

