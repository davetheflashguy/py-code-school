import math

swallow_limit = 60 / 3
swallows_per_coconut = 1450
swallows_per_apple = 128
swallows_per_cherry = 8


print('Our research shows:')
print('\n\tWe need ', math.ceil(swallows_per_coconut / swallow_limit), 'swallows to carry a single coconut')
print('\n\tWe need ', math.ceil(swallows_per_apple / swallow_limit), 'swallows to carry a single apple')
print('\n\tWe need ', math.ceil(swallows_per_cherry / swallow_limit), 'swallows to carry a single cherry')
