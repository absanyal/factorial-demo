f = open("factlen.txt", "w")

n = 1
s = 1

while (n <= 20000):
    s = s * n
    #print (s)
    p = str(n) + "\t" + str(len(str(s))) + "\n"
    print(p)
    f.write(p)
    n = n + 1
    
f.close()