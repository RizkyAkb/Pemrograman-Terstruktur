import random
def shuffle_string(x, n):
    kata_acak = []
    i = 0
    while i < n:
        result = ''.join(random.sample(x,len(x)))
        if result not in kata_acak:
            kata_acak.append(result)
            i+=1
            
    print (kata_acak)

shuffle_string("aku", 2)
shuffle_string("aku", 3)
shuffle_string("aku", 4)

