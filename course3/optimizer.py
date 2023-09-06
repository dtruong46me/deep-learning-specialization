import math


def optimize1(x):
    f = 1/2 * (x - 3)**2
    derivative = x-3

    theta=0
    learning_rate = 0.1
    for i in range(100):
        print(f"t={i}: \\theta_{i}= {theta:.2f} - {learning_rate} \\times ({theta:.2f} - 3) = {theta - learning_rate * (theta-3):.3f}")
        theta = theta - learning_rate * (theta-3)

    return

def optimize2(x, beta_1=0.9, beta_2=0.999, epsilon=1e-8):

    f = 1/2 * (x-3)**2
    m_t = 0
    v_t = 0
    theta=0
    for i in range(1, 100):
        m_t = 0.9*m_t + (1-0.9) * (theta - 3)
        v_t = 0.999 * v_t + (1-0.999) * (theta -3)**2
        m_t_hat = m_t / (1-0.9**i)
        v_t_hat = v_t / (1-0.999**i)
        theta = theta - 0.1 * m_t_hat / (math.sqrt(v_t_hat) + epsilon)
        print(f"t={i}: m_t={m_t:.3f}, v_t={v_t:.3f}, m_t_hat={m_t_hat:.3f}, v_t_hat={v_t_hat:.3f}, \\theta_{i}={theta:.3f}")

    return

if __name__=='__main__':
    # optimize1(0)
    optimize2(0)