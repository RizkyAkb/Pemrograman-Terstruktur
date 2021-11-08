def mahal(x):
    maks = max(x.values())
    for x,y in x.items():
        if y == maks:
            return x
def rata2(x):
    rata = sum(x.values())/len(x)
    return rata

buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
print(buah)
print('Termahal   :',mahal(buah))
print('Harga rata2:',rata2(buah))

    
