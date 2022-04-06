from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import math


def run(dt, min_a, da):
    t_array = []
    tmp_t = 0
    while tmp_t < 2 * math.pi:
        t_array.append(tmp_t)
        tmp_t += dt

    a_array = []
    tmp_a = min_a
    while len(a_array) < len(t_array):
        a_array.append(tmp_a)
        tmp_a += da

    x_tmp_array = [t - math.sin(t) for t in t_array]
    y_tmp_array = [1 - math.cos(t) for t in t_array]
    x_array = [[a * x for x in x_tmp_array] for a in a_array]
    y_array = [[a * y for y in y_tmp_array] for a in a_array]

    x_mass_array = [math.pi * a for a in a_array]
    y_mass_array = [a * 4 / 3 for a in a_array]

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    for x in x_array:
        for y in y_array:
            ax.plot3D(x, y, a_array)

    ax.plot3D(x_mass_array, y_mass_array, a_array)

    ax.set_title(
        "Cycloids, " + str(min_a) + " <= a <= " + str(round(max(a_array), 2)) + ", dt = " + str(dt) + ", da = " +
        str(da))
    ax.set_xlabel('X = a(t - sint)')
    ax.set_ylabel('Y = a(1 - cost)')
    ax.set_zlabel('A')
    plt.grid(True)

    plt.savefig("dt_" + str(dt) + "_stereo_cycloids.png", format="png", dpi=300)
    plt.close()
    plt.plot(x_array, y_array, x_mass_array, y_mass_array)

    plt.title(
        "Cycloids, " + str(min_a) + " <= a <= " + str(round(max(a_array), 2)) + ", dt = " + str(dt) + ", da = " +
        str(da))
    plt.xlabel('X = a(t - sint)')
    plt.ylabel('Y = a(1 - cost)')
    plt.grid(True)
    plt.savefig("dt_" + str(dt) + "_plot_cycloids.png", format="png", dpi=300)


if __name__ == "__main__":
    run(0.1, 1, 0.1)  # (dt, min_a, da). max_a = 2 * pi / dt.
