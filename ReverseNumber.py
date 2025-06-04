def reverse_number(num):
    reversed=0
    while num>0 :
        digit=num%10
        reversed = reversed * 10 + digit
        num//=10
    return reversed    
        
num=int(input("Enter a number:"))    
reversed_number=reverse_number(num)
print("The reversed number is ",reversed_number)