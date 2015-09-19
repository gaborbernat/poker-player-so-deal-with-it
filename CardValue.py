
class CardValue:

    rankValue = {
        "2" : 2,
        "3" : 3,
        "4" : 4,
        "5" : 5,
        "6" : 6,
        "7" : 7,
        "8" : 8,
        "9" : 9,
        "J" : 10,
        "Q" : 11,
        "K" : 12,
        "A" : 13,
    }


    order = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def getSingleCardValue(self, card):
        try:
            return self.rankValue[card.rank]
        except KeyError:
            return 0

    def get_hand_value(self, hand):
        pass

    def find_hand_name(self, cards):
        """

        input format:

        [...
        {
            "rank": "4",
            "suit": "spades"
        },
        ...
        ]

        Array of tuples, each tuple looks like ('rank', 'suit')
        2-10, J, Q, K, A
        hearts, spades, clubs, diamonds

        :param cards: Cards array
        :return: Returns card strenghs in INT
        """
        cards = sorted(cards, key=lambda x: self.order.index(x[0]))
        #cards = sorted(cards, key=lambda x: x[1])
        print(cards)


        # is straight flush
        # poker
        # full house
        # flush
        # staight
        # drill
        # 2p
        # p
        # high
        # nothing

        return sum([self.order.index(x[0]) for x in cards])

if __name__ == '__main__':
    #class Card:
    #    def __init__(self, rank):
    #        self.rank = rank


    #assert 2 == CardValue().getSingleCardValue(Card("2"))
    #assert 12 == CardValue().getSingleCardValue(Card("K"))
    #assert 0 == CardValue().getSingleCardValue(Card("invalid"))

    print(CardValue().find_hand_name([('6', 'spades'), ('4', 'diamonds'), ('5', 'spades'), ('K', 'hearts'), ('J', 'spades')]))
