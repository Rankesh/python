# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.

#version1
#def find_element (p,t):
#	i = 0
#	while i < len(p):
#		if p[i] == t:
#			return i
#		i =+ 1
#	return -1

#version2
#def find_element(p,t):
#	i=0
#	for e in p:
#		if e == t:
#			return p.index(e)
#		i += 1
#	return -1

#version3
#def find_element(p,t):
#	if t in p:
#		return p.index(e)
#	else:
#		return -1

#version4
#def find_element(p,t):
#	if t not in p:
#		return -1
#	return p.index(t)


def test_element (list, element):
    position = -1
    result = -1
    for e in list:
        position += 1
        if element == e:
            result =  position
            break
    return result
    

def find_element (list, element):
    if test_element(list, element) == -1:
        return -1
    else:
        return test_element(list, element)



print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'gamma')
#>>> -1