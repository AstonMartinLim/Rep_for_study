str1 = 'Hello, welcome to my world!'

# index
r1 = str1.index ('welcome')
print(r1)
# будет искать 'е' между 5 и 10 индексами
r2 = str1.index('e', 5, 10)
r3 = str1.index('my w', 0, -1)
print(r2)
print(r3)
# If the value is not found, the find() method returns -1,
# but the index() method will raise an exception:
print(str1.find('q'))
print(str1.index('q'))
