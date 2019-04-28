import math


def primes_list(limit):
    a = [True] * limit
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i * i, limit, i):  # Mark factors non-prime
                a[n] = False


tests = int(input())


def factorize(num):
    primes = primes_list(num)
    for prime in primes:
        if num % prime == 0:
            return prime, int(num / prime)


alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


def factorized_cipher(cipher_list, x, y):
    factorized_list = []
    cipher_list = list(cipher_list)
    if cipher_list[0] % x:
        next_element = y
    else:
        next_element = x
    for c in cipher_list:
            factorized_list.append(next_element)
            next_element = int(c / next_element)
    factorized_list.append(next_element)
    return factorized_list


for i in range(tests):
    N, L = map(int, input().split())
    cipher = [int(x) for x in input().split()]
    string_primes = []
    next_letter = None
    min_cipher = min(cipher)
    min_index = cipher.index(min_cipher)
    primes = primes_list(cipher[min_index])
    x, y = factorize(cipher[min_index])
    left = list(reversed(factorized_cipher(reversed(cipher[:min_index]), x, y)))
    right = factorized_cipher(cipher[min_index + 1:], x, y)
    string_primes = left + right
    index = dict((prime, i) for i, prime in enumerate(sorted(set(string_primes))))
    deciphered = [alphabet[index[prime]] for prime in string_primes]
    print("Case #" + str(i + 1) + ": " + "".join(deciphered))
