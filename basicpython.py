



#BASIC CODES

'''
ADDITION
SIMPLE INTEREST
PRIME NO IN INTERVAL
PRIME NO
AREA OF SHAPE
FIBONACCI SERIES
SUM ON SQAURE OF 1ST N NOS
SUM ON CUBES OF 1ST N NOS
ASCCI NO OF CHARACTER  ORD()
'''


"""
#add two numbers

a=2
b=5
c=a+b
print(c)"""

'''
#factorial of no
n = int(input())
fact = 1
for i in range (1,n+1):
    fact = fact * i

print(fact)

'''


'''
#Simple interest formula is given by:
#Simple Interest = (P x T x R)/100

p=int(input("enter principle amount"))
r=int(input("enter rate"))
t=int(input("enter time in years"))

simpleinterest = (p * t * r)/100

print(simpleinterest)
'''





'''
# Python program to print all  
# prime number in an interval 

lower =  2
upper = 10 
  
for num in range(lower,upper + 1):  
    
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:  
           print(num) 
'''


'''
#check whether no prime or not

a=int(input("enter a number"))


for i in range(2,a+1):
    if(a%i)==0:
        print("not prime")
        break;
    else:
        print("prime")
        break;

'''

'''

#find area of the circle

r=int(input("enter the radius "))

area=3.142*r*r

print("area is",area)



'''





'''
#fibonacci sequence within a limit

n=int(input("enter a number"))


i,j=0,1
c=0

while(c<n):
    a=i+j
    i=j
    j=a
    c +=1
    print(a)
'''




'''
# Python program to print  
# ASCII Value of Character 

#ord()


a=(input("enter a character"))

print("ASCII value of the character " ,a ,"  is ",ord(a))


'''






#Python Program for cube sum of first n natural numbers
#Python Program for square sum of first n natural numbers

'''
def sq(n):
    return  (n*(n+1) * (2*n+1)) /6   
 


def cube(n):
    return ( (n*(n+1) )/2)**2
 

print(sq(4))
print(cube(4))
    

'''





#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------




#Array  Programs:
















