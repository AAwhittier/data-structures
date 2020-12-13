
def head_sum_up_to(n):
    if n < 1:
        return 0
    else:
        return head_sum_up_to(n - 1) + n

n = int(input('Enter a number n: '))
print(head_sum_up_to(n))


def tail_sum_up_to(n):
    if n < 1:
        return n

    return tail_sum_up_to(n - 1) + n

n = int(input('Enter a number n: '))
print(tail_sum_up_to(n))

