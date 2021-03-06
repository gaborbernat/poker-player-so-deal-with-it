import copy

class dictlike(object):
    def __getitem__(self, key):
        return self.__getattribute__(key)
    def get(self, key, default = None):
        try:
            return self[key]
        except KeyError:
            return default

class Card(dictlike):
    def __init__(self, rank = "2", suit = "diamonds" ):
        if (len(rank)==1):
            self.rank = rank
            self.suit = suit
        else:
            self.rank, self.suit = self.fromString(rank)

    def fromString(self, s):
        if s.startswith("10"):
            rank = "10"
            suitChar = s[2:]
        else:
            rank = s[0]
            suitChar = s[1]
        suit = self.suitFromChar(suitChar)
        return rank, suit
        
    def suitFromChar(self, s):
        if s == "c":
            return "clubs"
        if s == "s":
            return "spades"
        if s == "d":
            return "diamonds"
        if s == "h":
            return "hearts"
        raise AssertionError("Invalid suit character: " + s)

    @staticmethod
    def buildCards(s):
        return [ Card(x) for x in s.split() ]

class PlayerMock(dictlike):
    playerTemplate = {
        "name": "booLean",
        "stack": 940,
        "status": "folded",
        "bet": 0,
        "version": "Default PHP folding player",
        "id": 0
    }

    def __init__(self, name = "just a player"):
        self.name = name
        self.hole_cards = []
        self.stack = 1000
        self.status = "folded"
        self.bet = 50
        self.version = "Default ... player"
        self.id = 0

    def withCards(self, cards):
        self.hole_cards.extend(cards)
        return self

    def withBet(self, bet):
        self.bet = bet
        return self

    def withStack(self, stack):
        self.stack = stack
        return self

class MyPlayer(PlayerMock):
    def __init__(self):
        PlayerMock.__init__(self, "So Deal With It ")

class StateBuilder:
    stateTemplate = {
        "type": "bet",
        "on_turn": 1,
        "message": "LeanMasters made a bet of 0 (fold) and is left with 580 chips. The pot now contains 2020 chips.",
        "game_state": {
            "tournament_id": "55e6f2bb0708790003000002",
            "game_id": "55fd423b1474db000300009c",
            "round": 7,
            "small_blind": 10,
            "orbits": 1,
            "dealer": 0,
            "players" : [],
            "community_cards": [],
            "current_buy_in": 1990,
            "pot": 2020
        }
    }
    
    def __init__(self):
        self.players = []
        self.cards = []
        self.current_buy_in = 500
        self.pot = 550
    
    def withPlayer(self, player):
        self.players.append(player)
        return self

    def withCommunityCards(self, cards):
        self.cards.extend(cards)
        return self
        
    def withBuyIn(self, buyin):
        self.current_buy_in = buyin
        return self

    def withPot(self, pot):
        self.pot = pot
        return self

    def build(self):
        state = copy.deepcopy(self.stateTemplate)
        state["players"] = self.players
        state["community_cards"] = self.cards
        return state


