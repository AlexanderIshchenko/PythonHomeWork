# 2. Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.



def simple_mult(n):
    result = set()
    while n % 2 == 0: 
        result.add(2)
        n = n / 2 
    for i in range(3, int(n**0.5) + 1, 2): 
         while n % i == 0: 
            result.add(i) 
            n = n / i 
    if n > 2: 
      result.add(int(n)) 
    return result
 
n = 15
print(simple_mult(n))