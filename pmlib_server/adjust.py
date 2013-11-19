f= open("obt_values.txt", "r")
x= f.readlines()


for i in xrange(len(x)):
        v2=2.0
        if i != 4: v1=0.5
        else: v1=0.6
        [l, x2, x1]= x[i].split("\t")
        a= (v2 - v1) / (float(x2) - float(x1))
        b= v2 - (float(x2) * a)
        print "%s\t%f\t%f" % (l, a, b)

