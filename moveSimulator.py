import json
import pokerCheatSheetGenerator

def handsort(hand):
    result = [hand,[1,2,3,4,5]]
    for i in range(0,5):
        for j in range(i+1,5):
            if (hand[i] > hand[j]):
                swaptmp = hand[j]
                hand[j] = hand[i]
                hand[i] = swaptmp

                swaptmp = result[1][j]
                result[1][j] = result[1][i]
                result[1][i] = swaptmp
    return result

def sortmaskstore(input):
    maskstore = input
    # for i in maskstore:
    #     print(i)
    # print(len(maskstore))
    for i in range (0, len(maskstore)):
        for j in range (i, len(maskstore)):
            if maskstore[i][1] < maskstore[j][1]:
                swaptmp = maskstore[j][1]
                maskstore[j][1] = maskstore[i][1]
                maskstore[i][1] = swaptmp

                swaptmp = maskstore[j][0]
                maskstore[j][0] = maskstore[i][0]
                maskstore[i][0] = swaptmp
    return maskstore

def whichdicestothrow(unsortedhand):
    handwithmask = handsort(unsortedhand)
    hand = handwithmask[0]
    print(hand)
    filename = 'data/'
    for character in hand:
        filename += str(character)
    filename += '.json'
    print(filename)
    with open(filename, 'r') as f:
        datastore = json.load(f)

    myHand = pokerCheatSheetGenerator.whatbesthandplayerhad(hand)
    # print(datastore)
    tmpmaskstore = []
    for i in range(0,len(datastore)//8):
        probability = 0
        for j in range (0,8):
            # print("MyHand: ", myHand, " hand from table: ", datastore[8 * i + j][2],
            #       " probability from table: ", datastore[8 * i + j][3],
            #       " mask from table: ", datastore[8 * i + j][1])
            if myHand <= datastore[8 * i + j][2]:
                probability += datastore[8 * i + j][3]
        # print("Mask: ", datastore[8 * i][1], " probability: ", round(probability,4))
        tmpmaskstore.append([datastore[8 * i][1], round(probability,4), ])

    # for t in tmpmaskstore:
    #     print(t)

    sortedstore = sortmaskstore(tmpmaskstore)

    sortedcutstore = []
    max = sortedstore[0][1]

    for s in sortedstore:
        if s[1] == max:
            sortedcutstore.append(s)
        # print(s)

    for s in sortedstore:
        print(s)

whichdicestothrow([1,1,5,4,3])