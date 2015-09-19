
from player import Player
from StateBuilder import StateBuilder, PlayerMock, MyPlayer, Card

class Scenarios:
    def run(self):
        pass

if __name__ == '__main__':
    p = Player()
    state = StateBuilder()\
        .withPlayer(MyPlayer()\
            .withCards(Card.buildCards("Ks Kh"))\
            .withStack(800))\
        .withPlayer(PlayerMock("C# Team"))\
        .withPlayer(PlayerMock("Java Team"))\
        .withCommunityCards(Card.buildCards("7d 7s 7h"))\
        .withBuyIn(500)\
        .withPot(550)\
        .build()

    print p.betRequest(state)
