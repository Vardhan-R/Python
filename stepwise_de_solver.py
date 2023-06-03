import matplotlib.pyplot as plt, numpy as np

dt = 0.01
x = np.linspace(-5, 5, 31)
y = np.linspace(-5, 5, 31)

x_mesh, y_mesh = np.meshgrid(x, y)

# u = y_mesh / x_mesh + 6 * x_mesh
# v = np.log(np.abs(x_mesh)) - 2
# u = 3 * y_mesh ** 2
# v = 2 * x_mesh ** 3
u = 2 * x_mesh + 3
v = 2 * y_mesh - 2
# u = 3 * x_mesh ** 2 + 6 * x_mesh * y_mesh ** 2
# v = 6 * x_mesh ** 2 * y_mesh + 4 * y_mesh ** 3
# u = 3 * x_mesh ** 2 * y_mesh + 2 * x_mesh * y_mesh + y_mesh ** 3
# v = x_mesh ** 2 + y_mesh ** 2
# u = (3 * x_mesh ** 2 * y_mesh ** 3 - y_mesh ** 2 + y_mesh) / x_mesh ** 2 / y_mesh ** 3
# v = (-x_mesh * y_mesh + 2 * x_mesh) / x_mesh ** 2 / y_mesh ** 3
# u = -2 * y_mesh
# v = x_mesh

v_x, v_y = -v, u
p_x, p_y = 0.9, 0.1
all_pos_x = [p_x]
all_pos_y = [p_y]

for i in range(400):
    d_x = np.abs(p_x - x)
    d_y = np.abs(p_y - y)
    p_x_index = np.argmin(d_x)
    p_y_index = np.argmin(d_y)
    p_x += v_x[p_y_index][p_x_index] * dt
    p_y += v_y[p_y_index][p_x_index] * dt
    all_pos_x.append(p_x)
    all_pos_y.append(p_y)

c = 1
# sol = y_mesh * np.log(np.abs(x_mesh)) + 3 * x_mesh ** 2 - 2 * y_mesh
# sol = -4 * x_mesh ** 2 / (c * x_mesh ** 2 + 3) - y_mesh
sol = x_mesh ** 2 + 3 * x_mesh + y_mesh ** 2 - 2 * y_mesh
# sol = x_mesh ** 3 + 3 * x_mesh ** 2 * y_mesh ** 2 + y_mesh ** 4
# sol = y_mesh * (x_mesh ** 2 + y_mesh ** 2 / 3) * np.exp(3 * x_mesh)
# sol = 1 / x_mesh / y_mesh ** 2 * (y_mesh - 1) + 3 / 5 * x_mesh
# sol = y_mesh / x_mesh ** 2

plt.quiver(x_mesh, y_mesh, u, v)
# plt.plot(x, y_sol)
# plt.contour(x_mesh, y_mesh, sol, [c], colors=["red"])
plt.contourf(x_mesh, y_mesh, sol, np.linspace(1, 10, 10))
plt.plot(all_pos_x, all_pos_y, color="red", lw=2)
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.gca().set_aspect("equal", "box")
plt.title("Vector Field and Solution Contour")
plt.show()

# ax = plt.figure().add_subplot(projection="3d")
# ax.plot_surface(x_mesh, y_mesh, sol, edgecolor="royalblue", lw=0.5, rstride=1, cstride=1, alpha=0.3)
# ax.set(xlabel='$x$', ylabel='$y$', zlabel='$G\\left(x,y\\right)$')
# plt.show()