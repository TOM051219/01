w = input('your weight: ')
w = float(w)
h = input('your height(cm): ')
h = float(h)
e = h / 100
t = w / e / e
print('your BMI: ', t)
if t < 18.5:
	print('health risk minimal')
elif t >= 18.5 and t <=24.9:
    print('heaith risk minial')
elif t >= 25 and t <=29.9:
    print('health risk increased')
elif t >= 30 and  t <= 34.9:
	print('heaith risk high')
elif t >=35 and t <= 39.9:
	print('heaith risk very high')
elif t >= 40 and t <= 50:
	print('health risk extremely high')
else:
	print('error')