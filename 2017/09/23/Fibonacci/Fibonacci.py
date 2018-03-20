
def fib1(number):
    if number == 0 or number == 1:
        return 1
    else:
        return fib1(number-1) + fib1(number-2)

def fib2(number):
    cur = 1
    pre = 1
    if number == 0 or number == 1:
        return 1
    number -= 1
    while number:
        cur, pre = pre + cur, cur
        number -= 1
    return cur

import numpy as np
def fib3(number):
    factor = np.matrix([[1, 1], [1, 0]])
    res = np.matrix([[1, 1], [1, 0]])
    bonus = np.matrix([[1, 0], [0, 1]])
    while(number > 1):
        if number % 2:
            bonus *= factor
        res = res * res
        number = int(number / 2)
        factor *= factor
    return (res * bonus)[0,0]

if __name__ == '__main__':
    import time
    import matplotlib.pyplot as plt
    time1 = []
    time2 = []
    time3 = []
    num = 30
    for number in range(30):
        t1 = time.time()
        f1 = fib1(number)
        t2 = time.time()
        time1.append(t2 - t1)
    for number in range(0, num, 1):
        t1 = time.time()
        f2 = fib2(number)
        t2 = time.time()
        time2.append(t2 - t1)

        t1 = time.time()
        f3 = fib3(number)
        t2 = time.time()
        time3.append(t2 - t1)

        # if f1 != f2 or f1 != f3 or f2 != f3:
        #     print("Error occur:", number, f1, f2, f3)

    x = np.arange(0, num, 1)

    plt.rc('font', weight='bold', size=6)
    plt.rc('mathtext', fontset='stixsans')
    plt.rcParams['text.latex.preamble'] = [r'\boldmath']

    # plt.scatter(np.arange(30), time1, color='g', label='normal')
    # plt.scatter(x, time2, color='r', label='memorized')
    # plt.scatter(x, time3, color='b', label='use matrix')
    plt.plot(np.arange(30), time1, color='g', linestyle='--', markerfacecolor='none', label='normal')
    plt.plot(x, time2, color='r', linestyle='--', markerfacecolor='none', label='memorized')
    plt.plot(x, time3, color='b', linestyle='--', markerfacecolor='none', label='use matrix')

    axis = plt.subplot(1, 1, 1)
    handles, label = axis.get_legend_handles_labels()

    axis.set_ylabel('time (s)', fontweight='bold')
    axis.set_xlabel('number', fontweight='bold')
    axis.grid(True, linestyle='dotted')
    axis.tick_params(top="on", right="on", direction='in')
    legend_properties = {'weight':'bold'}
    plt.legend(handles, label, prop=legend_properties, frameon=False)
    #plt.gca().invert_xaxis()
    #plt.show()
    fig = plt.gcf()
    #fig.set_size_inches(3.5, 2.66)
    fig.savefig('Fibonacci-1.png', bbox_inches='tight', dpi=600, facecolor='black')