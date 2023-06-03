import matplotlib.pyplot as plt, numpy as np

density = 11
lim = 8

x = np.linspace(-lim, lim, density)
y = np.linspace(-lim, lim, density)
y_1 = np.linspace(-lim, lim, density)
# y = np.logspace(-lim, lim, density)
# y_1 = np.logspace(-lim, lim, density)

x_mesh, y_1_mesh, y_mesh = np.meshgrid(x, y_1, y)

'''Constant 2nd Order ODE's'''
a, b, c = 1, -4, 4
m = np.sqrt((c * y_mesh) ** 2 + b ** 2 + a ** 2)
u, v, w = c * y_mesh / m, b / m, a / m

'''Solutions'''
c_1 = 1
c_2 = 1

discriminant = b ** 2 - 4 * a * c

x = np.linspace(-10, 1, 301)

if discriminant > 0:
    m_1 = (-b - np.sqrt(discriminant)) / 2 / a
    m_2 = (-b + np.sqrt(discriminant)) / 2 / a

    y = c_1 * np.exp(m_1 * x) + c_2 * np.exp(m_2 * x)
    y_1 = c_1 * m_1 * np.exp(m_1 * x) + c_2 * m_2 * np.exp(m_2 * x)

elif discriminant == 0:
    m = -b / 2 / a

    y = np.exp(m * x) * (c_1 + c_2 * x)
    y_1 = np.exp(m * x) * (m * (c_1 + c_2 * x) + c_2)

else:
    la = -b / 2 / a
    om = np.sqrt(-discriminant) / 2 / a

    y = np.exp(la * x) * (c_1 * np.cos(om * x) + c_2 * np.sin(om * x))
    y_1 = np.exp(la * x) * (la * (c_1 * np.cos(om * x) + c_2 * np.sin(om * x)) + om * (c_2 * np.cos(om * x) - c_1 * np.sin(om * x)))

ax = plt.figure().add_subplot(projection="3d")

ax.quiver(x_mesh, y_mesh, y_1_mesh, u, v, w, length=1.7 * lim / density, alpha=0.7)
# ax.quiver(x_mesh, np.log10(y_mesh), np.log10(y_1_mesh), np.log10(u), v, w, length=0.2, alpha=0.7)
# ax.set_yscale("symlog")
# ax.set_zscale("symlog")
ax.plot(x, y, y_1, color="red", lw=2)
# ax.plot(x, np.log10(y), np.log10(y_1), color="red", lw=2)

ax.set(xlabel="$x$", ylabel="$y$", zlabel="$y_1$", xlim=(-lim, lim), ylim=(-lim, lim), zlim=(-lim, lim))
plt.show()