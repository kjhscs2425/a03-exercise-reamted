'''
Write a function `print_multiples` with one parameters `n`.

When called, your function should print out ALL of the multiples of `n` between 0 and 100 (including both 0 and 100), and NO OTHER numbers.

Call your function for `n = 2`, `n = 3`, `n = 5`, and `n = 12`.
'''




#actually asighment
for e in range(1, 100):
    n=e
    for i in range(101):
        x = i
        if x % n == 0:
            print(i)


#fizzbuzz 
for n in range(1, 100):
    if n % 15 ==0:
        print("fizzbuzz")
    if n % 5 ==0:
        print("fizz")
    if n % 3 ==0:
        print("buzz")
    