import gym
import numpy as np
import random

env = gym.make('FrozenLake-v0')

SIZE = env.observation_space.n
Q = []
E = 0.1
MAX_STEPS = 100
DISCOUNT_RATE = 0.99
LEARNING_RATE = 0.85

reward_list = []


def initialize_q():
    for i in range(SIZE):
        Q.append([0, 0, 0, 0])


def step(state,i):
    # if len(set(Q[state])) <= 1 or random.random() < E:
    #     action = env.action_space.sample()
    # else:
    #     action = np.argmax(Q[state])
    action = np.argmax(Q[state] + np.random.randn(1, env.action_space.n)*(1./(i+1))) #cheat

    # TODO: MAKE A BETTER E-GREEDY ACTION-PICKER

    observation, reward, done, info = env.step(action)
    q_learning(action, reward, state, observation)
    # env.render()
    return observation, reward, done


def episode(i):
    state = env.reset()
    total_reward = 0
    counter = 1
    while counter < MAX_STEPS:
        state, reward, done = step(state,i)
        total_reward += ((DISCOUNT_RATE ** counter) * reward)

        if done:
            break

        counter += 1
        # print "You found it at round", counter
    reward_list.append(total_reward)
    #print "Total reward", total_reward
    return counter


def q_learning(a, r, s, ns):  # ns = next state
    if r == 1:
        print "S,A,R,NS", s,a,r,ns
        print "BEFORE:",Q[s][a]
        Q[s][a] += LEARNING_RATE * (r + DISCOUNT_RATE * (max(Q[ns]) - Q[s][a]))
        print "AFTER:",Q[s][a]
        print "--------------------"
    else:
        Q[s][a] += LEARNING_RATE * (r + DISCOUNT_RATE * (max(Q[ns]) - Q[s][a]))




def main():
    initialize_q()
    s = 0
    episodes = 2000
    for i in range(episodes):
        s += episode(i)
        print "Episode nr", i + 1
    print Q
    print "Score over time: " + str(sum(reward_list)/episodes)

if __name__ == "__main__":
    main()
