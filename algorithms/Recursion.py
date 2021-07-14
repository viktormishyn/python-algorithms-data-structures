from time import sleep


def power(num, pow):
    # if pow == 1:
    #     return num
    if pow == 0:
        return 1
    return num*power(num, pow-1)


def fac(n):
    # if n == 0:
    #     return 1
    if n == 1:
        return n
    return n*fac(n-1)


def countdown(n):
    if n == 0:
        print('Done!')
    else:
        print(n, '...')
        sleep(0.3)
        countdown(n-1)
        # sleep(0.3)
        # print('foo', n)


if __name__ == '__main__':
    countdown(5)
