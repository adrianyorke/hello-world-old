#!/usr/bin/env python

from __future__ import print_function

def myFunc():
    """myFunc() description."""
    return '1'

def main():
    """main() description."""
    returnVal = myFunc()
    print(myFunc.__doc__)
    print(main.__doc__)
    print('returnVal =', returnVal)

    # Defining Dictionaries (key/value pairs)
    d = {"server":"mpilgrim", "database":"master"}
    print(type(d))
    print(d["server"])
    print(d["database"])

    # Defining Lists
    li = ["a", "b", "mpilgrim", "z", "example"]
    print(type(li))
    print(li[0])
    print(li[4])

    # Slicing a List
    print(li[1:3])

    # Adding Elements to a List
    li.append("new")
    print(li)

    # pop
    print(li.pop())
    print(li.pop())
    print(li.pop())
    print(li)

    # Defining Tuples
    t = ("a", "b", "mpilgrim", "z", "example")
    print(type(t))
    print(t)
    
if __name__ == '__main__':
    main()
