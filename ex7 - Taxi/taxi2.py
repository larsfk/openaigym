import gym
import numpy as np
import random


env = gym.make('Taxi-v1')
env.monitor.start('/tmp/taxi2', force=True)



Q = []
SIZE = env.observation_space.n
LEARNING_RATE = 0.25
DISCOUNT_RATE = 0.99
E = 0.1


def initialize_q():
    for i in range(SIZE):
        Q.append([0, 0, 0, 0, 0, 0])

def q_learning():
    s = env.reset()
    done = False
    total_reward = 0
    na = e_greedy_action(s)
    while not done:
        #env.render()
        a = na

        ns, r, done, _ = env.step(a)
        total_reward += r

        na = e_greedy_action(ns)

        Q[s][a] += LEARNING_RATE * (float(r) + DISCOUNT_RATE * Q[ns][na] - Q[s][a])
        s = ns
    return total_reward

def e_greedy_action(s):
    if len(set(Q[s])) <= 1 or random.random() < E:
        return env.action_space.sample()
    else:
        return np.argmax(Q[s])

def print_q():
    print "DOWN, UP, RIGHT, LEFT, PICKUP, DROPOFF"
    for l in Q:
        print l



def main():
    global E
    initialize_q()
    total_reward = 0
    for i in range(2000):
        r = q_learning()
        if i > 500:
            total_reward += r
        E -= 0.5/2000
    print total_reward/1500.0

print_q()


if __name__ == "__main__":
    main()
env.monitor.close()
gym.upload('/tmp/taxi2', api_key='sk_wJpw7PKIQ92cQl2G2Oa4sQ')
