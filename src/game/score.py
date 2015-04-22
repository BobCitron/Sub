#-*- coding: utf-8 -*-

class Score(object):

    value = {'SA': 
                {
                    '7': 0,
                    '8': 0,
                    '9': 0,
                    'J': 2,
                    'Q': 3,
                    'K': 4,
                    'T': 10,
                    'A': 19,
                    'DER': 10,
                }
            }


    def __init__(self):
        # score[0] is the score of players 0-2
        # score[1] is the score of players 1-3
        self.__score = [0, 0]


    @staticmethod
    def eval_card(card, trump=None):
        """
            Return the value of a card, with trump consideration
            if trump is not None

        """
        if trump is None or card[1] != trump:
            return Score.value["SA"][card[0]]
        else:
            raise NotImplemented


    @staticmethod
    def evaluate(cards, trump=None):
        """
            Evaluate the value of a set of cards

            @param cards    the set of cards to evaluate
            @param trump    the trump to consider (if not None)

        """
        return sum([Score.eval_card(c, trump) for c in cards])


    def update_score(self, team, pts):
        self.__score[team] += pts


    def get_score(self, team):
        return self.__score[team]


    def deal_points(self, deal, trump, last):
        """

            @param deal     two lists of tuples (trick, player), where:
                                - trick is the set of played cards
                                - player is the winning player of the trick
            @param trump    color of trump for this deal
            @param last     team that won the last trick
                            
        """
        # Score of each team from tricks
        pts = [0] * len(deal)
        for team, tricks in enumerate(deal):
            for trick in tricks:
                pts[team] += self.evaluate(trick[0], trump)
        # todo belotte / rebelotte

        # 10-der ?
        if trump != "TA":
            pts[last] += 10
        return pts 


    def around(self, pts):
        """
            Round points to multiple of 10

        """
        return int(round(float(pts) / 10.) * 10)


    def deal_score(self, deal, last, (trump, pts_to_do, coef, taker)):
        """
            @param deal     two lists of tuples (trick, player), where:
                                - trick is the set of played cards
                                - player is the winning player of the trick
            @param contract Tuple of (color of trump, points to do, mult coef, taker ot the contract)
            @param taker    Team (0 or 1) that is supposed to realise the contract
            @param last     team that won the last trick

        """
        team_taker = taker.team()
        #todo belotte/rebelotte
        pts = [0] * 2
        # Special case : the taker team did win all tricks
        if len(deal[1 - team_taker]) == 0:
            pts[team_taker] = 250
            pts[1 - team_taker] = 0
        else:
            pts = self.deal_points(deal, trump, last)
        score_inc = [0, 0]
        if pts[team_taker] >= pts_to_do:
            # Contract is done
            score_inc[team_taker] = coef * pts_to_do + self.around(pts[team_taker])
            # If the contract was not "coinché"
            if coef == 1:
                # Then the defensive team scores its points
                score_inc[1 - team_taker] = self.around(pts[1 - team_taker])
        else:
            # Contract is not done
            score_inc[1 - team_taker] = coef * pts_to_do + 160
        for team in xrange(len(self.__score)):
            self.update_score(team, score_inc[team])
        #todo notify event manager
