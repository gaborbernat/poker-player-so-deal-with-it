
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

        result = sum([self.order.index(x[0]) for x in cards])

        if self.has_straight_flush(cards):
            return result * 100

        if self.has_poker(cards):
            return result * 80

        if self.has_full_house(cards):
            return result * 60

        if self.has_flush(cards):
            return result * 50

        if self.has_straight(cards):
            return result * 40

        if self.has_drill(cards):
            return result * 30

        if self.has_2p(cards):
            return result * 20

        if self.has_p(cards):
            return result * 10

        if self.has_high(cards):
            return result * 5

        return sum([self.order.index(x[0]) for x in cards])

    def has_straight_flush(self, cards):
        dist = self.get_card_dist(cards, 1)
        suit = None
        for card in dist.iteritems():
            if card[1] >= 5:
                suit = card[0]
        if suit:
            cards = filter(lambda x: x[1] == suit, cards)

            ranks = sorted(map(lambda x: self.order.index(x), map(lambda x: x[0], cards)))
            diff1 = 0
            last = -100
            for rank in ranks:
                diff1 = diff1 + 1 if rank - last == 1 else 0
                if diff1 == 4:
                    return True
                last = rank
        return False

    def has_poker(self, cards):
        dist = self.get_card_dist(cards)
        for rank, num in dist.iteritems():
            if num >= 4:
                print("Found poker")
                return True
        return False

    def has_full_house(self, cards):
        dist = self.get_card_dist(cards)
        found2 = False
        found3 = False
        for num in dist.values():
            if num >= 3:
                found3 = True
            if num == 2:
                found2 = True

        if found2 and found3:
                print("Found full house")
                return True

        return False

    def has_flush(self, cards):
        dist = self.get_card_dist(cards, 1)
        return max(map(lambda x: dist[x], dist)) >= 5

    def has_straight(self, cards):
        ranks = sorted(map(lambda x: self.order.index(x), map(lambda x: x[0], cards)))
        diff1 = 0
        last = -100
        for rank in ranks:
            diff1 = diff1 + 1 if rank - last == 1 else 0
            if diff1 == 4:
                return True
            last = rank
        return False

    def has_drill(self, cards):
        dist = self.get_card_dist(cards)
        for rank, num in dist.iteritems():
            if num >= 3:
                print("Found drill")
                return True
        return False

    def has_2p(self, cards):
        dist = self.get_card_dist(cards)
        found = False
        for rank, num in dist.iteritems():
            if num >= 2 and found is True:
                print("Found 2 pair")
                return True
            elif num >= 2 and not found:
                found = True
        return False

    def has_p(self, cards):
        for i in range(0, len(cards)-1):
            if cards[i][0] == cards[i+1][0]:
                print("Found pair")
                return True
        return False

    def has_high(self, cards):
        for card in cards:
            if card[0] in ['J', 'Q', 'K', 'A']:
                print("Found high card")
                return True
        return False

    def get_card_dist(self, cards, id=0):
        return {card[id]: len([x for x in cards if x[id] == card[id]]) for card in cards}




if __name__ == '__main__':
    #class Card:
    #    def __init__(self, rank):
    #        self.rank = rank


    #assert 2 == CardValue().getSingleCardValue(Card("2"))
    #assert 12 == CardValue().getSingleCardValue(Card("K"))
    #assert 0 == CardValue().getSingleCardValue(Card("invalid"))

    cards = [('6', 'spades'), ('6', 'diamonds'), ('6', 'spades'), ('5', 'hearts'), ('5', 'spades')]
    #
    #assert True == CardValue().straight_flush([('1', 'spades'), ('2', 'hearts')])

    assert False == CardValue().has_poker([('1', 'spades'), ('2', 'hearts')])
    assert False == CardValue().has_poker([('10', 'spades'), ('10', 'hearts'), ('9', 'clubs'), ('8', 'clubs'), ('10', 'diamonds')])
    #assert True == CardValue().has_poker([('10', 'spades'), ('10', 'hearts'), ('10', 'clubs'), ('8', 'clubs'), ('10', 'diamonds')])

    assert False == CardValue().has_full_house([('1', 'spades'), ('2', 'hearts')])
    assert False == CardValue().has_full_house([('2', 'spades'), ('4', 'hearts'), ('4', 'spades'), ('4', 'hearts'), ('4', 'hearts')])
    #assert True == CardValue().has_full_house([('2', 'spades'), ('2', 'hearts'), ('4', 'spades'), ('4', 'hearts'), ('4', 'hearts')])

    assert False == CardValue().has_flush([('1', 'spades'), ('2', 'hearts')])
    assert False == CardValue().has_flush([('5', 'spades'), ('6', 'spades'), ('7', 'spades'), ('8', 'spades'), ('9', 'hearts')])
    #assert True == CardValue().has_flush([('1', 'spades'), ('2', 'spades'), ('3', 'spades'), ('2', 'spades'), ('4', 'spades')])

    assert False == CardValue().has_staight([('1', 'spades'), ('2', 'hearts')])
    assert False == CardValue().has_staight([('1', 'spades'), ('2', 'hearts'), ('3', 'spades'), ('2', 'hearts'), ('4', 'hearts')])
    #assert True == CardValue().has_staight([('3', 'spades'), ('4', 'hearts'), ('5', 'spades'), ('6', 'hearts'), ('7', 'hearts')])

    assert False == CardValue().has_drill([('1', 'spades'), ('2', 'hearts')])
    assert False == CardValue().has_drill([('1', 'spades'), ('2', 'hearts'), ('3', 'spades'), ('2', 'hearts'), ('4', 'hearts')])
    assert True == CardValue().has_drill([('K', 'spades'), ('3', 'hearts'), ('3', 'spades'), ('K', 'hearts'), ('K', 'hearts')])

    assert False == CardValue().has_2p([('1', 'spades'), ('2', 'hearts')])
    assert False == CardValue().has_2p([('1', 'spades'), ('2', 'hearts'), ('3', 'spades'), ('2', 'hearts'), ('4', 'hearts')])
    assert True == CardValue().has_2p([('2', 'spades'), ('2', 'hearts'), ('4', 'spades'), ('4', 'hearts'), ('7', 'hearts')])

    assert False == CardValue().has_p([('1', 'spades'), ('2', 'hearts')])
    assert True == CardValue().has_p([('2', 'spades'), ('2', 'hearts')])

    assert False == CardValue().has_high([('1', 'spades'), ('2', 'hearts')])
    assert True == CardValue().has_high([('K', 'spades'), ('2', 'hearts')])


    print(CardValue().find_hand_name(cards))
    print(CardValue().get_card_dist(cards))
