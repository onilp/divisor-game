# Onil Pravasi
# cs-335, Fall 2018
# Asst 6
import math

p1=input("Enter the FIRST player's name: ")
p2=input("Enter the SECOND player's name: ")
print()
n = int(input("Enter a positive integer n: "))
print()
i=1
div =[]
   
while(i<=n):
   if(n%i==0):
      div.append(i)
   i=i+1   
count=1
while(len(div)!=0):
   if (count==1):
      p=p1
      count+=1
   else:
      p=p2
      count-=1 
   print ("Here are the remaining numbers:",div)
   m = int(input(str(p) +" which one do you pick? :"))
   print()
   if(m==div[-1]):
      print ("You lose,",p,"!")
      print()
      print ("Bye!")
   new_list = div[0:(div.index(m)+1)]
   up_list = div[(div.index(m)+1):]
   #print new_list
   #print up_list
   for i in new_list:
      if(m%i!=0):
         up_list.append(i)
         up_list.sort()
   div=up_list