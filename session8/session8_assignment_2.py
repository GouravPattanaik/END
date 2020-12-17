# write a program to reverse a list 
def reverse(lst): 
    new_lst = lst[::-1] 
    return new_lst
	
# write a program to find sum of elements in list
list1 = [11, 5, 17, 18, 23]
total = sum(list1)
print("Sum of all elements in given list: ", total)

# write a program to find the largest number in a list 
list1 = [10, 20, 4, 45, 99] 
list1.sort() 
print("Largest element is:", list1[-1]) 

# write a program to print Even Numbers in a List 
list1 = [10, 21, 4, 45, 66, 93] 
for num in list1: 
    if num % 2 == 0: 
       print(num, end = " ") 
       
# write a program to print negative Numbers in given range 
start, end = -4, 19
for num in range(start, end + 1): 
    if num < 0: 
        print(num, end = " ") 
        
# write a program to remove empty List from List using list comprehension 
test_list = [5, 6, [], 3, [], [], 9] 
print("The original list is : " + str(test_list)) 
res = [ele for ele in test_list if ele != []] 
print ("List after empty list removal : " + str(res)) 

# write a  program to remove empty tuples from a list of tuples 
def Remove(tuples): 
    tuples = filter(None, tuples) 
    return tuples 
  
# Driver Code 
tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'),  
          ('krishna', 'akbar', '45'), ('',''),()] 
print Remove(tuples)

# write a program to break a list into chunks of size N
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]  
n = 4 
x = [l[i:i + n] for i in range(0, len(l), n)]  
print(x)

# write a program to find the frequency of words present in a string  
  
test_str = 'times of india times new india express'
print("The original string is : " + str(test_str)) 

res = {key: test_str.count(key) for key in test_str.split()} 
print("The words frequency : " + str(res))

# write a program to accept a string if it contains all vowels
def check(string): 
  if len(set(string).intersection("AEIOUaeiou"))>=5: 
    return ('accepted') 
  else: 
    return ("not accepted") 
  
if __name__=="__main__": 
  string="helloworld"
  print(check(string)) 
  

# write a program to rotate string left and right by d length  
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
    

# write a program to convert key-values list to flat dictionary 

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


# write a program to convert into dictionary 
def Convert(tup, di): 
    for a, b in tup: 
        di.setdefault(a, []).append(b) 
    return di 
      
tups = [("A", 10), ("B", 20), ("C", 30),  
     ("D", 40), ("E", 50), ("F", 60)] 
dictionary = {} 
print (Convert(tups, dictionary)) 


# write program to extract digits from Tuple list 
from itertools import chain 
test_list = [(15, 3), (3, 9), (1, 10), (99, 2)] 
print("The original list is : " + str(test_list)) 
temp = map(lambda ele: str(ele), chain.from_iterable(test_list)) 
res = set() 
for sub in temp: 
    for ele in sub: 
        res.add(ele) 
print("The extrated digits : " + str(res))  

# write a program to Remove Tuples of Length K Using list comprehension 
  
test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)] 
print("The original list : " + str(test_list)) 
K = 1
res = [ele for ele in test_list if len(ele) != K] 
  
# printing result  
print("Filtered list : " + str(res)) 

# write a program to find Maximum and Minimum K elements in Tuple 
test_tup = (5, 20, 3, 7, 6, 8) 
print("The original tuple is : " + str(test_tup)) 
K = 2
test_tup = list(test_tup) 
temp = sorted(test_tup) 
res = tuple(temp[:K] + temp[-K:]) 
print("The extracted values : " + str(res))  

