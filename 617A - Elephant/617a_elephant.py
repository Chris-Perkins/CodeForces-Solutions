# Description of the problem can be found at https://www.twitch.tv/savjz

n = int(input())
print(n // 5 + (1 if n % 5 != 0 else 0))