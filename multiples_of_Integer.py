def multiples(n):
    if (n < 20 and n > 2):
        for i in range (1,11):
            result = n*i
            print (n,'X', i, '=', result)
    else:
        print ("The number is out of range")

