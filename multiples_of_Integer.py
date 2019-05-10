def multiples(n):
    '''takes n as integer and finds all first 10 multiples of n'''
    for i in range (1,11):
        result = n*i
        print (n,'X', i, '=', result)
'''Calling the function with a sample integer, n =5'''
multiples(5)