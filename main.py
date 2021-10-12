import math
def prim(n):
    """
    :param n: nr intreg
    :return: daca nr este prim sau nu
    """
    if n == 1:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


def get_longest_all_primes(lst: list[int]) -> list[int]:
    """
    aflam cea mai mare subsecventa de nr prime
    :param lst: lista cu nr intregi citita de la tastatura
    :return: subsecventa cea mai lunga de nr prime
    """
    nr=0
    mx=-1
    for i in range(len(lst)):
        if prim(lst[i]) == True:
            nr=nr+1
        else:
            if nr > mx:
                mx=nr
                pozmx=i
            nr=0
    if nr > mx:
        mx=nr
        pozmx=i+1
    return lst[pozmx-mx:pozmx]


def test_get_longest_all_primes():
    """
    testam functia get_longest_all_primes
    :return: daca functia merge
    """
    assert get_longest_all_primes([2,3,5,4,5,6,7,5,]) == [2,3,5]
    assert get_longest_all_primes([2,4,5,7,7,5,6,7,2]) == [5,7,7,5]
    assert get_longest_all_primes([2,4,5,7,6,3,5,2,7]) == [3,5,2,7]

#test_get_longest_all_primes()


def get_longest_prime_digits(lst: list[int]) -> list[int]:
    """

    :param lst: lista cu nr intregi pe care o primim
    :return: subsecventa maxima de nr care au toate cifrele prime
    """
    nr=0
    mx=-1
    ok = True
    for i in range(len(lst)):
        ok = True
        x = lst[i]
        while x!=0:
            if prim(x%10) == False:
                ok = False
            x=x//10
        if ok == True:
            nr = nr + 1
        else:
            if nr > mx:
                mx=nr
                pozmx=i
            nr=0
    if nr > mx:
        mx=nr
        pozmx=i+1

    return lst[pozmx-mx:pozmx]


def test_get_longest_prime_digits():
    """
    testam functia get_longest_prime_digits
    :return: daca functia merge sau nu
    """
    assert get_longest_prime_digits([235,112,7757,737,357,725,212,222,325]) == [7757, 737, 357, 725]
    assert get_longest_prime_digits([7773,737,355,122,235,352,247,357]) == [7773, 737, 355]
    assert get_longest_prime_digits([777,737,2435,3124,456,333,5237,7575]) == [333, 5237, 7575]

#test_get_longest_prime_digits()


def citireLista():
    """
    citim o lista de la tastatura
    :return: lista citita

    """
    l = []
    n = int(input("Dati nr de elemente: "))
    for i in range(n):
        l.append(int(input("l[" + str(i) + "]=")))
    return l


def print_menu():
    print("Alegeti optiunea:\n"
          "1.Afisati cea mai lunga subsecventa de nr prime a unei liste de numere\n"
          "2.Afisati cea mai lunga subsecventa de nr care au toate cifrele prime a unei liste de numere\n"
          "3.Afisati cea mai lunga subsecventa de patrate perfecte\n")


def is_perfect_square(x):
    """
    verifica daca un nr este patrat perfect
    :param x: nr int
    :return: true daca e patrat perfect , fals in caz contrar
    """
    if int(math.sqrt(x)) * (math.sqrt(x)) == x:
        return True
    else:
        return False


def get_longest_all_perfect_squares(lst: list[int]) -> list[int]:
    """
    det subsecventa de patrate perfecte maxima
    :param lst: lista de numere intregi
    :return: subsecventa maxima de patrate perfecte
    """
    mx=-1
    nr=0
    for i in range(len(lst)):
        if is_perfect_square(lst[i]):
            nr = nr + 1
        else:
            if nr > mx:
                pozmx=i
                mx=nr
            nr = 0
    if nr > mx:
        pozmx = i+1
        mx = nr
    return lst[pozmx-mx:pozmx]


def test_get_longest_all_perfect_squares():
    assert get_longest_all_perfect_squares([4,9,16,5,4,36,11,15,81,16]) == [4,9,16]
    assert get_longest_all_perfect_squares([15,11,4,25,81,5,9,16,36,25,11]) == [9,16,36,25]
    assert get_longest_all_perfect_squares([4,9,15,36,17,16,25,9]) == [16,25,9]


def main():
    l=[]
    while True:
        print_menu()
        optiune = input("Dati optiunea:\n")
        if optiune == "1":
            print("Introducesti lista:")
            l=citireLista()
            print(get_longest_all_primes(l))
        if optiune == "2":
            print("Introducesti lista:")
            l = citireLista()
            print(get_longest_prime_digits(l))
        if optiune == "3":
            print("Introduceti lista:")
            l=citireLista()
            print(get_longest_all_perfect_squares(l))
        else:
            print("optiunea nu exista")


main()
