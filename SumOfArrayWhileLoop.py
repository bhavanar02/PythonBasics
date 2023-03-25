def sum(int_array):

    sum = 0
    i = 0

    while(i < len(int_array)):

        sum += int_array[i]
        i+=1

    return(sum)

int_array = []
int_array = [6, 8, 12, 2, 1]
ans = sum(int_array)
print('Sum of the array is: ', ans)
