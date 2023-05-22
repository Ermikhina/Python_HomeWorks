year = int(input("Введите год "))
n = "Yes" if (year%4==0 and year%100!=0) or year%400==0 else "Not"
print (n)