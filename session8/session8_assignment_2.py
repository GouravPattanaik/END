#1 write a program to reverse a list 
lst = [11, 5, 17, 18, 23]
def reverse(lst): 
    new_lst = lst[::-1] 
    return new_lst
	
#2 write a program to find sum of elements in list
list1 = [11, 5, 17, 18, 23]
total = sum(list1)
print("Sum of all elements in given list: ", total)

#3 write a program to find the largest number in a list 
list1 = [10, 20, 4, 45, 99] 
list1.sort() 
print("Largest element is:", list1[-1]) 

#4 write a program to print Even Numbers in a List 
list1 = [10, 21, 4, 45, 66, 93] 
for num in list1: 
    if num % 2 == 0: 
       print(num, end = " ") 
       
#5 write a program to print negative Numbers in given range 
start, end = -4, 19
for num in range(start, end + 1): 
    if num < 0: 
        print(num, end = " ") 
        
#6 write a program to remove empty List from List using list comprehension 
test_list = [5, 6, [], 3, [], [], 9] 
print("The original list is : " + str(test_list)) 
res = [ele for ele in test_list if ele != []] 
print ("List after empty list removal : " + str(res)) 

#7 write a  program to remove empty tuples from a list of tuples 
def Remove(tuples): 
    tuples = filter(None, tuples) 
    return tuples 
  
# Driver Code 
tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'),  
          ('krishna', 'akbar', '45'), ('',''),()] 
print Remove(tuples)

#8 write a program to break a list into chunks of size N
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]  
n = 4 
x = [l[i:i + n] for i in range(0, len(l), n)]  
print(x)

#9 write a program to find the frequency of words present in a string  
  
test_str = 'times of india times new india express'
print("The original string is : " + str(test_str)) 

res = {key: test_str.count(key) for key in test_str.split()} 
print("The words frequency : " + str(res))

#10 write a program to accept a string if it contains all vowels
def check(string): 
  if len(set(string).intersection("AEIOUaeiou"))>=5: 
    return ('accepted') 
  else: 
    return ("not accepted") 
  
if __name__=="__main__": 
  string="helloworld"
  print(check(string)) 
  

#11 write a program to rotate string left and right by d length  
def rotate(input,d):  
  
    Lfirst = input[0 : d]  
    Lsecond = input[d :]  
    Rfirst = input[0 : len(input)-d]  
    Rsecond = input[len(input)-d : ]  
  
    print ("Left Rotation : ", (Lsecond + Lfirst) ) 
    print ("Right Rotation : ", (Rsecond + Rfirst))  
  
if __name__ == "__main__":  
    input = 'helloworld'
    d=2
    rotate(input,d) 
    

#12 write a program to convert key-values list to flat dictionary 

from itertools import product 
test_dict = {'month' : [1, 2, 3], 
             'name' : ['Jan', 'Feb', 'March']} 
  
print("The original dictionary is : " + str(test_dict)) 
  
res = dict(zip(test_dict['month'], test_dict['name'])) 
print("Flattened dictionary : " + str(res)) 

# write a program to remove the duplicate words 
s = "Hello world Hello"
l = s.split() 
k = [] 
for i in l: 
    if (s.count(i)>1 and (i not in k)or s.count(i)==1): 
        k.append(i) 
print(' '.join(k)) 


#13 write a program to convert into dictionary 
def Convert(tup, di): 
    for a, b in tup: 
        di.setdefault(a, []).append(b) 
    return di 
      
tups = [("A", 10), ("B", 20), ("C", 30),  
     ("D", 40), ("E", 50), ("F", 60)] 
dictionary = {} 
print (Convert(tups, dictionary)) 


#14 write program to extract digits from Tuple list 
from itertools import chain 
test_list = [(15, 3), (3, 9), (1, 10), (99, 2)] 
print("The original list is : " + str(test_list)) 
temp = map(lambda ele: str(ele), chain.from_iterable(test_list)) 
res = set() 
for sub in temp: 
    for ele in sub: 
        res.add(ele) 
print("The extrated digits : " + str(res))  

#15 write a program to Remove Tuples of Length K Using list comprehension 
  
test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)] 
print("The original list : " + str(test_list)) 
K = 1
res = [ele for ele in test_list if len(ele) != K] 
print("Filtered list : " + str(res)) 

#16 write a program to find Maximum and Minimum K elements in Tuple 
test_tup = (5, 20, 3, 7, 6, 8) 
print("The original tuple is : " + str(test_tup)) 
K = 2
test_tup = list(test_tup) 
temp = sorted(test_tup) 
res = tuple(temp[:K] + temp[-K:]) 
print("The extracted values : " + str(res))  

#17 write a program to get current date and time 
import datetime  
current_time = datetime.datetime.now()  
    
print ("Time now at greenwich meridian is : " , end = "")  
print (current_time)

#18 write a program to convert time from 12 hour to 24 hour format 
  
def convert24(str1): 
      
    # Checking if last two elements of time 
    # is AM and first two elements are 12 
    if str1[-2:] == "AM" and str1[:2] == "12": 
        return "00" + str1[2:-2] 
          
    # remove the AM     
    elif str1[-2:] == "AM": 
        return str1[:-2] 
      
    # Checking if last two elements of time 
    # is PM and first two elements are 12    
    elif str1[-2:] == "PM" and str1[:2] == "12": 
        return str1[:-2] 
          
    else: 
          
        # add 12 to hours and remove PM 
        return str(int(str1[:2]) + 12) + str1[2:8] 
  
# Driver Code         
print(convert24("08:05:45 PM"))   

#19 write a program to find the difference between two times 
  
  
# function to obtain the time in minutes form 
def difference(h1, m1, h2, m2): 
      
    # convert h1 : m1 into minutes 
    t1 = h1 * 60 + m1 
      
    # convert h2 : m2 into minutes  
    t2 = h2 * 60 + m2 
      
    if (t1 == t2):  
        print("Both are same times") 
        return 
    else: 
          
        # calculating the difference 
        diff = t2-t1 
          
    # calculating hours from difference 
    h = (int(diff / 60)) % 24
      
    # calculating minutes from difference 
    m = diff % 60
  
    print(h, ":", m) 
  
# Driver's code 
if __name__ == "__main__": 
      
    difference(7, 20, 9, 45) 
    difference(15, 23, 18, 54) 
    difference(16, 20, 16, 20) 
    
#20 write program to find yesterday, today and tomorrow 
  
# Import datetime and timedelta 
# class from datetime module 
from datetime import datetime, timedelta 
  
  
# Get today's date 
presentday = datetime.now() # or presentday = datetime.today() 
  
# Get Yesterday 
yesterday = presentday - timedelta(1) 
  
# Get Tomorrow 
tomorrow = presentday + timedelta(1) 
  
  
# strftime() is to format date according to 
# the need by converting them to string 
print("Yesterday = ", yesterday.strftime('%d-%m-%Y')) 
print("Today = ", presentday.strftime('%d-%m-%Y')) 
print("Tomorrow = ", tomorrow.strftime('%d-%m-%Y')) 



