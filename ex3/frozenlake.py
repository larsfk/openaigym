import gym
import numpy as np
import random


env = gym.make('FrozenLake-v0')
#env.monitor.start('/tmp/frozenlake', force=True)



Q = []
SIZE = env.observation_space.n
LEARNING_RATE = 0.1
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

        Q[s][a] += LEARNING_RATE * (float(r) + DISCOUNT_RATE * max(Q[ns]) - Q[s][a])
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
#env.monitor.close()
#gym.upload('/tmp/frozenlake', api_key='sk_wJpw7PKIQ92cQl2G2Oa4sQ')
