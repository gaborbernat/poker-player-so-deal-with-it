from player import Player

state = {
    "type": "bet",
    "on_turn": 1,
    "message": "LeanMasters made a bet of 0 (fold) and is left with 580 chips. The pot now contains 2020 chips.",
    "game_state": {
        "tournament_id": "55e6f2bb0708790003000002",
        "game_id": "55fd423b1474db000300009c",
        "round": 7,
        "players": [
            {
                "name": "booLean",
                "stack": 940,
                "status": "folded",
                "bet": 0,
                "hole_cards": [
                    {
                        "rank": "2",
                        "suit": "diamonds"
                    },
                    {
                        "rank": "3",
                        "suit": "hearts"
                    }
                ],
                "version": "Default PHP folding player",
                "id": 0
            },
            {
                "name": "LeanMasters",
                "stack": 580,
                "status": "active",
                "bet": 10,
                "hole_cards": [
                    {
                        "rank": "5",
                        "suit": "diamonds"
                    },
                    {
                        "rank": "K",
                        "suit": "clubs"
                    }
                ],
                "version": "Enjoy",
                "id": 1
            },
            {
                "name": "So Deal With It ",
                "stack": 1460,
                "status": "active",
                "bet": 20,
                "hole_cards": [
                    {
                        "rank": "A",
                        "suit": "hearts"
                    },
                    {
                        "rank": "4",
                        "suit": "spades"
                    }
                ],
                "version": "Smart hands only with a twist",
                "id": 2
            },
            {
                "name": "AsdfLEAN",
                "stack": 0,
                "status": "active",
                "bet": 1990,
                "hole_cards": [
                    {
                        "rank": "8",
                        "suit": "hearts"
                    },
                    {
                        "rank": "A",
                        "suit": "diamonds"
                    }
                ],
                "version": "AsdfLEAN 1.8",
                "id": 3
            },
            {
                "name": "PokerMinds",
                "stack": 0,
                "status": "out",
                "bet": 0,
                "hole_cards": [],
                "version": "Default Java folding player",
                "id": 4
            }
        ],
        "small_blind": 10,
        "orbits": 1,
        "dealer": 0,
        "community_cards": [],
        "current_buy_in": 1990,
        "pot": 2020
    }
}
if __name__ == '__main__':
    p = Player()
    print(p.betRequest(state['game_state']))
