from player import Player

state = {"type": "bet", "on_turn": 2,
         "message": "So Deal With It  made a bet of 401 (raise) and is left with 589 chips. The pot now contains 821 chips.",
         "game_state": {"tournament_id": "55e6f2bb0708790003000002", "game_id": "55fd4e431474db00030000ca", "round": 2,
                        "players": [{"name": "booLean", "stack": 990, "status": "folded", "bet": 0,
                                     "hole_cards": [{"rank": "6", "suit": "hearts"}, {"rank": "9", "suit": "diamonds"}],
                                     "version": "Default PHP folding player", "id": 0},
                                    {"name": "LeanMasters", "stack": 970, "status": "folded", "bet": 0,
                                     "hole_cards": [{"rank": "8", "suit": "hearts"}, {"rank": "5", "suit": "hearts"}],
                                     "version": "Enjoy", "id": 1},
                                    {"name": "So Deal With It ", "stack": 589, "status": "active", "bet": 601,
                                     "hole_cards": [{"rank": "10", "suit": "clubs"}, {"rank": "9", "suit": "spades"}],
                                     "version": "1.0.1", "id": 2},
                                    {"name": "AsdfLEAN", "stack": 1030, "status": "folded", "bet": 20,
                                     "hole_cards": [{"rank": "2", "suit": "diamonds"},
                                                    {"rank": "7", "suit": "diamonds"}], "version": "AsdfLEAN 1.8",
                                     "id": 3}, {"name": "PokerMinds", "stack": 600, "status": "active", "bet": 200,
                                                "hole_cards": [{"rank": "7", "suit": "hearts"},
                                                               {"rank": "K", "suit": "diamonds"}],
                                                "version": "Default Java folding player", "id": 4}], "small_blind": 10,
                        "orbits": 0, "dealer": 1,
                        "community_cards": [{"rank": "6", "suit": "clubs"}, {"rank": "9", "suit": "spades"},
                                            {"rank": "A", "suit": "clubs"}], "current_buy_in": 601, "pot": 821}}
flop_state = {
  "type": "bet",
  "on_turn": 2,
  "message": "So Deal With It  made a bet of 0 (fold) and is left with 250 chips. The pot now contains 4730 chips.",
  "game_state": {
    "tournament_id": "55e6f2bb0708790003000002",
    "game_id": "55fd2f051474db000300001b",
    "round": 48,
    "players": [
      {
        "name": "booLean",
        "stack": 0,
        "status": "active",
        "bet": 4570,
        "hole_cards": [
          {
            "rank": "K",
            "suit": "hearts"
          },
          {
            "rank": "6",
            "suit": "clubs"
          }
        ],
        "version": "Default PHP folding player",
        "id": 0
      },
      {
        "name": "LeanMasters",
        "stack": 0,
        "status": "out",
        "bet": 0,
        "hole_cards": [],
        "version": "Default C# folding player",
        "id": 1
      },
      {
        "name": "So Deal With It ",
        "stack": 250,
        "status": "active",
        "bet": 160,
        "hole_cards": [
          {
            "rank": "J",
            "suit": "spades"
          },
          {
            "rank": "Q",
            "suit": "diamonds"
          }
        ],
        "version": "Smart hands only",
        "id": 2
      },
      {
        "name": "AsdfLEAN",
        "stack": 0,
        "status": "out",
        "bet": 0,
        "hole_cards": [],
        "version": "AsdfLEAN 1.0",
        "id": 3
      },
      {
        "name": "PokerMinds",
        "stack": 20,
        "status": "folded",
        "bet": 0,
        "hole_cards": [
          {
            "rank": "K",
            "suit": "clubs"
          },
          {
            "rank": "K",
            "suit": "diamonds"
          }
        ],
        "version": "Default Java folding player",
        "id": 4
      }
    ],
    "small_blind": 80,
    "orbits": 9,
    "dealer": 4,
    "community_cards": [],
    "current_buy_in": 4570,
    "pot": 4730
  }
}

if __name__ == '__main__':
    p = Player()
    print('bet ' + str(p.betRequest(flop_state['game_state'])))
    print('bet ' + str(p.betRequest(state['game_state'])))
