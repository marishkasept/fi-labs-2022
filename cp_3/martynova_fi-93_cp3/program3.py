def Euclid_alg(a, b, advanced_flag):
    r = [a, b]
    q  = [0]
    i = 2
    while r[-1] != 0:
        q.append(r[i-2]//r[i-1])
        r.append(r[i-2]%r[i-1])
        i += 1
    d = r[-2]
    if advanced_flag == False:
        return d
    else:
        u = [1, 0]
        v = [0, 1]
        k = 2
        while len(u) != len(r)-1:
            u.append(u[k-2] - q[k-1]*u[k-1])
            v.append(v[k - 2] -  q[k-1]*v[k-1])
            k+=1
        if u[-1]*a + v[-1]*b == 1:
            print(f'The reversed for {a} exist')
            return u[-1], v[-1]
        elif v[-1]*a + u[-1]*b == 1:
            print(f'The reversed for {a} exist')
            return v[-1], u[-1]
        else:
            print(f'The reversed for {a} doesn\'t exist')
            return None, None


def linear_comparison(a, b, n):
    x = []
    d = Euclid_alg(a, n, False)
    if d == 1:
        a_reversed, n_reversed = Euclid_alg(a, n, True)
        x.append((a_reversed*b)%n)
    elif b%d != 0:
        return f'There is no solution'
    else:
        n1 = n//d
        a1 = a//d
        b1 = b//d
        temp = linear_comparison(a1, b1, n1)
        x0 = temp[0]
        for i in range(d):
            x.append(x0 + i*n1)
    return x

print(Euclid_alg(12, 27, True))
print(linear_comparison(12, 9, 27))