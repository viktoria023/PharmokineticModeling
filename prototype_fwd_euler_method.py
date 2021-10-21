import numpy as np
import matplotlib.pyplot as plt


def dose(t, X):
    '''This is the dose function. '''
    return X*np.exp(t*np.sin(t))


def solve_ode(countT, initial_q_c, initial_q_p1, Q_p1, V_c, V_p1, CL):
    '''This is the solution for ODE without k_a'''
    q_c, q_p1 = initial_q_c, initial_q_p1
    qclist, qp1list = [], []
    for count_t in range(0, countT):
        t = count_t/countT
        q_c += (dose(t, X) - q_c / V_c * CL - Q_p1 * (q_c / V_c - q_p1 / V_p1))*(1 / countT)
        qclist.append(q_c)
        q_p1 += (Q_p1 * (q_c / V_c - q_p1 / V_p1))*(1 / countT)
        qp1list.append(q_p1)
    return [qclist, qp1list]


def solve_ode2(countT, initial_q_c, initial_q_p1, initial_q_0, Q_p1, V_c, V_p1, CL, k_a):
    '''This is the solution for ODE with k_a'''
    q_c, q_p1, q_0 = initial_q_c, initial_q_p1, initial_q_0
    qclist, qp1list, q0list = [], [], []
    for count_t in range(0, countT):
        t = count_t/countT
        q_0 += (dose(t, X) - k_a*q_0)*(1 / countT)
        q0list.append(q_0)
        q_c += (k_a*q_0 - q_c / V_c * CL - Q_p1 * (q_c / V_c - q_p1 / V_p1))*(1 / countT)
        qclist.append(q_c)
        q_p1 += (Q_p1 * (q_c / V_c - q_p1 / V_p1))*(1 / countT)
        qp1list.append(q_p1)
    return [qclist, qp1list, q0list]


def plotode(all_graphs_axes, Type):
    '''This is the plot function'''
    output = np.array(qclist)
    output2 = np.array(qp1list)
    all_graphs_axes.plot(output, label=f'Model {Type}: q_c')
    all_graphs_axes.plot(output2, label=f'Model {Type}: q_p1')
    plt.legend()
    plt.ylabel('drug mass [ng]')
    plt.xlabel('time [h]')


# Test Plot for ODE without k_a
all_graphs, all_graphs_axes = plt.subplots()
initial_q_c, initial_q_p1, Q_p1, V_c, V_p1, CL = 0, 0, 1, 1, 1, 1
countT, X = 100, 1
[qclist, qp1list] = solve_ode(countT, initial_q_c, initial_q_p1, Q_p1, V_c, V_p1, CL)
plotode(all_graphs_axes, '(no k_a, Parameter 1)')

initial_q_c, initial_q_p1, Q_p1, V_c, V_p1, CL = 0, 0, 2, 1, 1, 1
countT, X = 100, 1
[qclist, qp1list] = solve_ode(countT, initial_q_c, initial_q_p1, Q_p1, V_c, V_p1, CL)
plotode(all_graphs_axes, '(no k_a, Parameter 2)')
plt.show()


# Test Plot for ODE with k_a
all_graphs, all_graphs_axes = plt.subplots()
initial_q_c, initial_q_p1, initial_q0, Q_p1, V_c, V_p1, CL, k_a = 0, 0, 0, 1, 1, 1, 1, 1
countT, X = 100, 1
[qclist, qp1list, q0list] = solve_ode2(countT, initial_q_c, initial_q_p1, initial_q0, Q_p1, V_c, V_p1, CL, k_a)
plotode(all_graphs_axes, '(with k_a, Parameter 1)')

initial_q_c, initial_q_p1, Q_p1, V_c, V_p1, CL = 0, 0, 2, 1, 1, 1
countT, X = 100, 1
[qclist, qp1list] = solve_ode(countT, initial_q_c, initial_q_p1, Q_p1, V_c, V_p1, CL)
plotode(all_graphs_axes, '(with k_a, Parameter 2)')
plt.show()
