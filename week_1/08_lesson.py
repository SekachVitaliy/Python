# Дано положительное двузначное число. Найдите число десятков в нем.
n = int(input())
first_num = n // 100
second_num = n // 10 % 10
third_num = n % 10
print(first_num + second_num + third_num)
