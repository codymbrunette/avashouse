'''
friends = [("rolf",25),("cody",28),("anne",30),("genoa",34)]
for friend,age in friends:
    print(f"my friend {friend}, is {age} years old")
'''
'''
friend_ages = {"rolf":25,"cody":28,"anne":30,"genoa":34}
for name in friend_ages:#also friend_ages.values, and friend_ages
    print(f"my friend {name} is years old.")

'''

# Print out numbers from 1 to 100 (including 100).
# But, instead of printing multiples of 3, print "Fizz"
# Instead of printing multiples of 5, print "Buzz"
# Instead of printing multiples of both 3 and 5, print "FizzBuzz".
'''
for i in range(1,101):
    if i % 3 == 0 and i % 5 ==0:
        print("FizzBuzz")
    elif i % 3==0:
        print("Fizz")
    elif i % 5 ==0:
        print("Buzz")
    else:
        print(i)
'''
#finding prime with for loops
'''
for n in range (2,10):
    for x in range(2,n):
        if n % x ==0:
            print(f"{n} equals {x} * {n//x}")
            break
    else:
        print(f"{n} is a prime number.")
        '''
'''
names = ["rolf","bob","jen","ben","jim"]
friend_ages= [22,21,31,45,30]
age_strings = [f"my friend is {age} years old." for age in friend_ages]
lower = [name.upper() for name in names]
print (lower)

'''
#comprehension with conditionals

friends = ["raph", "genoa", "ava", "seth", "james"]
time_since_seen = [3,4,1,66,11,23]

#dictionary comprehension
long_timers = {
    friends[i]:time_since_seen[i]
    for i in range(len(friends))
    if time_since_seen[i] > 5
}

#zip function: combines two lists or more into one list
long_timers = dict([("raph", 3), ("genoa",4)])#blah blah blah
long_timers = dict(zip(friends,time_since_seen))
#print(long_timers)


#enumerate turn sequence or tuple into something else
friends = ["raph", "genoa", "ava", "seth", "james"]

for counter,friend in enumerate(friends, start = 1):
    break

list(enumerate(friends)) #prints list of tuple
#print(dict(enumerate(friends, start=1)) #prints dict of tuple
guests = [('rolf', 25), ('adam', 28), ('jen', 24)]
dict(guests)

#friends[starting point: ending point]
numbers = [1,2,3,4,5,7,2,4,34,34,54,65]
double_numbers = []
for number in numbers:
    double_numbers.append(number * 2)

double_numbers = [f"{number} is a number"  for number in numbers]

odds = [age for age in numbers if age % 2 ==1]

friends = ["rolf", "ruth", "Charlie", "Jen"]
guests = ["Jose", "bob", "Rolf", "Charlie", "michael"]

friends_lower = {n.lower() for n in friends}
guests_lower = {g.lower() for g in guests}
present_friends = friends_lower.intersection(guests_lower)
present_friends = {name.title() for name in present_friends}
#print(friends_lower.intersection(guests_lower))