# Finding out the largest and the smallest number in a list of a number

numbers = [56, 45, 78, 99, 100, 43, 1, 78, 2, 3]

def largest(list):
    max = list[0]

    for i in range(1,len(list)) :
        if list[i] > max:
            max = list[i]

    return max

print(largest(numbers))

def smallest(list):
    min = list[0]

    for i in range(1,len(list)) :
        if list[i] < min:
            min = list[i]

    return min

print(smallest(numbers))