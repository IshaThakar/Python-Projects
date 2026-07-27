import random


def deal_card():
        """returns a random card from deck"""
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card = random.choice(cards)
        return card
def calculate_score(cards):
   if sum(cards) == 21 and len(cards) == 2:
    return 0
   if 11 in cards and sum(cards) == 21:
       cards.remove(11)
       cards.append(1)
   return sum(cards)

def compare(u_score, c_score):
    if u_score==c_score:
        return "draw"
    elif c_score==0:
        return "you lose opponent has a blackjack"
    elif u_score==0:
        return "you Win with a blackjack"
    elif u_score > 21:
        return "you went over, you lose"
    elif c_score > 21:
        return "opponent went over, you win"
    elif u_score > c_score:
        return "you win"
    else:
        return f"you lose"

def play_game():

 user_card=[]
 comp_card=[]
 comp_score=-1
 user_score=-1

 is_game_over = False
 for _ in range(2):
    user_card.append(deal_card())
    comp_card.append(deal_card())


 while not is_game_over:
  user_score=calculate_score(user_card)
  comp_score=calculate_score(comp_card)
  print(f"users card: {user_card},users score: {user_score}")
  print(f"computers first card: {comp_card[0]}")

  if user_score==0 or comp_score==0 or user_score>22:
     is_game_over=True
  else :
     deal=input("Type y to get another card and n to pass").lower()
     if deal=='y':
         user_card.append(deal_card())
     else :
         is_game_over=True


 while comp_score!=0 and comp_score<17:
     comp_card.append(deal_card())
     comp_score=calculate_score(comp_card)
 print(f"users card: {user_card},users score: {user_score}")
 print(f"computers card: {comp_card},computer score: {comp_score}")
 print(compare(user_score, comp_score))
 n=input("Type y to play again n to end").lower()
 while n=="y":
      print("\n"*20)
      play_game()

play_game()

