с1 = abs(float(input('Число 1: ')))
с2 = abs(float(input('Число 2: ')))




numerator = с1-с2
denominator = (1 + (с1*с2))

tot = numerator / denominator



print(f'{tot:.2}')