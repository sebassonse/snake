import numpy as np

fieldSize = 30

M_numpy = np.zeros((10, 10))
print(M_numpy)

a = [[20, 40], [60, 60]]


M = np.zeros((playing_field_size, playing_field_size))
for i in range(1, len(snake_placement_list)):
    M[np.floor_divide(snake_placement_list[i], snake_size)] = 5
M[np.floor_divide(snake_placement_list[0], snake_size)] = 6
M[np.floor_divide(apple_placement, snake_size)] = 10
