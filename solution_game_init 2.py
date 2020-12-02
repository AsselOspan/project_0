import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)
random_array = np.random.randint(1,101, size=(1000))

count_ls = []

def game_core(number, step=10):
    count = 0
    predict = 0
    while number != predict:
        count+=1
        if number > predict:
            predict+=step
        else:
            predict-=1
    return count

for number in random_array:
    count_ls.append(game_core(number))

# print(random_array[0:15])
# print(np.mean(count_ls))
count_ls.sort()
print(count_ls)

cnt = [x for x in range(len(count_ls))]

plt.plot(cnt, count_ls)
plt.show()




