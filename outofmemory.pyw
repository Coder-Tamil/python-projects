import random
for i in range(1000):
    f=open("junk{}".format(i),'w')
    for w in range(100):
        f.write(str(random.randint(345354,56755786867867)))
