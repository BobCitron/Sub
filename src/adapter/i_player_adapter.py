#-*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

class IPlayerAdapter(object):
    """
        Interface that must implement a player adapter
        object to be correctly interfaced with a game

    """

    __metaclass__ = ABCMeta


    def __init__(self):
        pass


    @abstractmethod
    def give_cards(self, cards):
        """
            Add some cards to a hand

        """
        raise NotImplemented


    @abstractmethod
    def get_card(self, played, playable):
        """
            Player must play a card among playable

            @param played   list of cards played so far in this trick
            @param playable list of player's cards that he can play

        """
        raise NotImplemented

    
    @abstractmethod
    def get_coinche(self):
        """
            Player must return a coinche code to signal a coinche to the engine

        """
        raise NotImplemented


    @abstractmethod
    def get_bid(self, bidded, biddable):
        """
            Player must announce a bid (possibly "Pass") among biddable

            @param bidded   list of biddings announced in the current round
                            (bidded[i] is the last bidding from player i)
            @param biddable list of possible biddings

        """
        raise NotImplemented

    
    @abstractmethod
    def played(self, pid, card):
        """
            Notification to the user that a card has been played

            @param pid      id of the player who played
            @param card     card played by player pid

        """
        raise NotImplemented

    
    @abstractmethod
    def bidded(self, bid):
        """
            Notification to the user that a bidding has been announced

            @param bid      Bidding announced (note that bid.taker returns the 
                            id of player who announced)

        """
        raise NotImplemented

    
    @abstractmethod
    def is_removable(self):
        """
            Return True iif the player can be replaced by another player
            (e.g. a bot filling empty places while no human player is here)

        """
        raise NotImplemented


    @abstractmethod
    def reset_hand(self):
        """
            The hand of the player is reset, because the deal has not been played

        """
        raise NotImplemented

