# Less efficient in the point of time complexity

# O(n^2) is a loop within a loop i.e. nested loop



def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

print_items(10)