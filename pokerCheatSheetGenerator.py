#
#
#
#
import itertools as it
from enum import Enum
from collections import Counter
import json
import time


class possibleHandsEnum:
    FIVE = 8
    FOUR = 7
    FULL = 6
    STRAIGHT = 5
    THREE = 4
    TWOPAIRS = 3
    ONEPAIR = 2
    BUST = 1


# check whether SORTED hand with length 5 has Five
def containsfive(hand):
    return hand[0] == hand[4]


# check whether SORTED hand with length 5 has Four
def containsFour(hand):
    return hand[0] == hand[3] or hand[1] == hand[4]


# check whether SORTED hand with length 5 has Full
def containsFull(hand):
    return (hand[0] == hand[2] and hand[3] == hand[4]) or (hand[0] == hand[1] and hand[2] == hand[4])


# check whether SORTED hand with length 5 has Straight
def containsStraight(hand):
    return hand[0] == (hand[1] - 1) == (hand[2] - 2) == (hand[3] - 3) == (hand[4] - 4)


# check whether SORTED hand with length 5 has Three
def containsThree(hand):
    return (hand[0] == hand[2]) or (hand[1] == hand[3]) or (hand[2] == hand[4])


# check whether SORTED hand with length 5 has Two Pairs
def containsTwoPairs(hand):
    return ((hand[0] == hand[1]) and (hand[2] == hand[3])) or ((hand[1] == hand[2]) and (hand[3] == hand[4]))


# check whether SORTED hand with length 5 has Pair
def containsPair(hand):
    for i in range(0, 4):
        if hand[i] == hand[i + 1]:
            return True
    return False


def containsbust(hand):
    for i in range(0, 4):
        if hand[i] == hand[i + 1]:
            return False
    return hand[0] == (hand[4] - 5)


def whatbesthandplayerhad(hand):
    sortedHand = sorted(hand)
    if containsfive(sortedHand):
        return possibleHandsEnum.FIVE
    if containsFour(sortedHand):
        return possibleHandsEnum.FOUR
    if containsFull(sortedHand):
        return possibleHandsEnum.FULL
    if containsStraight(sortedHand):
        return possibleHandsEnum.STRAIGHT
    if containsThree(sortedHand):
        return possibleHandsEnum.THREE
    if containsTwoPairs(sortedHand):
        return possibleHandsEnum.TWOPAIRS
    if containsPair(sortedHand):
        return possibleHandsEnum.ONEPAIR
    return possibleHandsEnum.BUST


def increase(inputlist):
    if inputlist[4] == 6:
        inputlist[4] = 1
        if inputlist[3] == 6:
            inputlist[3] = 1
            if inputlist[2] == 6:
                inputlist[2] = 1
                if inputlist[1] == 6:
                    inputlist[1] = 1
                    if inputlist[0] == 6:
                        inputlist[0] = 1
                        return []
                    else:
                        inputlist[0] += 1
                else:
                    inputlist[1] += 1
            else:
                inputlist[2] += 1
        else:
            inputlist[3] += 1
    else:
        inputlist[4] += 1
    return inputlist


def isHandNotDescending(hand):
    return hand[0] <= hand[1] <= hand[2] <= hand[3] <= hand[4]


def generateHandsList():
    result = []
    tmpHand = [1, 1, 1, 1, 1]
    for i in range(0, 7776):
        if isHandNotDescending(tmpHand):
            # print(tmpHand)
            result += tmpHand

        increase(tmpHand)
    secondresult = []
    # 252 - ilość kombinacji bez powtórzeń 5-elementowych w zbiorze 6-elementowym
    for x in range(0, 252 * 5, 5):
        secondresult.append(result[x:x + 5])

    return secondresult


handsList = generateHandsList()


def onesNumber(singleMask):
    count = 0
    for el in singleMask:
        if el == 1:
            count += 1
    return count


masks = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 1, 0], [0, 0, 0, 1, 1], [0, 0, 1, 0, 0], [0, 0, 1, 0, 1],
         [0, 0, 1, 1, 0], [0, 0, 1, 1, 1],
         [0, 1, 0, 0, 0], [0, 1, 0, 0, 1], [0, 1, 0, 1, 0], [0, 1, 0, 1, 1], [0, 1, 1, 0, 0], [0, 1, 1, 0, 1],
         [0, 1, 1, 1, 0], [0, 1, 1, 1, 1],
         [1, 0, 0, 0, 0], [1, 0, 0, 0, 1], [1, 0, 0, 1, 0], [1, 0, 0, 1, 1], [1, 0, 1, 0, 0], [1, 0, 1, 0, 1],
         [1, 0, 1, 1, 0], [1, 0, 1, 1, 1],
         [1, 1, 0, 0, 0], [1, 1, 0, 0, 1], [1, 1, 0, 1, 0], [1, 1, 0, 1, 1], [1, 1, 1, 0, 0], [1, 1, 1, 0, 1],
         [1, 1, 1, 1, 0], [1, 1, 1, 1, 1]]

masksOne = [x for x in masks if onesNumber(x) == 1]
masksTwo = [x for x in masks if onesNumber(x) == 2]
masksThree = [x for x in masks if onesNumber(x) == 3]
masksFour = [x for x in masks if onesNumber(x) == 4]
masksFive = [x for x in masks if onesNumber(x) == 5]


# print(masksOne)
# print(masksTwo)
# print(masksThree)
# print(masksFour)
# print(masksFive)

