import re

statement = "To database@g.msuiit.edu.ph Sat jan 5 09:14:16 2018"
finder1 = re.findall ('d.+?h',statement)
finder2 = re.findall (r'[\w\.-]+@[\w\.-]+',statement)
finder3 = re.findall ('\s.+?h',statement)
finder4 = re.findall ('[\w.]+@.+?h',statement)

print(finder1)
print(finder2)
print(finder3)
print(finder4)
