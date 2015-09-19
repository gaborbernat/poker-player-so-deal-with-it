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
    VERSION = "1.0.1"
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
                if check_amount >= all_in_amount:
                    return 0
                return check_amount
        else:
            if hand_win_perc < 12:
                if check_amount >= all_in_amount:
                    return 0
                return all_in_amount
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
        return self.get_our_player(game_state).get("stack", 0)

    def action_check(self, game_state):
        # current buy in - our chips = check (or fold is there is another raise)
        return r(game_state, ['current_buy_in'], 0)

    def action_raise(self, game_state, amount=0):
        # current buy in + minimal raise + raise you want to do
        current_buy_in = r(game_state, ['current_buy_in'], 0)
        us = self.get_our_player(game_state)
        already_bet = us.get("bet", 0)
        minimum_raise = r(game_state, ['minimum_raise'], 0)
        our_stack = us.get("stack")
        result = max(minimum_raise, min(our_stack, current_buy_in + already_bet + amount))
        return result

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
    print(p.hand_win_percentage([dict(rank='A'), dict(rank='4')]))
