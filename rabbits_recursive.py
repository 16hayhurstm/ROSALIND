def rabbit_recursive(n):
    k = 3
    if n <= 1:
        return n
    else:
        return rabbit_recursive(n - 1) + 3 * rabbit_recursive(n - 2)


print(rabbit_recursive(29))
