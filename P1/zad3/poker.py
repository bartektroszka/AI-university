from random import randint

#((number, kolor)) 2,3....13,14 //  1,2,3,4
def variant(hand):
    numbers = set()
    counter = 1
    colors = set()
    for i in range(5):
        colors.add(hand[i][1])
    if len(colors) == 1:
        if abs(max((l[0] for l in hand)) - min((l[0] for l in hand))) == 4:
            return 7
        else:
            return 6
    
    for i in range(5):
        if hand[i][0] in numbers:
            counter += 1
        else:
            numbers.add(hand[i][0])
    if counter == 4:
        return 5
    if len(numbers) == 2:
        return "ful"
    if abs(max((l[0] for l in hand)) - min((l[0] for l in hand))) == 4:
        return 4
    if len(numbers) == 3:
        if counter == 3:
            return 3
        else:
            return 2
    if len(numbers) == 4:
        return 1
    return 0


def random_hand_blot(cards_out): #losowa talia dla blotkarza
    hand = []
    for i in range(5):
        stopper = False
        while stopper == False:
            number = randint(2,10)    #mozemy zmienic zakres czyli wyrzucić 4 karty o najniższych wartościach
            color = randint(1,4)
            if not (((number, color) in hand) or ((number, color) in cards_out)):
                hand.append((number, color))
                stopper = True
    return hand

def random_hand_royal():
    hand = []
    for i in range(5):
        stopper = False
        while stopper == False:
            number = randint(11,14)
            color = randint(1,4)
            if not ((number, color) in hand):
                hand.append((number, color))
                stopper = True
    return hand




def play_games(num_of_games, cards_out):
    royal_score = 0
    blot_score = 0
    for i in range(num_of_games):
        royal_hand = random_hand_royal()
        blot_hand = random_hand_blot(cards_out)
        if variant(royal_hand) >= variant(blot_hand):
            royal_score += 1
        else:
            blot_score += 1
    print("royal score:", royal_score)
    print("blot score:", blot_score)



for i in range(5):
    play_games(1000, ((2,1), (2,2), (2,3)))
print("____________________________________________")
