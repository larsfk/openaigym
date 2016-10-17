import gym
import numpy as np

env = gym.make('FrozenLake-v0')

SIZE = env.observation_space.n
Q = []


def initialize_q():
    for i in range(SIZE):
        Q.append([0.5, 1, 0.5, 0.5])


def episode(state):
    action = np.argmax(Q[state])
    observation, reward, done, info = env.step(action)
    #env.render()
    return observation, reward, done


def run():
    counter = 0
    reward = 0
    state = env.reset()

    while reward < 1:
        state, reward, done = episode(state)

        if done and reward < 1:
        #    print "You died at round", counter
            state = env.reset()

        counter += 1

    #print "You found it at round", counter
    return counter

def main():
    initialize_q()
    sum = 0
    for i in range(1000):
        sum += run()
    print sum/1000


if __name__ == "__main__":
    main()
