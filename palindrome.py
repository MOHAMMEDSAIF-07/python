def pal(user):
    
    if user == user[::-1]: 
        print("the given number is palindrome")
    else:
        print("the given number is not palindrome")
        
pal(input("enter a number"))