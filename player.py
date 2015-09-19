class Player:
    VERSION = "Smart hands only"
    order = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    team_name = "So Deal With It"
    good_cards = [['A', 'A'], ['K', 'K'], ['Q', 'Q'], ['A', 'K'], ['J', 'J'], ['A', 'Q'], ['K', 'Q'], ['A', 'J'],
                  ['K', 'J'], ['10', '10'], ['A', 'K'], ['A', '10'], ['Q', 'J'], ['K', '10'], ['Q', '10'], ['J', '10'],
                  ['9', '9'], ['A', 'Q'], ['A', '9'], ['K', 'Q'], ['8', '8'], ['K', '9'], ['10', '9'], ['A', '8'],
                  ['Q', '9'], ['J', '9'], ['A', 'J'], ['A', '5'], ['7', '7'], ['A', '7'], ['K', 'J'], ['A', '4'],
                  ['A', '3'], ['A', '6'], ['Q', 'J'], ['6', '6'], ['K', '8'], ['10', '8'], ['A', '2'], ['9', '8'],
                  ['J', '8'], ['A', '10'], ['Q', '8'], ['K', '7'], ['K', '10'], ['5', '5'], ['J', '10'], ['8', '7'],
                  ['Q', '10'], ['4', '4'], ['2', '2'], ['3', '3'], ['K', '6'], ['9', '7'], ['K', '5'], ['7', '6'],
                  ['10', '7'], ['K', '4'], ['K', '2'], ['K', '3'], ['Q', '7'], ['8', '6'], ['6', '5'], ['J', '7'],
                  ['5', '4'], ['Q', '6'], ['7', '5'], ['9', '6'], ['Q', '5'], ['6', '4'], ['Q', '4'], ['Q', '3'],
                  ['10', '9'], ['10', '6'], ['Q', '2'], ['A', '9'], ['5', '3'], ['8', '5'], ['J', '6'], ['J', '9']]

    def betRequest(self, game_state):
        us = self.get_our_player(game_state)
        hand = self.get_cards(us)
        return 0 if self.should_we_fold(hand) else 1000000

    def showdown(self, game_state):
        pass

    def should_we_fold(self, hand):
        our_hand = self.order_cards([hand[0]['rank'], hand[1]['rank']])
        return our_hand not in self.good_cards

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
    print(p.should_we_fold([dict(rank='A'), dict(rank='A')]), p.should_we_fold([dict(rank='2'), dict(rank='8')]))
