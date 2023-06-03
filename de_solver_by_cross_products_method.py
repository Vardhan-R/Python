import matplotlib.pyplot as plt, numpy as np

ds = 0.0001
density = 13
lim = 2

x = np.linspace(-lim, lim, density)
y = np.linspace(-lim, lim, density)
y_1 = np.linspace(-lim, lim, density)

x_mesh, y_1_mesh, y_mesh = np.meshgrid(x, y_1, y)

# u = y_mesh / x_mesh + 6 * x_mesh
# v = np.log(np.abs(x_mesh)) - 2
# u = 3 * y_mesh ** 2
# v = 2 * x_mesh ** 3
# u = 2 * x_mesh + 3
# v = 2 * y_mesh - 2
# u = 3 * x_mesh ** 2 + 6 * x_mesh * y_mesh ** 2
# v = 6 * x_mesh ** 2 * y_mesh + 4 * y_mesh ** 3
# u = 3 * x_mesh ** 2 * y_mesh + 2 * x_mesh * y_mesh + y_mesh ** 3
# v = x_mesh ** 2 + y_mesh ** 2
# u = (3 * x_mesh ** 2 * y_mesh ** 3 - y_mesh ** 2 + y_mesh) / x_mesh ** 2 / y_mesh ** 3
# v = (-x_mesh * y_mesh + 2 * x_mesh) / x_mesh ** 2 / y_mesh ** 3
# u = -2 * y_mesh
# v = x_mesh

'''Euler Equations'''
a = -4
b = 6

def u(pos):
    return b * pos[1]

def v(pos):
    return a * pos[0]

def w(pos):
    return pos[0] ** 2

m_1 = np.sqrt((b * y_mesh) ** 2 + (a * x_mesh) ** 2 + x_mesh ** 4)
u_1, v_1, w_1 = b * y_mesh / m_1, a * x_mesh / m_1, x_mesh ** 2 / m_1
m_2 = np.sqrt(y_1_mesh ** 2 + 1)
u_2, v_2, w_2 = y_1_mesh / m_2, -1 / m_2, 0 / m_2

# v_x, v_y = -v, u
curr_pos = [1, 2, 5] # p_x, p_y, p_y_1
all_pos = [np.array(curr_pos, dtype=np.float64)]
# all_pos_x = [p_x]
# all_pos_y = [p_y]
# all_pos_y_1 = [p_y_1]

for i in range(400):
    cp = np.array([w(curr_pos), curr_pos[2] * w(curr_pos), -u(curr_pos) - curr_pos[2] * v(curr_pos)], dtype=np.float64)
    # m = np.sqrt(cp[0] ** 2 + cp[1] ** 2 + cp[2] ** 2)
    # m = np.sum(np.square(cp))
    cp *= ds
    curr_pos[0] += cp[0]
    curr_pos[1] += cp[1]
    curr_pos[2] += cp[2]
    all_pos.append(cp)

all_pos_arr = np.array(all_pos)

cp_x_arr = np.zeros(u_1.shape)
cp_y_arr = np.zeros(u_1.shape)
cp_z_arr = np.zeros(u_1.shape)

for i in range(density):
    for j in range(density):
        for k in range(density):
            temp = np.cross([u_1[i][j][k], v_1[i][j][k], w_1[i][j][k]], [u_2[i][j][k], v_2[i][j][k], w_2[i][j][k]])
            m_temp = np.sqrt(temp[0] ** 2 + temp[1] ** 2 + temp[2] ** 2)
            cp_x_arr[i][j][k] = temp[0] / m_temp
            cp_y_arr[i][j][k] = temp[1] / m_temp
            cp_z_arr[i][j][k] = temp[2] / m_temp

# k = np.cross(np.array([u_1, v_1, w_1]), np.array([u_2, v_2, w_2]))
# print(k.shape)

ax = plt.figure().add_subplot(projection="3d")

# ax.quiver(x_mesh, y_mesh, y_1_mesh, u_1, v_1, w_1, length=0.85 * lim / density, alpha=0.7)
# ax.quiver(x_mesh, y_mesh, y_1_mesh, u_2, v_2, w_2, length=0.85 * lim / density, color="orange", alpha=0.7)
ax.quiver(x_mesh, y_mesh, y_1_mesh, cp_x_arr, cp_y_arr, cp_z_arr, length=0.85 * lim / density, alpha=0.7)

ax.plot(all_pos_arr[:, 0], all_pos_arr[:, 1], all_pos_arr[:, 2], color="red", lw=2)

ax.set(xlabel="$x$", ylabel="$y$", zlabel="$y_1$")
plt.show()