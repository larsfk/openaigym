import gym
import numpy as np
import random

old_q = [[0.5767003363719356, 0.3287063066801955, 0.328207224914355, 0.3265190167869208],
     [0.258474291741455, 0.22954556904686588, 0.29625517516452976, 0.5108600271808252],
     [0.2821720814447693, 0.27348441178217436, 0.28910247288331176, 0.4670806839575886],
     [0.24581045134098434, 0.22782734835512813, 0.2224290421824645, 0.4518721262448759],
     [0.6247847028060564, 0.2957408776056888, 0.2641460892518556, 0.3362580652997783],
     [0, 0, 0, 0],
     [0.029941763090034372, 0.030516053007073655, 0.4185921839985824, 0.014620688681353286],
     [0, 0, 0, 0],
     [0.22935992319225063, 0.27479905107159946, 0.3275248703776332, 0.6512053959183662],
     [0.3084147468758004, 0.7255786127808296, 0.30434443350450335, 0.30595339876878463],
     [0.7129328182808019, 0.20185530833137627, 0.18648191415461107, 0.1491099907521132],
     [0, 0, 0, 0],
     [0, 0, 0, 0],
     [0.3707288973259156, 0.3831981196599762, 0.8069022618351328, 0.34018132818241803],
     [0.6051084200127824, 0.9224300813542278, 0.5870633352695784, 0.555607010746044],
     [0, 0, 0, 0]]

env = gym.make('FrozenLake-v0')
env.monitor.start('/tmp/frozenlake', force=True)



Q = []
SIZE = env.observation_space.n
LEARNING_RATE = 0.3
DISCOUNT_RATE = 0.99
E = 0.1


def initialize_q():
    for i in range(SIZE):
        Q.append([0, 0, 0, 0])

def q_learning():
    s = env.reset()
    done = False
    total_reward = 0

    while not done:
        if len(set(Q[s])) <= 1 or random.random() < E:
            a = env.action_space.sample()
        else:
            a = np.argmax(Q[s])

        ns, r, done, _ = env.step(a)
        total_reward += r

        Q[s][a] += LEARNING_RATE * (float(r) + DISCOUNT_RATE * max(old_q[ns]) - Q[s][a])
        s = ns
    return total_reward


def print_q():
    print "LEFT, DOWN, RIGHT, UP"
    for l in Q:
        print l



def main():
    global E
    initialize_q()
    total_reward = 0
    rounds = 10000
    offset = 1000
    for i in range(rounds):
        r = q_learning()
        if i > rounds - offset:
            total_reward += r
        E -= 0.25/rounds
    print total_reward/offset
    print_q()


if __name__ == "__main__":
    main()
env.monitor.close()
gym.upload('/tmp/frozenlake', api_key='sk_wJpw7PKIQ92cQl2G2Oa4sQ')



