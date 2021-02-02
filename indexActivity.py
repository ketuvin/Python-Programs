

D1 = 'He likes to wink, he likes to drink'
D2 = 'He likes to drink, and drink, and drink'
D3 = 'The thing he likes to drink is ink'
D4 = 'The ink he likes to drink is pink'
D5 = 'He likes to wink and drink pink ink'
doc = [D1,D2,D3,D4,D5]

freq = []

for line in doc:
    list = line.lower().split()
    len(list)
for word in list:
    freq.append(list.count(word))

print(str(zip(list, freq)))
