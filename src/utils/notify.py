# -*- coding:utf-8 -*-
from abc import ABCMeta

class Notify(object):
    """
        Abstract class that provides tools to notify others obejcts
    """

    __metaclass__ = ABCMeta


    def __init__(self, evts = None):
        if evts is not None:
            self._event = evts
        else:
            # Event notification methods
            self._event = dict()


    def set_method(self, evt_id, method):
        """
            Set a new method to be called on a certain type
            of event
            @param evt_id   id of the event
            @param method   method that must be called on event occurence
        """ 
        # Add the event method
        self._event[evt_id] = method


    def notify(self, evt, *args):
        if evt in self._event.keys():
            self._event[evt](*args)

