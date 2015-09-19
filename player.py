import logging
from hands import hands

def r(w, i, d):
    x = w
    found = False
    for k in i:
        if k in x:
            x = x[k]
            found = True
    return x if found else d


class Player:
    VERSION = "Smart hands only"
    order = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    team_name = "So Deal With It "

    def betRequest(self, game_state):
        us = self.get_our_player(game_state)
        hand = self.get_cards(us)
        what_to_do = self.should_we_fold(hand)
        logging.info('should we fold {} with {}'.format(what_to_do, hand))
        return 0 if what_to_do else 1000000

    def is_pref_flop(self, game_state):
        return len(self.get_community_cards(game_state)) == 0

    def get_community_cards(self, game_state):
        return r(game_state, ['community_cards'], [])

    def showdown(self, game_state):
        pass

    def should_we_fold(self, hand):
        our_hand = self.order_cards([hand[0]['rank'], hand[1]['rank']])
        percentage = hands[tuple(our_hand)]
        return percentage < 14

    def order_cards(self, elements):
        return sorted(elements, key=lambda x: -1 * self.order.index(x))

    @staticmethod
    def get_cards(player):
        return player['hole_cards']

    def get_our_player(self, game_state):
        for player in game_state['players']:
            if player["name"] == self.team_name:
                return player


if __name__ == '__main__':
    p = Player()
    assert not p.should_we_fold([dict(rank='A'), dict(rank='A')])
    assert p.should_we_fold([dict(rank='2'), dict(rank='8')])
