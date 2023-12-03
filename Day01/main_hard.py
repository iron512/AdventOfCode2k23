import re
t=open("i").read()
for i, v in enumerate(['one','two','three','four','five','six','seven','eight','nine'],1):
    t=t.replace(v,v+str(i)+v)
print(sum([int(i[0])*10+int(i[-1]) for i in[re.findall("\\d",l) for l in t.split("\n")]]))

# 10:31 - 10:38
# 10:41 - 10:54