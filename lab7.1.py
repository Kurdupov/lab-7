a=input('Введіть числа')
set_a=set(a)
b={'0','1','2','3','4','5','6','7','8','9'}
set_b=set(b)
diff_set = set_b.difference(set_a)
sort=sorted(diff_set)
print(sort)