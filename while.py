password = 12345678

while True:
    input =int(input("Enter your password: "))

    if input == password:
        print("Password accepted. Welcome!")
        break  
    else:
        print("Incorrect password. Try again.")
        break