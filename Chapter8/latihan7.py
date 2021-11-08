def mahal(x):
    maks = max(x.values())
    for x,y in x.items():
        if y == maks:
            return x
    

buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
print(buah)
print('Termahal:',mahal(buah))

    
