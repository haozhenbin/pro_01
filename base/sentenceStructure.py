#for

for letter in "python" :
    print(letter);

fruits = ["apple","orange","mango","banana"];
for fruit in fruits:
    print(fruit);
print("bye!");

for i in range(len(fruits)):
    print("第",i+1,fruits[i]);

num = range(10,20);
for n in num:
    print(n," | ",end='');
    if(n%2==0):
        print(" 这个数是偶数。");
    else :
        print(" 这个是奇数 ");

for n in num:
    if(n == 10):
        print("NO ",n," Boss.");
    elif(n==11):
        print("NO ",n," Manager");
    elif(n==12):
        print("NO ",n," CFO.")
    elif(n>12 and n<15):
        print("NO ",n , " Mid Manager.");
    else:
        print("NO ",n," employee ");
numbers = [40,41,42,43,44,45,4,47,46,48,49,50];
#numbers = range(40,55);
even = [];
odd = [];
while len(numbers)>0:
    num = numbers.pop();
    if(num%2==0):
        print(num, " is even.");
        even.append(num);
    else:
        print(num , " is Odd.");
        odd.append(num);
i = 10;
while i>0 :
    print("current num is ",i);
    i= i-1 ;
    if(i==5):
        break;
i=10;
while i>0 :
    if(i==5):
        continue;
    print("current num is ",i);
    i= i-1 ;
print("bye!");


