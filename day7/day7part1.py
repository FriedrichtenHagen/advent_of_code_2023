import re

#  A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2

# JJJJJ 435
# 29QA4 847
# 6A9A9 348

with open("/Users/friedrichtenhagen/coding/advent_of_code_2023/day7/input.txt") as f:
    data = f.read().strip()
    lines = data.split("\n")

    hands_and_bids = {}
    for line in lines:
        split_line = line.split(' ')
        hand = split_line[0]
        bid = split_line[1]
        hands_and_bids[hand] = bid

    # print(hands_and_bids)


# goal is to order DESC
def compare_hands(hand1, hand2):
    # check for type
    type_hand1 = find_highest_type(hand1)
    type_hand2 = find_highest_type(hand2)
    # return new order
    if(type_hand1 > type_hand2):
        return hand1, hand2
    elif(type_hand1 < type_hand2):
        return hand2, hand1
    elif(type_hand1 == type_hand2):
        # now the hands need to be compared by the highest first character
        for i in range(5):
            if(hand1[i] > hand2[i]):
                return hand1, hand2
            elif(hand1[i] < hand2[i]):
                return hand2, hand1
        # after going though both hands: they are both identical
        # the order of hands is returned unchanged
        return hand1, hand2


def find_highest_type(hand):
    if(x_of_a_kind(hand, 5)):
        # Five of a kind, where all five cards have the same label: AAAAA
        return 7
    elif(x_of_a_kind(hand, 4)):
        # Four of a kind, where four cards have the same label and one card has a different label: AA8AA
        return 6
    elif(fullhouse(hand)):
        # Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
        return 5
    elif(x_of_a_kind(hand, 3)):
        # Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
        return 4
    elif(twopairs(hand)):
        # Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
        return 3
    elif(x_of_a_kind(hand, 2)):
        # One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
        return 2
    else:
        # High card, where all cards' labels are distinct: 23456  
        return 1

def x_of_a_kind(hand, x):
    char_count = {}
    for character in hand:
        if character in char_count:
            char_count[character] += 1
        else:
            char_count[character] = 1

    print(char_count)
    for count in char_count.values():
        if(count == x):
            return f'{x} of a kind'
        else:
            return None

def fullhouse(hand):
    char_count = {}
    for character in hand:
        if character in char_count:
            char_count[character] += 1
        else:
            char_count[character] = 1
    print(char_count)
    if 3 in char_count.values() and 2 in char_count.values():
        return 'full house'
    else:
        return None

def twopairs(hand):
    char_count = {}
    for character in hand:
        if character in char_count:
            char_count[character] += 1
        else:
            char_count[character] = 1
    print(char_count)
    if sum(value == 2 for value in char_count.values()):
        return 'two pairs'
    else:
        return None
# print(x_of_a_kind('JJJJJ', 5))
# print(x_of_a_kind('JJJ5J', 4))
# print(x_of_a_kind('JdJJ5', 3))
# print(x_of_a_kind('5d5JJ', 2))
# print(x_of_a_kind('mlkJo', 1))
# print(x_of_a_kind('dfert', 0))
# print(fullhouse('JddJJ'))
# print(twopairs('kkdid'))

print(compare_hands('kkkld', 'dkeli'))