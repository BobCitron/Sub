from Tkinter import Frame, Button
from src.ui.utils import subimage 
from src.ui.cards_image import UICards

class UIHand:
    # number of cards in the hand
    # must be 8 for the Coinche
    max_cards = 8

    # define the first card column
    def return_first_card_column(self):
        column = [2, 2 + self.max_cards, 2, 0]
        # return the position
        return column[self.position]
    
    # define the first card row
    def return_first_card_row(self):
        row = [0, 1, 1 + self.max_cards, 1]
        # return the position
        return row[self.position]

    def _remove_last_button(self):
        self.buttons[len(self.buttons) - 1].destroy()
        self.buttons.pop()

    # index correspond to the clicked card (from 0 to 7)
    def play_card(self, index):
        self._remove_last_button()

    # initialize the button for the cards
    def init_cards_button(self):
        # defines if the hand must be displayed vertically
        # or horizonthally 
        vertical = [0, 1, 0, 1]
        for i in xrange(0, self.max_cards):
            # define the button
            self.buttons[i] = Button(self.frame, image=self.cards_image[i], 
                                     command=lambda : self.play_card(i))
            # which row
            row = self.return_first_card_row() 

            # which column
            column = self.return_first_card_column() 
            # display vertically or horizontally ?
            if vertical[self.position]:
                row += i / 2 * vertical[self.position]            
                if i % 2:
                    # side by side with the previous
                    column += 1
            else:
                # horizontally
                column += i
            # place the button
            self.buttons[i].grid(row = row, column = column)

    # refresh images for the buttons
    def updateCardsImage(self):
        for i in xrange(0, len(self.hand)):
            new_card = UICards.get_card(self.hand[i])
            self.buttons[i].configure(image = new_card)
            self.cards_image[i] = new_card
            
    @property
    def hand(self):
        return self._hand

    @hand.setter
    def hand(self, value):
        self._hand = value
        self.updateCardsImage()
            
    # constructor
    def __init__(self, frame, position):
        self.frame = frame
        self.position = position
        # list of cards in the hand
        self._hand = [None]*self.max_cards
        # list for recording the images itself
        self.cards_image = [None]*self.max_cards
        # place corresponding buttons
        self.buttons = [None]*self.max_cards

        # add random card
        for i in xrange(0, UIHand.max_cards):
            self.cards_image[i] = UICards.get_random_card()

        # init button
        self.init_cards_button()

class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.hands = [UIHand(frame, 0),
                      UIHand(frame, 1),
                      UIHand(frame, 2),
                      UIHand(frame, 3)]

        self.quit = Button(frame, text = "Quit",
                                     command=frame.quit)
        
        self.quit.grid(row = 7, column = 13)

        
