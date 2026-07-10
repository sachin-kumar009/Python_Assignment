# Q1. Find Product

def Find_Prod(arr):
    prod = 1
    for i in arr:
        prod *= i
    return prod

lst = [1, 2, 3, 4, 5]
print(Find_Prod(lst))

# Q2. Find Sum

def Find_Sum(arr):
    return sum(arr)

lst = [1, 2, 3, 4, 5]
print(Find_Sum(lst))

# Q3. Count Occurrences

def findCount(arr, k):
    return arr.count(k)

lst = [3, 1, 2, 3]
print(findCount(lst, 3))

# Q4. Even Odd

def findEvenOdd(arr):
    even = sum([i for i in arr if i % 2 == 0])
    odd = sum([i for i in arr if i % 2 != 0])
    return [even, odd]

lst = [1, 2, 3, 4, 5, 6, 7]
print(findEvenOdd(lst))

# Q5. Find Number

def Find_Num(arr, num):
    if num in arr:
        return "YES"
    return "NO"

lst = [1, 2, 3, 4, 5]
print(Find_Num(lst, 2))

# Q6. Higher Age

def highAge(arr):
    return [i for i in arr if i >= 18]

lst = [11, 23, 3, 45, 72, 68]
print(highAge(lst))

# Q7. Increment List Elements

def Inc_Arr(arr):
    for i in range(len(arr)):
        arr[i] += 1
    print(arr)

lst = [1, 2, 3, 4, 5]
Inc_Arr(lst)

# Q8. Pass or Fail

def isAllPass(arr):
    if min(arr) >= 32:
        return "YES"
    return "NO"

lst = [13, 89, 45, 98, 67, 45, 54]
print(isAllPass(lst))

# Q9. Unique Color Shirt

def Unique_Shirt(arr):
    count = 0
    for i in set(arr):
        if arr.count(i) == 1:
            count += 1
    return count

lst = [2, 4, 1, 2, 3, 3]
print(Unique_Shirt(lst))

# Q10. Min and Max

def Min_Max(arr):
    return [min(arr), max(arr)]

lst = [3, 1, 4, 6, 2, 7]
print(Min_Max(lst))