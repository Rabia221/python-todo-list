import  random

secret_number =random.randint( 1, 20)
print('Guess a number between 1 and 20')
guess = int(input('Your Guess:'))

if guess < secret_number:
    print('"Congratulations You guessed it right')
elif guess < secret_number:
    print('Too low Try again')
else:
    print('Too high Try again')
    
    
attempts =0
while True:
    guess =int(input('Your guess'))
    
    attempts += 1
    if guess == secret_number:
         print(f"Congratulations You guessed it in {attempts} tries ")
         break
    elif guess < secret_number:
        print('Too high try again')
    elif guess < secret_number:
        print('Too low try again')
        