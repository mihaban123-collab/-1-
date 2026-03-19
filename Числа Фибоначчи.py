nums = list(map(int, input().split()))
prev1, prev2 = 1, 0
s = 0
first_fib = []
while s < nums[0]:
    s = prev1 + prev2
    prev2 = prev1
    prev1 = s

if s > nums[1]:
    print('В заданном диапазоне нет чисел Фибоначчи')
else:
    while s <= nums[1]:
        first_fib.append(s)
        s = prev1 + prev2
        prev2 = prev1
        prev1 = s
    print(' '.join(map(str, first_fib)))
        
