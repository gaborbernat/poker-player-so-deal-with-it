from player import Player

state = {
    "type": "bet",
    "on_turn": 1,
    "message": "LeanMasters made a bet of 0 (fold) and is left with 970 chips. The pot now contains 230 chips.",
    "game_state": {
        "tournament_id": "55e6f2bb0708790003000002",
        "game_id": "55fd4e431474db00030000ca",
        "round": 1,
        "players": [
            {
                "name": "booLean",
                "stack": 990,
                "status": "folded",
                "bet": 0,
                "hole_cards": [
                    {
                        "rank": "9",
                        "suit": "spades"
                    },
                    {
                        "rank": "J",
                        "suit": "diamonds"
                    }
                ],
                "version": "Default PHP folding player",
                "id": 0
            },
            {
                "name": "LeanMasters",
                "stack": 970,
                "status": "active",
                "bet": 10,
                "hole_cards": [
                    {
                        "rank": "A",
                        "suit": "clubs"
                    },
                    {
                        "rank": "4",
                        "suit": "hearts"
                    }
                ],
                "version": "Enjoy",
                "id": 1
            },
            {
                "name": "So Deal With It ",
                "stack": 960,
                "status": "active",
                "bet": 20,
                "hole_cards": [
                    {
                        "rank": "3",
                        "suit": "hearts"
                    },
                    {
                        "rank": "7",
                        "suit": "hearts"
                    }
                ],
                "version": "1.0.1",
                "id": 2
            },
            {
                "name": "AsdfLEAN",
                "stack": 1050,
                "status": "folded",
                "bet": 0,
                "hole_cards": [
                    {
                        "rank": "6",
                        "suit": "spades"
                    },
                    {
                        "rank": "7",
                        "suit": "clubs"
                    }
                ],
                "version": "AsdfLEAN 1.8",
                "id": 3
            },
            {
                "name": "PokerMinds",
                "stack": 800,
                "status": "active",
                "bet": 200,
                "hole_cards": [
                    {
                        "rank": "10",
                        "suit": "spades"
                    },
                    {
                        "rank": "A",
                        "suit": "hearts"
                    }
                ],
                "version": "Default Java folding player",
                "id": 4
            }
        ],
        "small_blind": 10,
        "orbits": 0,
        "dealer": 0,
        "community_cards": [],
        "current_buy_in": 200,
        "pot": 230
    }
}
if __name__ == '__main__':
    p = Player()
    print(p.betRequest(state['game_state']))
