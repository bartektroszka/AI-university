from random import randint

#((number, kolor)) 2,3....13,14 //  1,2,3,4
def variant(hand):
    list_of_numbers = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(5):
        list_of_numbers[hand[i][0]] += 1
    numbers = set()
    counter = 0
    colors = set()
    for i in range(5):
        colors.add(hand[i][1])
    if len(colors) == 1: #wszystkie mają ten sam kolor
        if abs(max((l[0] for l in hand)) - min((l[0] for l in hand))) == 4:#mamy pokera
            return 7
        else: #mamy kolor
            return 4
    
    for i in range(5):
        if hand[i][0] in numbers:
            counter += 1
        else:
            numbers.add(hand[i][0])
    if max(list_of_numbers) == 4:
        return 6 #kareta
    if len(numbers) == 2:
        return 5 #ful
    if len(numbers) ==5:
        if abs(max((l[0] for l in hand)) - min((l[0] for l in hand))) == 4:
            return 3 #street
    if len(numbers) == 3:
        if max(list_of_numbers) == 3:
            return 2 #trójka
        else:    
            return 1 #dwie pary
    if len(numbers) == 4:
        return 0 #para
    return -1


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




def play_games(num_of_games, cards_out): #cards out np. ((4,4), (9,2))
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



for i in range(10):
    print("____________________________________________")
    play_games(1000, ())
print("____________________________________________")


#aby blotkarz wygrywał trzeba mu ułożyć taką talię aby łatwo mu było wylosować fula