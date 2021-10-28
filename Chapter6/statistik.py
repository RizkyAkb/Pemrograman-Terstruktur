def sum(*n):
    jml = 0
    for i in n:
        jml += i
    return jml

def avg(*n):
    hitung = 0
    for i in n:
        hitung += 1
        rata = sum(*n) / hitung
    return rata

def maks(*n):
    max = n[0]
    for i in n:
        if (i > max):
            max = i
    return max

def min(*n):
    minim = n[0]
    for i in n:
        if (i < minim):
            minim = i
    return minim

