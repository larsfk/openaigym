import gym
import numpy as np
import random

env = gym.make('FrozenLake-v0')

SIZE = env.observation_space.n
Q = []
E = 0.01


def initialize_q():
    for i in range(SIZE):
        Q.append([0.5, 1, 0.5, 0.5])


def step(state):
    if random.random() < E:
        action = env.action_space.sample()
    else:
        action = np.argmax(Q[state])
    observation, reward, done, info = env.step(action)
    #env.render()
    return observation, reward, done


def episode():
    counter = 0
    reward = 0
    state = env.reset()

    while reward < 1:
        state, reward, done = step(state)

        if done and reward < 1:
            #print "You died at round", counter
            state = env.reset()
            print reward

        counter += 1
    #print "You found it at round", counter
    return counter

def main():
    initialize_q()
    sum = 0
    for i in range(100):
        sum += episode()
    print sum/100

if __name__ == "__main__":
    main()
