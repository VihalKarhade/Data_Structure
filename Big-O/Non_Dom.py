# Drop non dominant term

# O(n^2 + n)   
# where n^2 is the dominant term and n is not dominant term

def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

    for k in range(n):
        print(i)

print_items(10)