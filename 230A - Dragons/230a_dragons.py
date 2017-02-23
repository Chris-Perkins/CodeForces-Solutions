# Description of the problem can be found at http://codeforces.com/problemset/problem/230/A

strength, num_dragons = map(int, input().split())

dragons_strengths = list()
dragons_rewards = list()

for _ in range(num_dragons):
    dragon_strength, dragon_reward = map(int, input().split())
    dragons_strengths.append(dragon_strength)
    dragons_rewards.append(dragon_reward)
    
dragons_strengths, dragons_rewards = zip(*sorted(zip(dragons_strengths, dragons_rewards)))

for index in range(len(dragons_strengths)):
    if strength > dragons_strengths[index]:
        strength = int(strength) + dragons_rewards[index]
    else:
        print("NO")
        quit()

print("YES")    