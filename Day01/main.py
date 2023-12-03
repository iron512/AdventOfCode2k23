import re
print(sum([int(i[0])*10+int(i[-1]) for i in[re.findall("\\d",l) for l in open("e").readlines()]]))


