def digital_root(n):
    if n<10 :
         return n
    return digital_root( n%10 + digital_root( n//10 ) )

'''n = 42
m= n%10
print(m)'''
