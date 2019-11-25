def avg_temps(temps):
    sum_temps = 0
    for temp in temps:
        sum_temps += temp
    return sum_temps/len(temps)


if __name__ == '__main__':
    temps = [21,15,21,22,20,23,24]
    avg = avg_temps(temps)
    print("La temperatura promedio es: {0}".format(avg))