import random
import time
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
           'p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O',
           'P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']
print("Auto Password Generator Started...\n(Press Ctrl + C to stop)\n")
while True:
    random.seed(time.time())
    password = ""
    n_letters = random.randint(4, 6)
    n_numbers = random.randint(2, 4)
    n_symbols = random.randint(2, 3)
    for i in range(n_letters):
        password += random.choice(letters)
    for i in range(n_numbers):
        password += random.choice(numbers)
    for i in range(n_symbols):
        password += random.choice(symbols)
    current_time = time.strftime("%H:%M:%S")
    print(f"[{current_time}] Generated Password: {password}")
    time.sleep(3)
