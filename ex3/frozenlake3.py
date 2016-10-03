import gym
import numpy as np
import random

env = gym.make('FrozenLake-v0')

SIZE = env.observation_space.n
Q = []


reward_list = []


def initialize_q():
    for i in range(SIZE):
        Q.append([0, 0, 0, 0])


def step(state, counter, E, DELTA, MAX_STEPS, DISCOUNT_RATE, LEARNING_RATE, EPISODES):
    if len(set(Q[state])) <= 1 or random.random() < E:
        action = env.action_space.sample()
    else:
        action = np.argmax(Q[state])
    # action = np.argmax(Q[state] + np.random.randn(1, env.action_space.n)*(1./(i+1))) #cheat


    # TODO: MAKE A BETTER E-GREEDY ACTION-PICKER

    observation, reward, done, info = env.step(action)
    q_learning(action, reward, state, observation, counter, E, DELTA, MAX_STEPS, DISCOUNT_RATE, LEARNING_RATE, EPISODES)

    # env.render()
    return observation, reward, done


def episode(i, E, DELTA, MAX_STEPS, DISCOUNT_RATE, LEARNING_RATE, EPISODES):
    state = env.reset()
    total_reward = 0
    counter = 1
    while counter < MAX_STEPS:
        state, reward, done = step(state, counter, E, DELTA, MAX_STEPS, DISCOUNT_RATE, LEARNING_RATE, EPISODES)
        total_reward += ((DISCOUNT_RATE ** counter) * reward)

        if done:
            break

        counter += 1
        # print "You found it at round", counter
    reward_list.append(total_reward)

    E -= DELTA / EPISODES
    # print "EP:",i , "R:", total_reward
    # print "Total reward", total_reward
    return counter


def q_learning(a, r, s, ns, counter, E, DELTA, MAX_STEPS, DISCOUNT_RATE, LEARNING_RATE, EPISODES):  # ns = next state
    if r == 1:
        # print "S,A,R,NS", s, a, r, ns
        # print "BEFORE:", Q[s][a]
        Q[s][a] += LEARNING_RATE * (r + DISCOUNT_RATE * (max(Q[ns]) - Q[s][a]))
        # print "AFTER:", Q[s][a]
        # print "--------------------"
    else:
        Q[s][a] += LEARNING_RATE * (r + DISCOUNT_RATE * (max(Q[ns]) - Q[s][a]))


def print_q():
    print "LEFT, DOWN, RIGHT, UP"
    for l in Q:
        print l


def run_rl(n, E, DELTA, MAX_STEPS, DISCOUNT_RATE, LEARNING_RATE, EPISODES):
    initialize_q()
    s = 0
    for i in range(n):
        s += episode(i, E, DELTA, MAX_STEPS, DISCOUNT_RATE, LEARNING_RATE, EPISODES)
    return sum(reward_list) / EPISODES


def main():

    tuning()
    #initialize_q()
    #s = 0
    #for i in range(EPISODES):
        #s += episode(i)
        # print "Episode nr", i + 1
    #print_q()
    #print "Score over time: " + str(sum(reward_list) / EPISODES)


def log(string):
    target = open("log.txt", 'a')
    target.write(string)
    target.write("\n")
    target.close()


def tuning():

    E = 0.1
    DELTA = 0.5
    MAX_STEPS = 100
    DISCOUNT_RATE = 0.99
    LEARNING_RATE = 0.3
    EPISODES = 4000

    changed = True
    best_score = 0
    while changed:
        best_parameter = 100
        for i in range(100, 10000,100):
            total_score = 0
            for j in range(100):
                total_score += run_rl(i, E, DELTA, MAX_STEPS, DISCOUNT_RATE, LEARNING_RATE, EPISODES)

            if total_score/100.0 > best_score:
                best_score = total_score/100.0
                best_parameter = i
        EPISODES = best_parameter
        log("Updating episodes to: " + str(EPISODES))

        best_score = 0
        best_parameter = 0.01
        for i in range(1,100,1):
            k = float(i / 100.0)
            total_score = 0
            for j in range(100):
                total_score += run_rl(i, E, DELTA, MAX_STEPS, DISCOUNT_RATE, LEARNING_RATE, EPISODES)

            if total_score/100.0 > best_score:
                best_score = total_score/100.0
                best_parameter = k
        LEARNING_RATE = best_parameter
        log("Updating learning rate to: " + str(LEARNING_RATE))

        best_score = 0
        best_parameter = 0.01
        for i in range(1,100,1):
            k = float(i / 100.0)
            total_score = 0
            for j in range(100):
                total_score += run_rl(i, E, DELTA, MAX_STEPS, DISCOUNT_RATE, LEARNING_RATE, EPISODES)

            if total_score/100.0 > best_score:
                best_score = total_score/100.0
                best_parameter = k
        DELTA = best_parameter
        log("Updating DELTA to: " + str(DELTA))



if __name__ == "__main__":
    main()
