import random
def number_guessing_game():
	''''number '''
	print("welcome to number guessing game")
	print("I am thinking of a number. can you guess it(between 1,100)")
	number=random.randint(1,100)
	attempt=0
	while True:
		guess=int(input("guess the number"))
		attempt +=1
		if(guess<number):
			print("too low.Try again")
		elif(guess>number):
			print("too high.try again")
		else:
			print("well done you gussed correctly")
			break
	    
if __name__ == "__main__":
  number_guessing_game()
