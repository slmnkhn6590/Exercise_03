import random
random_number = (random.randint(1,100))
count = 0

#create a loop which will tell the user about his guess
while True:
    
    count = 1 + count
    type_number = int(input("guess the number between the 1 and 100 "))
    if random_number == type_number:
        print("awesome you guess it write you want to guess it again")
        print(count)
        break
    elif random_number < type_number:
        print("you number is greater")
    elif random_number > type_number:
        print("your numer is smaller")
    else:
        print("sorry but please it should be between 100 and 1")
   
