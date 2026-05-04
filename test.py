from card import Card
from deck import Deck
from players import BlackJackPlayer

def main():
    # testDeck = Deck()
    # testCard = Card("Ace", "Spades")


    testPlayer = BlackJackPlayer()

    card1 = Card()
    card2 = Card("Seven", "Diamonds")
    card3 = Card("Ace", "Spades")
    card4 = Card("Ace", "Clubs")
    card5 = Card("Ten", "Hearts")

    testPlayer.draw(card2)
    testPlayer.draw(card3)

    testPlayer.showHand()
    testPlayer.calcScore()
    print(testPlayer.score)
    print("")

    testPlayer.discard(0)
    testPlayer.discard(0)

    testPlayer.draw(card3)
    testPlayer.draw(card4)

    testPlayer.showHand()
    testPlayer.calcScore()
    print(testPlayer.score)
    print("")

    testPlayer.discard(0)
    testPlayer.discard(0)

    testPlayer.draw(card1)
    testPlayer.draw(card3)
    testPlayer.draw(card4)
    testPlayer.draw(card5)

    testPlayer.showHand()
    testPlayer.calcScore()
    print(testPlayer.score)
    print("")

    # drawnCard = testDeck.draw()
    # print(drawnCard)
    # print("")
    # print(testDeck.drawPile)
    # print("")
    # print(testDeck.outPile)

    # testDeck.discard(testCard)
    # print("")
    # print(testDeck.discardPile)
    # print("")
    # print(testDeck.outPile)

    # testDeck.discard(drawnCard)
    # print("")
    # print(testDeck.discardPile)
    # print("")
    # print(testDeck.outPile)    





main()