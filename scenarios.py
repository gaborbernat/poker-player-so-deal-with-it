
from player import Player
from StateBuilder import StateBuilder, PlayerMock, MyPlayer, Card

class Scenarios:
    def run(self):
        pass

if __name__ == '__main__':
    p = Player()
    state = StateBuilder()\
        .withPlayer(MyPlayer()\
            .withCards((Card("K", "spades"),Card("K", "hearts"),))\
            .withStack(800))\
        .withPlayer(PlayerMock("C# Team"))\
        .withPlayer(PlayerMock("Java Team"))\
        .withCommunityCards((Card("7", "diamonds"), Card("7", "spades"), Card("7", "hearts"),))\
        .withBuyIn(500)\
        .withPot(550)\
        .build()

    print p.betRequest(state)
