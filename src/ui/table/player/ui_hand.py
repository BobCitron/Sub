# -*- coding:utf-8 -*-
from Tkinter import Button, CENTER
from threading import Event 

from src.game.game_engine import GameEngine
from src.game.card import Card 

from src.ui.utils.ui_card import UICard
from src.ui.utils.image_loader import ImageLoader  
from src.ui.ui_positioning import UIPositioning

class UIHand(object):
    """
       Interface object for the hand of a player 
       Contains as few logic as possible

    """

    def __init__(self, frame, position):
        # Memorise the frame
        self._frame = frame

        self.position = position

        # List of cards in the hand
        self._hand = []
        # Size of the hand
        self._size = 0 
        # Last card clicked in this hand
        # Must be None if no card were clicked during this round
        self.last_card_played = None 
        # Will be used to notify the main thread when waiting for a card
        self.card_played_event = Event() 

        # Indicates wheter the hand is displayed or not
        self.hidden = True 

        # List for recording the images itself
        self.cards_image = [None] * GameEngine.MAX_CARD
        # Contains the buttons 
        self._buttons = [None] * GameEngine.MAX_CARD
        # Init buttons
        self._init_buttons()
        self._update_buttons_position()


    def _update_first_card_column(self):
        """
            Define the column of the first card for each hand

        """
        # keep the hand centered
        nb_cards_missing = GameEngine.MAX_CARD - len(self._hand)
        missing_offset = nb_cards_missing / 2.0 * ImageLoader.CARD_WIDTH 
        # don't forget covering
        missing_offset *= UIPositioning.COVERING
        # magical formula
        space_taken = UIPositioning.HAND_WIDTH + UIPositioning.HAND_OFFSET
        UIPositioning.first_card_column = [space_taken + missing_offset, 
                                    space_taken * 2 + missing_offset, 
                                    space_taken + missing_offset, 
                                    missing_offset]
        # Add horizontal offset
        UIPositioning.first_card_column = [x + UIPositioning.HAND_OFFSET / 2.0 \
                                            for x in UIPositioning.first_card_column]


    def _update_first_card_row(self):
        """
            Define the row of the first card for each hand

        """
        height = UIPositioning.HAND_HEIGHT
        UIPositioning.first_card_row = [0, height * 2, height * 4, height * 2] 
        # Add vertical offset
        UIPositioning.first_card_row = [x + height / 2.0 for x in UIPositioning.first_card_row]


    def click_card(self, index):
        """
            Callback function for the card selection
            @param index    the clicked card (from 0 to 7)

        """
        # Set the last played card
        self.last_card_played = self.hand[index]
        # Notify the consumer (main thread)
        self.card_played_event.set()
        # Reset the event
        self.card_played_event.clear()


    def _init_buttons(self):
        """
            Init the buttons that will be used to modelise the cards

        """
        for i in xrange(0, GameEngine.MAX_CARD):
            # Define the button
            self._buttons[i] = Button(self._frame, image = self.cards_image[i],
                                      command=lambda i=i: self.click_card(i))

    def _update_button_position(self, i):
        """
            Place one button to its corresponding location
            @param i    index of the button

        """
        # Compute new positions
        self._update_first_card_column()
        self._update_first_card_row()
        # Place the button
        x = UIPositioning.first_card_column[self.position] + i * UIPositioning.CARD_SHIFTING
        y = UIPositioning.first_card_row[self.position]
        self._buttons[i].place(x = x, y = y)


    def _update_buttons_position(self):
        """
            Place the buttons to their corresponding locations

        """
        for i in xrange(0, self._size):
            self._update_button_position(i)


    def _update_button_image(self, buttonNumber, card):
        """
            Change one card image
            @param buttonNumber index of the button
            @param card         card to display

        """
        assert buttonNumber in range(0, GameEngine.MAX_CARD), \
                "Button number is out of range: " + str(buttonNumber)
        # Get the card mage
        if self.hidden:
            new_card = UICard.get_card_image(Card('7', 'S'))
        else:
            new_card = UICard.get_card_image(card)
        # Display it
        self._buttons[buttonNumber].configure(image = new_card)
        # Save it
        self.cards_image[buttonNumber] = new_card
        # Be sure that the button is visible
        self._update_button_position(buttonNumber)
            

    def update_cards_image(self):
        """
            Modify a cards for 
            Refresh images for the buttons

        """
        # Update new cards
        for i in xrange(0, self._size):
            self._update_button_image(i, self.hand[i])
        # Hide the remaining buttons
        for i in xrange(self._size, GameEngine.MAX_CARD):
            self._buttons[i].place_forget();


    @property
    def hand(self):
        """
            The hand property contains the corresponding cards

        """
        return self._hand

    @hand.setter
    def hand(self, value):
        """
            When modified, the button are automatically updated 
            @param value    new hand

        """
        assert len(value) <= GameEngine.MAX_CARD,\
               "Hand is to big: " + str(len(value))
        self._hand = value
        self._size = len(self._hand)
        self.update_cards_image()

    @property
    def size(self):
        """
            Return the number of card in the hand
        
        """
        return self._size

    @size.setter
    def size(self, value):
        """
            When modified, the button are automatically updated
            Used only for not handled players
            @param value    number of cards in the new hand
        """
        self._size = value
        self._hand = [None] * self._size
        self.update_cards_image()