# Pointers check whether the number is points to the same id/address or not
# Integers are immutable

num1 = 11

num2 = num1

print('Before num2 value is updated:')        
print('num1 = ',num1)                          #num1 =  11
print('num2 = ',num2)                          #num1 =  11

print("\nnum1 is points to",id(num1))          #num1 is points to 140713185590008
print("num2 is points to",id(num2))            #num2 is points to 140713185590008


num2 = 22

print('\nAfter num2 value is updated:')
print('num1 = ',num1)                          #num1 =  11
print('num2 = ',num2)                          #num2 =  22

print("\nnum1 is points to",id(num1))          #num1 is points to 140713185590008
print("num2 is points to",id(num2))            #num2 is points to 140713185590360




dict1 = {
    'value': 11
}

dict2 = dict1

print('\nBefore value is updated:')
print('dict1 =',dict1)                        #dict1 = {'value': 11}
print('dict2',dict2)                          #dict2 {'value': 11}

print('\ndict1 is points to',id(dict1))        #dict1 is points to 1710363781440
print('dict2 points to ',id(dict2))            #dict2 points to  1710363781440


dict2={
  'value': 22
}
print('\nAfter value is updated:')
print('dict1 =',dict1)                        #dict1 = {'value': 11}
print('dict2',dict2)                          #dict2 {'value': 22}

print('\ndict1 is points to',id(dict1))      #dict1 is points to 2495223376192
print('dict2 points to ',id(dict2))          #dict2 points to  2495223377088
