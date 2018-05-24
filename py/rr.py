crds = []

import os
def fill(q,x):
    i=1
    while i<=q:
        crds.append(x)
        i+=1
i=1
c=2
while i<=9:
    if c == 5:
        c+=1
        continue
    fill(4,c)
    c+=1
    i+=1

#print(crds)
