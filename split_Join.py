import re
text="Hello my? name is Artem Tupota. I live in Doiynska!"
sentens=re.split("[.\?\!]",text)
print(sentens)
list ="\n".join(sentens)
print(list)