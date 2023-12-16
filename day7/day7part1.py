import re
import pprint
#  A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2

# JJJJJ 435
# 29QA4 847
# 6A9A9 348

# goal is to order DESC
def swap_hands(hand1, hand2):
    # check for type
    type_hand1 = find_type(hand1)
    type_hand2 = find_type(hand2)
    # print(type_hand1, type_hand2)
    # return new order
    if(type_hand1 > type_hand2):
        return False
    elif(type_hand1 < type_hand2):
        return True
    elif(type_hand1 == type_hand2):
        # now the hands need to be compared by the highest first character
        card_hierachy = '23456789TJQKA'
        for i in range(5):
            card_hierachy1 = card_hierachy.index(hand1[i])
            print(f'card hierachy: {card_hierachy1}')
            card_hierachy2 = card_hierachy.index(hand2[i])
            print(f'card hierachy: {card_hierachy2}')
            if(card_hierachy1 > card_hierachy2):
                return False
            elif(card_hierachy1 < card_hierachy2):
                return True
        # after going though both hands: they are both identical
        # the order of hands is returned unchanged
        return False


def find_type(hand):
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

    for count in char_count.values():
        if(count == x):
            return f'{x} of a kind'

    return None

def fullhouse(hand):
    char_count = {}
    for character in hand:
        if character in char_count:
            char_count[character] += 1
        else:
            char_count[character] = 1
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
    if sum(value == 2 for value in char_count.values()) == 2 :
        return 'two pairs'
    else:
        return None

# bubble sort
def sort(list_of_hands):
    swapped_in_this_iteration = True
    print(list_of_hands)
    while(swapped_in_this_iteration):
        swapped_in_this_iteration = False
        for i in range(len(list_of_hands)-1):
            # compare i and i+1
            hand1 = list_of_hands[i]['hand']
            hand2 = list_of_hands[i+1]['hand']
            print(f'Hand1: {hand1}, Hand2:{hand2}')
            swap = swap_hands(hand1, hand2)
            print(f'Swap? {swap}')
            if(swap):
                list_of_hands[i], list_of_hands[i+1] = list_of_hands[i+1], list_of_hands[i]
                swapped_in_this_iteration = True
    # print(list_of_hands)
    for hand in list_of_hands:
        print(hand)
    return list_of_hands



with open("/Users/friedrichtenhagen/coding/advent_of_code_2023/day7/input.txt") as f:
    data = f.read().strip()
    lines = data.split("\n")

    hands_and_bids = []
    for line in lines:
        split_line = line.split(' ')
        hand = split_line[0]
        bid = split_line[1]
        hands_and_bids.append({'hand': hand, 'bid': bid})
  
    sorted_list_of_hands = sort(hands_and_bids)
    ascending_list = sorted_list_of_hands[::-1]
    print(ascending_list)

    # Now, you can determine the total winnings of this set of hands by 
    # adding up the result of multiplying each hand's bid with its rank
    total_winnings = 0
    for index, hand in enumerate(ascending_list):
        total_winnings += int(hand['bid']) * (index+1)

    print(f'Total winnings: {total_winnings}')



