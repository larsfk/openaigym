import gym
import numpy as np
import random

env = gym.make('FrozenLake-v0')
# env.monitor.start('/tmp/frozenlake')

SIZE = env.observation_space.n
Q = []
E = 0.1
MAX_STEPS = 100
DISCOUNT_RATE = 0.99
LEARNING_RATE = 0.3
EPISODES = 2000

reward_list = []


def initialize_q():
    for i in range(SIZE):
        Q.append([0, 0, 0, 0])


def episode(i):
    global E
    s = env.reset()
    total_reward = 0
    counter = 1
    while counter < MAX_STEPS:
        a = e_greedy(s)

        ns, r, done, info = env.step(a)
        Q[s][a] += LEARNING_RATE * (r + DISCOUNT_RATE * max(Q[ns]) - Q[s][a])

        total_reward += ((DISCOUNT_RATE ** counter) * r)

        if done:
            break

        s = ns
        counter += 1
    reward_list.append(total_reward)

    E -= 0.5 / EPISODES
    print "EP:", i, "R:", total_reward
    return counter


def e_greedy(s):
    if len(set(Q[s])) <= 1 or random.random() < E:
        return env.action_space.sample()
    else:
        return np.argmax(Q[s])


def print_q():
    print "LEFT, DOWN, RIGHT, UP"
    for l in Q:
        print l


def main():
    initialize_q()
    s = 0
    for i in range(EPISODES):
        s += episode(i)
        # print "Episode nr", i + 1
    print_q()
    print "Score over time: " + str(sum(reward_list) / EPISODES)


if __name__ == "__main__":
    main()

# env.monitor.close()
# gym.upload('/tmp/frozenlake', api_key='sk_wJpw7PKIQ92cQl2G2Oa4sQ')
