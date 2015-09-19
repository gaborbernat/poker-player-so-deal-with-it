
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

    def getSingleCardValue(self, card):
        try:
            return self.rankValue[card.rank]
        except KeyError:
            return 0

if __name__ == '__main__':
    class Card:
        def __init__(self, rank):
            self.rank = rank

    assert 2 == CardValue().getSingleCardValue(Card("2"))
    assert 12 == CardValue().getSingleCardValue(Card("K"))
    assert 0 == CardValue().getSingleCardValue(Card("invalid"))
