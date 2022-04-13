Number = int(input("Insira um número para ser invertido: "))    
Reverse = 0    
while(Number > 0):    
    Reminder = Number %10    
    Reverse = (Reverse *10) + Reminder    
    Number = Number //10    
     
print("\n O número inserido ao inverso é = %d" %Reverse) 