# Return list with probabilities for [Five, Four, Full, Straight, Three, TwoPairs, Pair, Bust]
def calculateProbabilityOneDice(inputHand, mask):
    maskIndexes = []
    for x in range(0, len(mask)):
        if (mask[x] == 1):
            maskIndexes.append(x)

    result = []

    for i in range(1, 7):
        for mIndex in maskIndexes:
            hand = []
            for ih in inputHand:
                hand.append(ih)
            hand[mIndex] = i
            # print("Hand: ", hand)
            result.append(whatbesthandplayerhad(hand))
            # print("Mask: ", mask)

    return result


def calculateProbabilityTwoDices(inputHand, mask):
    maskIndexes = []
    for x in range(0, len(mask)):
        if (mask[x] == 1):
            maskIndexes.append(x)

    result = []
    hand = inputHand

    for i in range(1, 7):

        for j in range(1, 7):
            hand = []
            for ih in inputHand:
                hand.append(ih)
            hand[maskIndexes[0]] = i
            hand[maskIndexes[1]] = j
            result.append(whatbesthandplayerhad(hand))
            # print("Hand: ", hand)
            # print("Mask: ", mask)

    return result


def calculateProbabilityThreeDices(inputHand, mask):
    maskIndexes = []
    for x in range(0, len(mask)):
        if (mask[x] == 1):
            maskIndexes.append(x)

    result = []

    for i in range(1, 7):
        for j in range(1, 7):
            for z in range(1, 7):
                hand = []
                for ih in inputHand:
                    hand.append(ih)
                hand[maskIndexes[0]] = i
                hand[maskIndexes[1]] = j
                hand[maskIndexes[2]] = z
                # print("Hand: ", hand)
                # print("Mask: ", mask)
                result.append(whatbesthandplayerhad(hand))

    return result


def calculateProbabilityFourDices(inputHand, mask):
    maskIndexes = []
    for x in range(0, len(mask)):
        if (mask[x] == 1):
            maskIndexes.append(x)

    result = []

    for i in range(1, 7):
        for j in range(1, 7):
            for z in range(1, 7):
                for a in range(1, 7):
                    hand = []
                    for ih in inputHand:
                        hand.append(ih)
                    hand[maskIndexes[0]] = i
                    hand[maskIndexes[1]] = j
                    hand[maskIndexes[2]] = z
                    hand[maskIndexes[3]] = a
                    # print("Hand: ", hand)
                    # print("Mask: ", mask)
                    result.append(whatbesthandplayerhad(hand))

    return result


# def calculateProbabilityFiveDices(hand, mask):
#
#     maskIndexes = []
#     for x in range(0, len(mask)):
#         if (mask[x] == 1):
#             maskIndexes.append(x)
#
#     result = []
#
#
#     for i in range(1,7):
#         for j in range(1,7):
#             for z in range(1,7):
#                 for a in range (1,7):
#                     for b in range(1,7):
#                         hand[maskIndexes[0]] = i
#                         hand[maskIndexes[1]] = j
#                         hand[maskIndexes[2]] = z
#                         hand[maskIndexes[3]] = a
#                         hand[maskIndexes[4]] = b
#                         print("Hand: ", hand)
#                         print("Mask: ", mask)
#                         result.append(whatBestHandPlayerHas(hand))
#
#
#     return result

def calculateAllProbabilities(hand):
    result = []
    for m4 in masksFour:
        tmp = calculateProbabilityFourDices(hand, m4)
        c = Counter(tmp)
        counterSum = sum(c.values())
        for i in range(1, 9):
            g = c.get(i)
            if g == None:
                g = 0
            result.append([hand, m4, i, round((g / counterSum), 4)])
    for m3 in masksThree:
        tmp = calculateProbabilityThreeDices(hand, m3)
        c = Counter(tmp)
        counterSum = sum(c.values())
        for i in range(1, 9):
            g = c.get(i)
            if g == None:
                g = 0
            result.append([hand, m3, i, round((g / counterSum), 4)])
    for m2 in masksTwo:
        tmp = calculateProbabilityTwoDices(hand, m2)
        c = Counter(tmp)
        counterSum = sum(c.values())
        for i in range(1, 9):
            g = c.get(i)
            if g == None:
                g = 0
            result.append([hand, m2, i, round((g / counterSum), 4)])
    for m1 in masksOne:
        tmp = calculateProbabilityOneDice(hand, m1)
        c = Counter(tmp)
        counterSum = sum(c.values())
        for i in range(1, 9):
            g = c.get(i)
            if g == None:
                g = 0
            result.append([hand, m1, i, round((g / counterSum), 4)])
    # print(result)
    return result


# r = calculateAllProbabilities([1,1,1,1,2])


# start = time.time()
#
# for hand in handsList:
#     fileName = ''
#     for dice in hand:
#         fileName += str(dice)
#     fileName += '.json'
#
#     # with open('data2/' + fileName, 'w') as outfile:
#     #     json.dump(calculateAllProbabilities(hand), outfile)
#
# stop = time.time()
#
# print("Cheatsheet generated. It took ", stop - start, "seconds")


# x = calculateAllProbabilities([1,1,1,1,2])

# print(len(x))
# print(x)


# print(cnt)
# cnt = Counter(calculateAllProbabilities([1,2,3,4,5]))
# print(cnt)
# c = 0
# for i in range(1,9):
#     c += cnt[i-1]
# print(c)

# print(calculateProbabilityFiveDices([1,2,3,4,4], [1,1,1,1,1]))
