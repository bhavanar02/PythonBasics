def sum(int_array):

    sum = 0
    i = 0

    for i in int_array:

        sum += i

    return(sum)

int_array = []
int_array = [1, 2, 3, 4, 5]
ans = sum(int_array)
print('Sum of the array is: ', ans)
