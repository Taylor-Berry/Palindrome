import time

while True:
    user = input("Enter a word to check if it is a Palindrome: ").lower()
    print("Checking...")
    time.sleep(1)

    backwards = ""

    i = len(user)

    while i > 0:
        backwards += user[i - 1]
        i -= 1

    if backwards == user:
        print(("%s is a palindrome") % (backwards)) 
    else:
        print("Sorry...")
        break
        		
