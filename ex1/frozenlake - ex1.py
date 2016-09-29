import gym

env = gym.make('FrozenLake-v0')

obs = env.reset()

done = False
counter = 0
reward = 0

while reward < 1:
    env.render()
    action = env.action_space.sample()
    obs, reward, done, info = env.step(action)
    print info
    print "Observation:", obs
    print "Reward", reward
    print "Done", done

    if done and reward < 1:
        print "You died at round", counter
        env.reset()

    counter += 1
print "You found it at round", counter





