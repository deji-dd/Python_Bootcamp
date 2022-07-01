s = set()
s.add(1)
s.add(2)
s.clear()  # removes all the element in a set
s = {1, 2, 3}
sc = s.copy()  # copies all the elements in a given set
s.add(4)
s.difference(sc)  # returns the difference between 2 sets
s1 = {1, 2, 3}
s2 = {1, 4, 5}
s1.difference_update(s2)  # removes the elements that appear in both sets
s.discard(2)  # removes a given element of a set
s3 = {1, 2, 3}
s4 = {1, 3, 5}
s3.intersection(s4)  # returns elements that appear in both sets
s3.isdisjoint(s4)  # returns if there's a null intersection or nut

