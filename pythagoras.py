def theorem(a,b,c):
    x=c*c
    y=a*a+b*b
    
    if x==y:
        print(f"{a},{b},{c} is satisfied Pythagorean theorem")
    else:
        print(f"{a},{b},{c} is not satisfied Pythagorean theorem")
        
theorem(3,4,5)
theorem(3, 5,6)