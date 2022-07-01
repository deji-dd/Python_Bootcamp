from collections import Counter
from collections import defaultdict
from collections import namedtuple

mylist = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
print(Counter(mylist))  # Module Counter counts the number of unique objects in a list
mylist1 = ['a', 'a', 10, 10, 10]
print(Counter(mylist1))
print(Counter('aaaaabbbbbbbcccccddddd'))
sentence = 'how many times does each word show up in this sentence with a word'
print(Counter(sentence.split()))
letters = 'aaaaabbbbbcccccddddddd'
c = Counter(letters)
print(c.most_common(2))  # Returns the most common object in a string/list...etc
print(list(c))
d = defaultdict(lambda: 0)  # deafultdict assigns a default value to keys that are not already in your dictionary
d['correct'] = 100
print(d['correct'])
print(d['tree'])
Dog = namedtuple('Dog', ['age', 'breed', 'name'])  # namedtuple assigns names to objects in a tuple
sammy = Dog(5, 'Husky', 'Sam')
print(sammy.breed)
# is also the same as:
print(sammy[1])
