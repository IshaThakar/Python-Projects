act='yes'
alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','!','@','#','$','%','^','&','*','<','>','?']

def caesar(text,shift_key,task):
  if task=='encode':
     final_msg = ''
     for i in msg:
         if i not in alpha:
             final_msg += i
         else:
             newindex= alpha.index(i)+shift
             newindex%=len(alpha)
             final_msg+=alpha[newindex]
     print(f"Your encrypted message is:{final_msg}")

  if task=='decode':
     final_msg = ''
     for i in msg:
         if i not in alpha:
             final_msg += i
         else:
             newindex= alpha.index(i)-shift
             newindex%=len(alpha)
             final_msg+=alpha[newindex]

     print(f"Your decrypted message is:{final_msg}")

while act=='yes':
 task = input("Type 'encode' to encrypt, type 'decode' to decrypt\n").lower()
 msg = input("Type your message\n")
 shift = int(input("Type the shift number\n"))
 caesar(text=msg,shift_key=shift,task=task)
 act=input("do you wish to continue? yes/no\n").lower()
if act=='no':
    print("Goodbye")

