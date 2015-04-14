from random import randint
from Tkinter import *

# return an instance of the cards image
def get_cards_image():
    cards_image = PhotoImage(file='../../data/classic_playing_cards.gif')       
    return cards_image

# constant card width
def get_card_width():
    return 71

# constant card height
def get_card_height():
    return 96

def index_to_coordinates(x_index, y_index):
    # number of pixel between cards
    x_white_space = 2; 
    y_white_space = 2;
    # compute position taking into account the white space between cards
    x = get_card_width() * x_index + x_white_space * (x_index + 1)
    y = get_card_height() * y_index + y_white_space * (y_index + 1)
    # return a 4-uplet in 
    return x, y, x + get_card_width(), y + get_card_height()

# return the coordinates of a random card
# the coordinates are in a 4-uplet in the following form (n, e, s, w)
def get_random_card_coord():
    # get a random card ...
    x_index = randint(0, 12);
    y_index = randint(0, 3);
    # ... and translate it into coordinates
    return index_to_coordinates(x_index, y_index)

class Cards_image:
    instance = 0
    
    @staticmethod
    def init_cards_image():
        Cards_image.instance = get_cards_image();

    @staticmethod    
    def get_cards_image_instance():
        if Cards_image.instance == 0:
            Cards_image.init_cards_image()
        return Cards_image.instance



