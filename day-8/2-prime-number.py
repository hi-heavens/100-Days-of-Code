#Write your code below this line ๐
def prime_checker(number):
    is_prime = True
    if number < 1:
        print("Try again!")
    else:
        for num in range(2, number):
            if number % num == 0:
                is_prime = False

        if not is_prime:
            print("It's not a prime number.")
        else:
            print("It's a prime number.")


#Write your code above this line ๐
    
#Do NOT change any of the code below๐
n = int(input("Check this number: "))
prime_checker(number=n)
