#MP4 Problem
def verbose():
    words={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',
           11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'
           }
    tens={2:'twenty',3:'thirty',4:'fourty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety'}
    for i in range(20,100):
        ones_digit=i%10
        tens_digit=i//10
        if ones_digit==0:
            words[i]=tens[tens_digit]
        else:
            words[i]=tens[tens_digit]+' '+words[ones_digit]

    return words

a=int(input('Enter a number(from 0-99):'))
d=verbose()
print(d[a])


#MP5 Problem
from random import shuffle
deck = [{'value':i, 'suit':c}
for c in ['spades', 'clubs', 'hearts', 'diamonds']
for i in range(2, 15)]
shuffle(deck)
pl1_cards=[deck.pop(0),deck.pop(0),deck.pop(0)]
pl2_cards=[deck.pop(0),deck.pop(0),deck.pop(0)]
def card_game(hand):
    card_names={11:'Jack',12:'Queen',13:'King',14:'Ace'}
    display_cards=[]
    for card in hand:
        val=card['value']
        name=card_names.get(val,str(val))
        display_cards.append(f"{name} of {card['suit']}")
    return ", ".join(display_cards)

print("Player 1 cards:",card_game(pl1_cards))
print("Player 2 cards:",card_game(pl2_cards))

pl1_values=sorted([card['value'] for card in pl1_cards],reverse=True)
pl2_values=sorted([card['value'] for card in pl2_cards],reverse=True)
winner=None
for i in range(3):
    if pl1_values[i]>pl2_values[i]:
        winner='Player 1'
        break
    elif pl2_values[i]>pl1_values[i]:
        winner='Player 2'
        break

if winner:
    print('The winner is',winner)
else:
    print('The game is a draw')



