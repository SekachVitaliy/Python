""""
a = int(input()) #Рубли 1го товара
b = int(input()) #Копейки 1го товара
c = int(input()) #Рубли 2го товара
d = int(input()) #Копейки 2го товара
cost1 = a * 100 + b
cost2 = c * 100 + d
totalCost = cost1 + cost2
print(totalCost // 100, totalCost % 100)
"""
n = int(input())
print(n % 256)