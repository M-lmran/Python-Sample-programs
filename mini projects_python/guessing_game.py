from random import randint
a = input("enter username : \n")
b = input("enter password : \n")
def guessing(answer,user):
  if answer == user:
        print("you are a genius")
        # return True
  else:
   print("username or password invalid")
if __name__ == "__main__":
  a = randint(1,10)
  while True:
      user = int(input("enter a number : "))
      if guessing(a,user):
          break
      else:
          print("try agin")
        
       
          

  


            
        
        


# answer = randint(1,10)

# while True:
   
#    user = int(input("enter your input as natural number: "))
#    print(answer)
    
#    if user == answer:
#         print("hoorrayyy you guessedd it")
#         break
        
#    else:
#         print("sorry try again")
         
   
   