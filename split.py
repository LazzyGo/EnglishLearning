f = open("longman-communication-9000.txt",mode="r")
c = f.read()
f.close()
f = c.split("\n")

n=0
o=[]
for i in f:
    n += 1
    l = i.split( )
    print(str(n)+" "+l[0])
    o.append(l[0])

[print(x) for x in o]

f = open("out.txt",mode="w")
[f.write(x+"\n") for x in o]
f.close()
