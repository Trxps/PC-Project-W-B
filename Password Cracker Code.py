#This imports the librarys necessary for the code.
import itertools #(itertools is for Functions creating iterators for efficient looping)
import string #(string contains a number of functions to process standard Python strings)

def guess_password(real):
    #setting the only available characters as letters and numbers.
    chars = string.ascii_lowercase + string.digits
    attempts = 0
    #the password length can be up to 15 characters with this range.
    for password_length in range(1, 15):
        for guess in itertools.product(chars, repeat=password_length):
            #counts each attempt to be shown how many attempts were made to crack the password.
            attempts += 1
            guess = ''.join(guess)
            #if the password is real/correct the password will be returned and shown in the format of the correct password
            #followed by the amount of attempts it took to actually get the password.
            if guess == real:
                return 'password is {}. found in {} guesses.'.format(guess, attempts)
            #prints the amount of guesses/attempts the cracker made.
            print(guess, attempts)
#This is where you input your password in which you want to be cracked.
print(guess_password(input("Enter the password that you want to be cracked:")))

#Warning, the longer your word in the range will define on how quickly it can be cracked, using a short word such as "abc"
#wont take long but if you use a word longer than 5 letters/words it will take a while to get
