import random
logo="""
   ____     _   _ U _____ u ____    ____              _____    _   _  U _____ u          _   _       _   _   __  __     ____  U _____ u   ____     
U /"___|uU |"|u| |\| ___"|// __"| u/ __"| u          |_ " _|  |'| |'| \| ___"|/         | \ |"|   U |"|u| |U|' \/ '|uU | __")u\| ___"|/U |  _"\ u  
\| |  _ / \| |\| | |  _|" <\___ \/<\___ \/             | |   /| |_| |\ |  _|"          <|  \| |>   \| |\| |\| |\/| |/ \|  _ \/ |  _|"   \| |_) |/  
 | |_| |   | |_| | | |___  u___) | u___) |            /| |\  U|  _  |u | |___          U| |\  |u    | |_| | | |  | |   | |_) | | |___    |  _ <    
  \____|  <<\___/  |_____| |____/>>|____/>>          u |_|U   |_| |_|  |_____|          |_| \_|    <<\___/  |_|  |_|   |____/  |_____|   |_| \_\   
  _)(|_  (__) )(   <<   >>  )(  (__))(  (__)         _// \\_  //   \\  <<   >>          ||   \\,-.(__) )(  <<,-,,-.   _|| \\_  <<   >>   //   \\_  
 (__)__)     (__) (__) (__)(__)    (__)             (__) (__)(_") ("_)(__) (__)         (_")  (_/     (__)  (./  \.) (__) (__)(__) (__) (__)  (__) 
"""
print(logo)
print("Welcome to number guessing game!")
print("I am thinking of a number between 1 and 100.")
level= input("choose a level: Easy , Hard").lower()
num=random.randint(1,100)
if level == "easy":
    life=10
else:
    life=5
while life > 0:
 print(f"You have {life} life left.")
 user_guess = int(input("Guess The number between 1 and 100\n"))
 if user_guess==num:
    print(f"You guessed right! the number was {num}")
    break
 elif user_guess > num:
    print("Too high!")
    print("Guess again.")
    life-=1
 elif user_guess < num:
    print("Too low!")
    print("guess again.")
    life-=1
 else:
     print("invalid input")
if life==0:
    print(f"Game over, the number was {num}")