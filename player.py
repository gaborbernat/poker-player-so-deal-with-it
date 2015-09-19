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
    VERSION = "Smart hands only with a twist"
    order = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    team_name = "So Deal With It "

    def betRequest(self, game_state):
        us = self.get_our_player(game_state)
        hand = self.get_cards(us)
        hand_win_perc = self.hand_win_percentage(hand)

        raise_amount = self.action_raise(game_state, amount=1)
        all_in_amount = self.action_all_in(game_state)
        check_amount = self.action_check(game_state)

        if self.is_pref_flop(game_state):
            if hand_win_perc > 14.8:
                return all_in_amount
            if hand_win_perc > 12:
                return min(raise_amount, 500)
            else:
                return max(check_amount, 80)
        else:
            if hand_win_perc < 12:
                return check_amount
            else:
                return raise_amount

    def is_pref_flop(self, game_state):
        return len(self.get_community_cards(game_state)) == 0

    def get_community_cards(self, game_state):
        return r(game_state, ['community_cards'], [])

    def showdown(self, game_state):
        pass

    def hand_win_percentage(self, hand):
        our_hand = self.order_cards([hand[0]['rank'], hand[1]['rank']])
        return hands[tuple(our_hand)]

    def order_cards(self, elements):
        return sorted(elements, key=lambda x: -1 * self.order.index(x))

    def action_all_in(self, game_state):
        # current buy in + all the money we still have
        return r(game_state, ['current_buy_in'], 0) + self.get_our_player(game_state).get("stack", 0)

    def action_check(self, game_state):
        # current buy in - our chips = check (or fold is there is another raise)
        return r(game_state, ['current_buy_in'], 0) - self.get_our_player(game_state).get("bet", 0)

    def action_raise(self, game_state, amount=0):
        # current buy in + minimal raise + raise you want to do
        return r(game_state, ['current_buy_in'], 0) - self.get_our_player(game_state).get("bet", 0) + \
               r(game_state, ['minimum_raise'], 0) + amount

    @staticmethod
    def get_cards(player):
        return player['hole_cards']

    def get_our_player(self, game_state):
        for player in game_state['players']:
            if player["name"] == self.team_name:
                return player


if __name__ == '__main__':
    p = Player()
    print(p.hand_win_percentage([dict(rank='A'), dict(rank='A')]))
    print(p.hand_win_percentage([dict(rank='2'), dict(rank='8')]))
