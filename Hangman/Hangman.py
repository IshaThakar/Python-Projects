import random
title=('''
    _      _            ___      ___
   | |____| |          | |\ \  / /| |
   |  ____  | A N G    | | \ \/ / | | A N 
   | |    | |          | |  \__/  | |
   |_|    |_|          |_|        |_|
  ''')
rhand=('''
            ______
           |      |
           |      0
           |      |\.
           |
''')
lhand=('''
            ______
           |      |
           |      0
           |     /|\.
           |
''')
lleg=('''
            ______
           |      |
           |      0
           |     /|\.
           |     / \.
''')
rleg=('''
            ______
           |      |
           |      0
           |     /|\.
           |       \.
''')
head=(''' 
            ______
           |      |
           |      0
           |
           |
          
          ''')
body=('''
            ______
           |      |
           |      0
           |      |
           |
        
            ''')
print(title)
list=['banana','quilt','cash','vibe','treated','oil','worth','snake','nearest','palatalise','beta','slope','fruit','lock','wedge','bunch','being','moist','leather','deconsecrate','total','period','sent','tight','recall','ghost','fewer','hoof','stray','permit','seamy','slug','prize','suppose','repeat','front','stake','wall','reek','rend','commission','separate','ultra','satisfied','metal','call','stronger','taped','duct','near','reach']
word=random.choice(list).lower()
n=int(len(word))
life=6
placeholder=''
for i in range(n):
    placeholder+="_"
print(placeholder)
correctletters=[]
gameover=False

#to display the letters chosen correctly
while gameover!=True:
 guess=input("Guess the letter\n").lower()
 display=''
 for i in word:
  if i==guess:
   display+=i
   correctletters.append(guess)
  elif i in correctletters:
      display+=i
  else :
   display+='_'
 print(display)

 if "_" not in display:
     gameover=True
     print("You guessed the word")

# to display man
 if guess not in word:
     life-=1
     print("life remaining", life, '/6')
     if life==5:
         print(head)
     elif life==4:
         print(body)
     elif life==3:
         print(rhand)
     elif life==2:
         print(lhand)
     elif life==1:
         print(rleg)
     else:
         print(lleg)
         print("YOU LOSE")
         print("THE WORD WAS",word)
         gameover=True





