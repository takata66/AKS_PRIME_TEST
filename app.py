import math

# Функция для проверки, является ли число n степенью целого числа
def is_power_of_integer(n):
    for b in range(2, int(math.log2(n)) + 2):  # Перебираем значения b от 2 до log2(n) + 1
        a = int(round(n**(1/b)))  # Округляем значение n^(1/b)
        if a**b == n:  # Проверяем, если a^b равно n
            return True  # Если равно, возвращаем True
    return False  # Если ни одно значение a^b не равно n, возвращаем False

# Функция для нахождения наибольшего общего делителя (НОД) двух чисел
def gcd(a, b):
    while b:  # Пока b не равно 0
        a, b = b, a % b  # Присваиваем a значение b, а b значение a % b
    return a  # Возвращаем НОД

def euler_phi(n):
    #Вычисление функции Эйлера для числа n
    count = 0
    for i in range(1, n):
        if gcd(i, n) == 1:
            count += 1
    return count

# Функция для нахождения мультипликативного порядка числа a по модулю r
def multiplicative_order(a, r):
    if gcd(a, r) != 1:  # Если НОД(a, r) не равен 1
        return -1  # Возвращаем -1 (порядок не существует)
    k = 1
    ak = a % r  # Начальное значение ak = a % r
    while ak != 1:  # Пока ak не равно 1
        ak = (ak * a) % r  # ak = (ak * a) % r
        k += 1  # Увеличиваем k на 1
    return k  # Возвращаем значение k

# Функция для проверки многочлена на условие (x + a)^n ≡ x^n + a (mod (x^r - 1, n))
def check_polynomial(n, r):
    max_a = int(math.sqrt(euler_phi(r)) * math.log2(n))  # Вычисляем максимальное значение a как sqrt(r) * log2(n)
    for a in range(1, max_a + 1):  # Проверяем значения a от 1 до max_a
        lhs = pow(a + 1, n, n)  # Вычисляем левую часть (a + 1)^n % n
        rhs = (pow(a, n, n) + 1) % n  # Вычисляем правую часть (a^n % n + 1) % n
        if lhs != rhs:  # Если левая часть не равна правой
            return False  # Возвращаем False (n не является простым)
    return True  # Если все условия выполнены, возвращаем True

# Основная функция для проверки, является ли число n простым с использованием алгоритма AKS
def is_prime_aks(n):
    if n < 2:  # Если n меньше 2, возвращаем False (число меньше 2 не является простым)
        return False
    if is_power_of_integer(n):  # Если n является степенью целого числа, возвращаем False
        return False

    r = 2
    log2n_squared = math.log2(n)**2  # Вычисляем log2(n)^2
    while True:
        if gcd(n, r) == 1 and multiplicative_order(n, r) > log2n_squared:  # Если НОД(n, r) == 1 и порядок n по модулю r > log2(n)^2
            break  # Выходим из цикла
        r += 1  # Увеличиваем r на 1

    for a in range(2, min(r + 1, n)):  # Проверяем значения a от 2 до min(r+1, n)
        if 1 < gcd(a, n) < n:  # Если НОД(a, n) больше 1 и меньше n
            return False  # Возвращаем False (n не является простым)

    if n <= r:  # Если n меньше или равно r
        return True  # Возвращаем True (n - простое число)

    return check_polynomial(n, r)  # Проверяем многочлен, если условие выполняется, возвращаем True

# Пример использования:
n = 1000000
print(f"{n} is prime: {is_prime_aks(n)}")  # Проверяем число 1000367
