def mat(k):
    k = ''.join(dict.fromkeys(k.upper().replace('J', 'I')))
    abc = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    k += ''.join(c for c in abc if c not in k)
    return [list(k[i:i+5]) for i in range(0, 25, 5)]

def pos(m, ch):
    for i in range(5):
        if ch in m[i]:
            return i, m[i].index(ch)

def pairs(t):
    t = t.upper().replace('J','I').replace(' ','')
    i, out = 0, []
    while i < len(t):
        a = t[i]
        b = t[i+1] if i+1 < len(t) and t[i] != t[i+1] else 'X'
        out.append((a, b))
        i += 2 if b != 'X' else 1
    if len(out[-1]) == 1:
        out[-1] = (out[-1][0], 'X')
    return out

def playfair(msg, key, mode='e'):
    m = mat(key)
    res = ''
    for a, b in pairs(msg):
        r1, c1 = pos(m, a)
        r2, c2 = pos(m, b)
        if r1 == r2:
            res += m[r1][(c1+1)%5] + m[r2][(c2+1)%5] if mode == 'e' else m[r1][(c1-1)%5] + m[r2][(c2-1)%5]
        elif c1 == c2:
            res += m[(r1+1)%5][c1] + m[(r2+1)%5][c2] if mode == 'e' else m[(r1-1)%5][c1] + m[(r2-1)%5][c2]
        else:
            res += m[r1][c2] + m[r2][c1]
    return res

text = input("txt: ")
key = input("key: ")
mode = input("m: ")
print("output: ", playfair(text, key, mode))
