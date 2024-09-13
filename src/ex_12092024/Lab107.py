#Ordereddict: same like dictionary, but it remembers insertion order
from collections import OrderedDict, defaultdict

d=OrderedDict()
d["banana"]=4
d["apple"]=8
d["pear"] = 12

print(d)

dd=defaultdict(int)
print(dd)