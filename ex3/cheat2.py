
import gym
import numpy as np

env = gym.make('FrozenLake-v0')

Q = np.zeros((env.observation_space.n, env.action_space.n)) # initialize Q matrix to zeros

epsilon = 1.0   # probability to take random action
epsilon_decay = 0.98    # probability decays every episode

alpha = 0.1     # learning rate to update Q

num_episodes = 5000


for i_episode in xrange(num_episodes):
    observation = env.reset()
    done = False

    while not done:
        # current state
        state = observation

        # choose optimal action
        if np.random.rand() > epsilon:
            action = np.argmax(Q[state,:])  # choose best action according to current Q matrix
        else:
            action = action = env.action_space.sample()     # random action

        # take action and observe state and reward
        observation, reward, done, info = env.step(action)

    # update Q matrix
    if reward == 0:
        # if we fell in a hole, reward is -100
        R = -100
    else:
        # if we reached goal, reward is 100
        R = 100
    # Q-learning update
    Q[state,action] += alpha * (R + np.max(Q[observation,:]) - Q[state,action])

    # decay epsilon
    epsilon *= epsilon_decay
print Q
