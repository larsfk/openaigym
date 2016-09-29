import gym

env = gym.make("Taxi-v1")

env.render()
done = False
count = 0

while not done:
    env.render()
    action = env.action_space.sample()
    observation, reward, done, info = env.step(action)

    print "Observation", observation
    print "Reward", reward
    count += 1

print "Done after round", count



