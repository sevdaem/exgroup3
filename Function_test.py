'''
def function(named_arg,*args):
    print(named_arg)
    print(args)
function(1,2,3,4,5)

def function(x,y,food="spam"):
    print(food)
function(1,2)
function(3,4,"egg")

def my_func(x,y=7,*args,**kwargs):
    print(x,y,args,kwargs)
my_func(2,3,4,5,6,a=7,b=8)

numbers = (1,2,3)
a,b,c=numbers
print(a)
print(b)
print(c)

a,b,*c,d=[1,2,3,4,5,6,7,8]
print(a)
print(b)
print(c)
print(d)

a=7
b=1 if a >= 5 else 42
print(b)

fruits = ["apple","bnana","cherry"]
for i in fruits:
    if i == "bnana":
        continue
    print(i)
    
i = 1
while i < 6:
    print(i)
    i+=1
else:
    print("i is no longer than 6")
    
def func():
    print("this is a module function")
if __name__=="main":
    print("this is a script")
    '''
#if
# a==b  a != b    a>b        a>=b     a<b a<=b
#Ternary operator
'''
i = 0
while i <= 5:
    i +=1
    
    
    print(i)

else:
    print("a")

list_a=['a,b,n,df,sf']
for i in range(100,10,-1):
    print(i)
'''
list1=[]
if not list1:
    print("a")