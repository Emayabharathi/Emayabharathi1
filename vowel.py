x=input()
x=x.lower()
if(x>="a" and x<="z"):
  if(x=="a" or x=="e" or x=="i" or x=="o" or x=="u"):
    print("Vowel")
  else:
    print("Consonent") 
else:
  print("Invalid")    
