def comb(L):
    a = int(input("Enter the first values : "))
    b = int(input("Enter the second value : "))
    c = int(input("Enter the third value : "))
    d = int(input("Enter the Fourth value : "))

    L.append(a)
    L.append(b)
    L.append(c)
    L.append(d)

    for i in range(4):
        for j in range(4):
            for k in range(4):
                for l in range(4):

                    if (i!=j and j!=k and i!=k and i!=l and i!=k and i!=l or i == k, i == j, j == k, i == l, j == l, k == l):
                        values = [L[i],L[j],L[k],L[l]]
                        a = a + 1
                        if values == [2,3,3,1]:
                            print("Values Found Amazing !  Great Work is Going ON!")
                        print("Values Number  = ",a,values)
                        #print(a)

comb([])