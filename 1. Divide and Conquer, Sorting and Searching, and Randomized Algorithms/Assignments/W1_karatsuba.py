"""
W1 Assignment

"""


first_num = 3141592653589793238462643383279502884197169399375105820974944592
second_num = 2718281828459045235360287471352662497757247093699959574966967627
#print(karatsuba(first_num, second_num))

#q8 = 12345678
#q16 = 1234567812345678
#q32 = 12345678123456781234567812345678
#q64 = 1234567812345678123456781234567812345678123456781234567812345678
#print(karatsuba(3, 4))
#print(karatsuba(13, 40))
#print(karatsuba(95, 40))
#print(karatsuba(921, 271))
#print(karatsuba(92100, 27100))

#print(karatsuba(10, 10))
#print(karatsuba(92, 27))

#print(karatsuba(102, 7))



def is_odd(num):
    """
    :param num: single digit non-negative Integer
    :return: Boolean, true if num is odd, false otherwise

    """
    odd_set = {1, 3, 5, 7, 9}

    return int(str(num)[-1]) in odd_set


def karatsuba(x, y):
    """
    :param x: An integer with n digits
    :param y: An integer with n digits
    :return: An integer representing the product of x and y using the karatsuba method.
    """

    x_str = str(x)
    y_str = str(y)
    n = len(x_str)
    len_y = len(y_str)
    zeros_added = 0

    if n + len_y == 2:
        return x * y

    elif n < len_y:
        return karatsuba(y, x)


    #case when x has an odd number of digits
    if is_odd(n):
        x_str += '0'
        n += 1
        zeros_added += 1

    for i in range(n - len_y):
        y_str += '0'
        zeros_added += 1

    n_half = int(n / 2)

    a = int(x_str[:n_half])
    b = int(x_str[n_half:])
    c = int(y_str[:n_half])
    d = int(y_str[n_half:])

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    adbc = karatsuba(a + b, c + d) - ac - bd

    total = ac * 10 ** n + adbc * 10 ** n_half + bd
    total_str = str(total)

    if int(total_str) == 0:
        return 0
    else:
        return int(total_str[:(len(total_str) - zeros_added)])




"""
#ac
print("10*70", karatsuba(10, 70))



#bc
print("20*70", karatsuba(20, 70))
#(a+b)(c+d)
print("30*70", karatsuba(30, 70))
#ad + bc
print("ad + bc", karatsuba(30, 70) - karatsuba(20, 70) - karatsuba(10, 70) )


print("asdasdasdasdasdghjadbgjahsbgkjhabdfjhasbdgjhabdfjhbadsfjabsdkfjbad")
print('')
print(karatsuba(1020, 7000))

"""

first_num = 3141592653589793238462643383279502884197169399375105820974944592
second_num = 2718281828459045235360287471352662497757247093699959574966967627
print(karatsuba(first_num, second_num))
#Answer is: 8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184