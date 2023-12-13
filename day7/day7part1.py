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

    print(hands_and_bids)



def compare_hands(hand1, hand2):
    # check for type
    type_hand1 = find_highest_type(hand1)
    type_hand2 = find_highest_type(hand2)

def find_highest_type(hand):
    if(bool(re.match(r'^(.)\1{4}$', hand))):
        # Five of a kind, where all five cards have the same label: AAAAA
        return 'five of a kind'
    elif(bool(re.match(r'(.)\1{3,}', hand))):
        # Four of a kind, where four cards have the same label and one card has a different label: AA8AA
        return 'four of a kind'
    elif(bool(re.match(r'^(.)\1{2}(.)\2{1}$', hand))):
        # Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
        return 'full house'
    elif(bool(re.match(r'^(.)\1{2}[^.]*$', hand))):
        # Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
        return 'three of a kind'
    elif(bool(re.match(r'^(.)\1{1}(.)\2{1}[^.]*$', hand))):
        # Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
        return 'two pair'
    elif(bool(re.match(r'^(.)\1{1}([^.\1]*\1[^.\1]*){2}$', hand))):
        # One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
        return 'one pair'
    else:
        # High card, where all cards' labels are distinct: 23456  
        return 'high card'


    
print(find_highest_type('J3JJJ'))
print(bool(re.search(r'(.)\1{3,}', 'JeJJJ')))
    
    
