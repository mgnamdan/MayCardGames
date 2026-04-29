from card import Card
from deck import Deck

def main():
    testDeck = Deck()
    testDeck2 = Deck()

    print(testDeck == testDeck2)

    testDeck.shuffle()
    testDeck2.shuffle()

    print(testDeck == testDeck2)





main()