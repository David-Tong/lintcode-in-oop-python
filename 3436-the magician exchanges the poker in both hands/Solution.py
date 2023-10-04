class Poker:
    def __init__(self, colour, num):
        # write your code here
        self.__colour = colour
        self.__num = num

    def __str__(self):
        # write your code here
        return "{},{}".format(self.__colour, self.__num)

class Hand:
    def __init__(self, poker):
        # write your code here
        self.__poker = poker
    
    def set_poker(self, poker):
        self.__poker = poker

    def get_poker(self):
        return self.__poker

class Person:
    def __init__(self, left_hand, right_hand):
        # write your code here
        self.__left_hand = left_hand
        self.__right_hand = right_hand

    def show_hand(self):
        # write your code here
        print("{} {}".format(self.__right_hand.get_poker(), self.__left_hand.get_poker()))

    def swap_hand(self):
        # write your code here
        tmp_poker = self.__right_hand.get_poker()
        self.__right_hand.set_poker(self.__left_hand.get_poker())
        self.__left_hand.set_poker(tmp_poker)
