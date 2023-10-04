from Solution import *

if __name__ == '__main__':
    p1 = Poker("Hearts", "A")
    p2 = Poker("Spades", "k")
    left_hand = Hand(p1)
    right_hand = Hand(p2)
    xiaoming = Person(left_hand, right_hand)
    xiaoming.show_hand()
    xiaoming.swap_hand()
    xiaoming.show_hand()