import geo.utils as utils

# a=3, b=4일 때 빗변의 길이 계산
a, b = 3, 4
c = utils.pythagoras(a, b)
print('c =', c)

# 반지름이 10인 원의 넓이 계산
r = 10
area = utils.circle(r)
print('area =', area)
