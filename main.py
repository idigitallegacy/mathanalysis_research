import matplotlib.pyplot as plt
import math

size = math.pi * 2

def g(x):
    if x < -math.pi / 2:
        try:
            return math.pow(2, (1 / (x + math.pi / 2)))
        except OverflowError:
            return float('inf')
    if math.fabs(x) <= math.pi / 2:
        return math.cos(2 * x)
    if x > math.pi / 2:
        try:
            return math.pow(2, (1 / (x - math.pi / 2)))
        except OverflowError:
            return float('inf')

def previous_f(x):
    global size
    if -size < x < -math.pi / 2:
        try:
            tmp = math.pow(2, 2 / (2 * x + math.pi - 1))
            tmp *= 2 * x + math.pi
            return tmp
        except OverflowError:
            return 1e9
    if math.pi / 2 < x < size:
        try:
            tmp = math.pow(2, 1 / (x - math.pi / 2))
            tmp *= x - math.pi / 2
            return tmp
        except OverflowError:
            return 1e9
    return 0


def f(x):
    global size
    if -size < x < -math.pi / 2:
        try:
            tmp = math.pow(2, 2 / (2 * x + math.pi - 1))
            tmp *= 2 * x + math.pi

            # certainly known that function does not decrease
            if x > 1 - math.pi / 2:
                return -tmp
            return tmp
        except OverflowError:
            return float('inf')
    if math.fabs(x) <= math.pi / 2:
        return math.sin(x) * math.cos(x)
    if math.pi / 2 < x < size:
        try:
            tmp = math.pow(2, 1 / (x - math.pi / 2))
            tmp *= x - math.pi / 2

            # certainly known that function does not decrease
            if x < 2.2:
                return -tmp
            return tmp
        except OverflowError:
            return float('inf')


def run(dx):
    graphic = plt
    x_array = []

    x = -size
    while x < size:
        x_array.append(x)
        x += dx

    y_g_array = [g(x) for x in x_array]

    graphic.title("g(x), dx = " + str(dx))
    graphic.xlabel('X')
    graphic.ylabel('Y')
    graphic.grid(True)
    graphic.plot(x_array, y_g_array)
    graphic.savefig("dx_" + str(dx) + "_g(x).png", format="png", dpi=300)
    graphic.ylim([-10, 10])
    graphic.savefig("dx_" + str(dx) + "_g(x)_limited.png", format="png", dpi=300)


def afterrun(dx):
    graphic = plt
    x_array = []
    x = -size
    while x < size:
        x_array.append(x)
        x += dx

    y_g_array = [g(x) for x in x_array]
    y_f_array = [f(x) for x in x_array]

    graphic.title("f(x), g(x) dx = " + str(dx))
    graphic.xlabel('X')
    graphic.ylabel('Y')
    graphic.grid(True)

    graphic.plot(x_array, y_g_array, x_array, y_f_array)

    graphic.savefig("dx_" + str(dx) + "_f(x).png", format="png", dpi=300)
    graphic.ylim([-10, 10])
    graphic.savefig("dx_" + str(dx) + "_f(x)_limited.png", format="png", dpi=300)
    graphic.ylim([-3, 5])
    graphic.savefig("dx_" + str(dx) + "_f(x)_ultralimited.png", format="png", dpi=300)


if __name__ == '__main__':
    run(0.001)
    plt.close()

    afterrun(0.001)
    plt.close()

