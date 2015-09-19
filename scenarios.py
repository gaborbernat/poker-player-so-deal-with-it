
from player import Player
from StateBuilder import StateBuilder, PlayerMock, MyPlayer, Card

class Scenarios:
    def run(self):
        pass

if __name__ == '__main__':
    p = Player()
    state = StateBuilder()\
        .withPlayer(MyPlayer().withCards((Card("K"),Card("A"),)))\
        .withPlayer(PlayerMock())\
        .build()

    print p.betRequest(state)
