# fizzbuzz with no ifs, no modulo??? should still be easily readable code?????
# for high performance, modulo with ints should be fine

# questions to ask (solution depending on answers):
# is this code going to be run many times a day/hour/second? (performance)
# is this code going to be run on different numbers? (scalability) if so, are the numbers going to be much bigger? (performance, memoryIfRecursion)
# do you anticipate scaling run times per unit of measurement, scaling numbers, both or neither? (performance, scalability)
# do I want to showcase clean code writing?
# do I want to showcase knowledge of particular programming language tricks?
# do I want to showcase ability to write modular and scalable code?
# do I want to showcase ability to implement a solution quickly and effectively?

import time

FIZZ = 3
BUZZ = 5
FIZZBUZZ = FIZZ * BUZZ
MAX_NUMBER = 100
FIZZ_WORD = "fizz"
BUZZ_WORD = "buzz"
FIZZBUZZ_WORD = "fizzbuzz"


def main():
    # should use decorators for timing
    time_list = []
    time_start = time.time()
    fizzbuzz_branchless_divisionless_readable()
    time_list.append(time.time() - time_start)

    time_start = time.time()
    fizzbuzz_branchless_divisionless_readable_scalable_list()
    time_list.append(time.time() - time_start)

    time_start = time.time()
    fizzbuzz_branchless_divisionless_readable_scalable()
    time_list.append(time.time() - time_start)

    time_start = time.time()
    fizzbuzz_loop()
    time_list.append(time.time() - time_start)

    time_start = time.time()
    fizzbuzz_small_loop()
    time_list.append(time.time() - time_start)

    # time_start = time.time()
    # fizzbuzz_recursion(MAX_NUMBER)
    # print("fizzbuzz_recursion(MAX_NUMBER): ", time.time() - time_start)

    print("fizzbuzz_branchless_divisionless_readable(): ", time_list[0])
    print("fizzbuzz_branchless_divisionless_readable_scalable_list(): ", time_list[1])
    print("fizzbuzz_branchless_divisionless_readable_scalable(): ", time_list[2])
    print("fizzbuzz_loop(): ", time_list[3])
    print("fizzbuzz_small_loop(): ", time_list[4])
    # results are very inconsistent - why? prob cause pc is doing other things too?


# ----------- no ifs, no division, no modulo, readable code
# drawback - not scalable without editing code
def fizzbuzz_branchless_divisionless_readable():
    print("fizzbuzz_branchless_divisionless_readable")
    number = 0
    for _ in range(0, MAX_NUMBER // FIZZBUZZ):
        number = loop_15(number)
    first_10(number)

    '''
    # to make scalable, end the last n<15 iterations with classic ifs
    for i in range(0, MAX_NUMBER % FIZZBUZZ):
        pass
        # classic ifs and stuff
    '''


def loop_15(number):
    number = first_10(number)
    number += 1
    print(number)  # 11
    number += 1
    print("fizz")  # 12
    number += 1
    print(number)  # 13
    number += 1
    print(number)  # 14
    number += 1
    print("fizzbuzz")  # 15
    return number


def first_10(number):
    number += 1
    print(number)  # 1
    number += 1
    print(number)  # 2
    number += 1
    print("fizz")  # 3
    number += 1
    print(number)  # 4
    number += 1
    print("buzz")  # 5
    number += 1
    print("fizz")  # 6
    number += 1
    print(number)  # 7
    number += 1
    print(number)  # 8
    number += 1
    print("fizz")  # 9
    number += 1
    print("buzz")  # 10
    return number


# ----------- no ifs, no division, no modulo, readable code
# drawback - uses list for all numbers, might have memory problems at very high numbers
# drawback - must be modified to use different divisors
def fizzbuzz_branchless_divisionless_readable_scalable_list():
    print("fizzbuzz_branchless_divisionless_readable_scalable_list")
    number = 0
    list_to_print = []
    for _ in range(0, (MAX_NUMBER // FIZZBUZZ) + 1):
        number, list_to_print = add_15_to_list(number, list_to_print)
    for i in range(0, MAX_NUMBER):
        print(list_to_print[i])


def add_15_to_list(number, list_to_print):
    number += 1
    list_to_print.append(number)  # 1
    number += 1
    list_to_print.append(number)  # 2
    number += 1
    list_to_print.append(FIZZ_WORD)  # 3
    number += 1
    list_to_print.append(number)  # 4
    number += 1
    list_to_print.append(BUZZ_WORD)  # 5
    number += 1
    list_to_print.append(FIZZ_WORD)  # 6
    number += 1
    list_to_print.append(number)  # 7
    number += 1
    list_to_print.append(number)  # 8
    number += 1
    list_to_print.append(FIZZ_WORD)  # 9
    number += 1
    list_to_print.append(BUZZ_WORD)  # 10
    number += 1
    list_to_print.append(number)  # 11
    number += 1
    list_to_print.append(FIZZ_WORD)  # 12
    number += 1
    list_to_print.append(number)  # 13
    number += 1
    list_to_print.append(number)  # 14
    number += 1
    list_to_print.append(FIZZ_WORD + BUZZ_WORD)  # 15
    return number, list_to_print


# ----------- no ifs, no division, no modulo, readable, scalable code
# drawback - must be modified to use different divisors
def fizzbuzz_branchless_divisionless_readable_scalable():
    print("fizzbuzz_branchless_divisionless_readable_scalable")
    number = 0
    for _ in range(0, MAX_NUMBER // FIZZBUZZ):
        number = loop_15(number)

    for i in range(0, MAX_NUMBER % FIZZBUZZ):
        if i % FIZZBUZZ == 0:
            print("fizzbuzz")
        elif i % FIZZ == 0:
            print("fizz")
        elif i % BUZZ == 0:
            print("buzz")
        else:
            print(i)


# -----------loop
def fizzbuzz_loop():
    print("fizzbuzz_loop")
    for i in range(1, MAX_NUMBER + 1):
        is_fizz = not (i % FIZZ)  # not 0 is true
        is_buzz = not (i % BUZZ)
        is_fizzbuzz = is_fizz and is_buzz
        if is_fizzbuzz:
            print("fizzbuzz")
        elif is_fizz:
            print("fizz")
        elif is_buzz:
            print("buzz")
        else:
            print(i)


# -----------recursion
def fizzbuzz_recursion(number):
    print("fizzbuzz_recursion")
    if number > 0:
        fizzbuzz_recursion(number - 1)

        if number % FIZZBUZZ == 0:
            print("fizzbuzz")
        elif number % FIZZ == 0:
            print("fizz")
        elif number % BUZZ == 0:
            print("buzz")
        else:
            print(number)


# ------------ no ifs in main loop
# drawback - format function might be impacting performance
# drawback - still uses modulo in main loop (but its on integer, so should be fine for performance)
def fizzbuzz_small_loop():
    print("fizzbuzz_small_loop")
    loop_list = []
    for i in range(1, FIZZBUZZ + 1):
        if not i % FIZZBUZZ:  # not 0 is true
            loop_list.append("fizzbuzz")
        elif not i % FIZZ:
            loop_list.append("fizz")
        elif not i % BUZZ:
            loop_list.append("buzz")
        else:
            loop_list.append("{}")

    for i in range(1, MAX_NUMBER + 1):
        print(loop_list[(i % FIZZBUZZ) - 1].format(i))


# ------------ branchless scalable math based fizzbuzz?


# ------------ clean code modular fizzbuzz with proper parameter passing


main()
