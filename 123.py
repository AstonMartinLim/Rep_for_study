# Write a Python program that will return true if the two given integer
# values are equal or their sum or difference is 5

int1 = int (input ('Type an integer 1: '))
int2 = int (input ('Type an integer 2: '))

##sum = int1 + int2
##dif = int1 - int2
##
##if int1 == int2 or sum == 5 or dif == 5 or dif == -5:
##    print ('True')
##else: print ('False')

# Site solution`s
def test_number5(int1, int2):
   if int1 == int2 or abs(int1-int2) == 5 or (int1+int2) == 5:
       return True
   else:
       return False
print(test_number5(int1, int2))
