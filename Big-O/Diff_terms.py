#  Different terms for input


# for loop followed by for loop with each running with n times 
# O(n)
def print_items(a,b):
    for i in range (a):   #runs a times
        print(i)
    for j in range (b):   #runs b times
        print(j)

print_items(8,10)



# O(n*n)

def print_items(a,b):
    for i in range(a):
        for j in range(b):
            print(i,j)

print_items(8,10)