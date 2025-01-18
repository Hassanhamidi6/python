'''
This is the small python module for backend functionality
'''

def union(s1:set,s2:set)->set:
    return s1.union(s2)

def intersection(s1:set,s2:set)->set:
    return s1.intersection(s2)

def symmetric_difference(s1:set,s2:set)->set:
    return s1.symmetric_difference(s2)

def difference(s1:set,s2:set)->set:
    return s1.difference(s2)


