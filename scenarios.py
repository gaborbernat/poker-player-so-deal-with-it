
from player import Player
from StateBuilder import StateBuilder, PlayerMock, MyPlayer, Card

class Scenarios:
    def run(self):
        pass

if __name__ == '__main__':
    p = Player()
    state = StateBuilder()\
        .withPlayer(MyPlayer().withCards((Card("K"),Card("K"),)))\
        .withPlayer(PlayerMock())\
        .withCommunityCards((Card("7", "diamonds"), Card("7", "spades"), Card("7", "hearts"),))\
        .build()

    print p.betRequest(state)
