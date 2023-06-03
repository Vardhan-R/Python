import numpy as np, time

t_cost = 0.01
t_new = 0

def func(err_arr: np.ndarray, ref_arr: np.ndarray):
    global t_new
    n = err_arr.size
    if n > 1:
        i = 0
        while err_arr[n // 2] != ref_arr[i + n // 2]:
            t_new += t_cost # time.sleep(t_cost)
            i += 1
        t_new += t_cost # time.sleep(t_cost)

        r = func(err_arr[n // 2:], ref_arr[i + n // 2:])

        if i:
            l = func(err_arr[:n // 2], ref_arr[:i + n // 2])
        else:
            l = err_arr[:n // 2]

        return np.concatenate((l, r))

    t_new += t_cost * (ref_arr.size - 1) # time.sleep(t_cost * (ref_arr.size - 1))
    return np.concatenate((err_arr, ref_arr[1:]))

rng = np.random.default_rng()

ref_arr_size = 16000
err_size = 2
err_arr_size = ref_arr_size - err_size

ref_arr = rng.choice(np.arange(0, 10 ** 5), ref_arr_size, False)
index_arr = np.sort(rng.choice(np.arange(ref_arr_size), err_arr_size, False))

err_arr = np.zeros(err_arr_size, np.int0)
for i in range(err_arr_size):
    err_arr[i] = ref_arr[index_arr[i]]

# err_arr = np.array([432, 612, 979, 888, 308, 401, 835, 719, 259, 335, 876, 239])
# ref_arr = np.array([432, 612, 590, 979, 825, 888, 496, 308, 186, 401, 276, 835, 719, 259, 335, 876, 239, 753])

err_lst = list(err_arr)
t_old = 0 # time.time()
for i in range(ref_arr_size):
    try:
        if ref_arr[i] != err_lst[i]:
            err_lst.insert(i, ref_arr[i])
    except:
        err_lst.append(ref_arr[i])
    t_old += t_cost # time.sleep(t_cost)
print(ref_arr_size) # t_old / t_cost

new_arr = func(err_arr, ref_arr)
print(round(t_new / t_cost))