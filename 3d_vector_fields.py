import matplotlib.pyplot as plt, numpy as np

density = 11
lim = 5

x = np.linspace(-lim, lim, density)
y = np.linspace(-lim, lim, density)
y_1 = np.linspace(-lim, lim, density)

x_mesh, y_1_mesh, y_mesh = np.meshgrid(x, y_1, y)
x_mesh_2d, y_mesh_2d = np.meshgrid(x, y)
y_mesh_2d_2 = x_mesh_2d
y_1_mesh_2d = y_mesh_2d

'''Vector Fields (u, v and w)'''
u, v, w = 0, x_mesh * y_1_mesh - y_mesh, x_mesh * y_mesh # ellipses

'''Solutions for General Ellipse Equation'''
a = 2 # semi-major axis
b = 1 # semi-minor axis
c_1 = -1
c_2 = 1

sol_1 = (x_mesh_2d / a) ** 2 + (y_mesh_2d / b) ** 2 - 1
sol_2 = y_mesh_2d_2 ** 2 * (y_1_mesh_2d ** 2 + (b / a) ** 2) - c_2

x_to_show = np.array((x, x))
y_to_show = b / a * np.sqrt(a ** 2 - x ** 2)
# y_to_show = np.concatenate((y_to_show, -y_to_show), axis=1)
y_to_show = np.array((y_to_show, -y_to_show))
y_1_to_show = -(b / a) ** 2 * x_to_show / y_to_show

full_sol = np.abs((x_mesh / a) ** 2 + (y_mesh / b) ** 2 - 1) + np.abs(y_1_mesh + (b / a) ** 2 * x_mesh / y_mesh)

sol_2 = -(b / a) ** 2 * x_mesh_2d / y_mesh_2d

# sol = (x_mesh[0] / a) ** 2 + (y_mesh[0] / b) ** 2 - 1

ax = plt.figure().add_subplot(projection="3d")

ax.quiver(x_mesh, y_mesh, y_1_mesh, u, v, w, length=0.05, alpha=0.7)
# ax.plot_surface(x_mesh_2d, y_mesh_2d, sol_1, edgecolor="red", lw=0.5, rstride=1, cstride=1, alpha=0.3)
# ax.plot_surface(x_mesh_2d, y_mesh_2d, sol_2, edgecolor="royalblue", lw=0.5, rstride=1, cstride=1, alpha=0.3)
# ax.plot_surface(y_mesh_2d_2, y_1_mesh_2d, sol_2, edgecolor="royalblue", lw=0.5, rstride=1, cstride=1, alpha=0.3)
# ax.plot_surface(x_mesh[0], y_mesh[0], sol, edgecolor="red", lw=0.5, rstride=1, cstride=1, alpha=0.3)
# ax.contourf(x_mesh_2d, y_mesh_2d, sol_2, zdir='z', cmap="coolwarm")
# ax.contour(x_mesh_2d, y_mesh_2d, sol_2, sol_1 + sol_2, zdir='z', cmap="coolwarm")
# ax.contourf(y_mesh_2d_2, y_1_mesh_2d, sol_2, zdir='z', offset=100, cmap="coolwarm")
# ax.contour(x_to_show, y_to_show, np.zeros((2, 41)), zdir='z', offset=0, cmap="coolwarm")
# print(y_to_show)

# ax.plot_surface(x_to_show[0], y_to_show[0], np.zeros((2, 41)), edgecolor="red", lw=0.5, rstride=1, cstride=1, alpha=0.3)

x = np.linspace(-5, 5, 801)
ax.plot(x, b / a * np.sqrt(a ** 2 - x ** 2), -(b / a) * x / np.sqrt(a ** 2 - x ** 2), color="red", lw=2)
ax.plot(x, -b / a * np.sqrt(a ** 2 - x ** 2), (b / a) * x / np.sqrt(a ** 2 - x ** 2), color="red", lw=2)

ax.set(xlabel="$x$", ylabel="$y$", zlabel="$y_1$")
plt.show()