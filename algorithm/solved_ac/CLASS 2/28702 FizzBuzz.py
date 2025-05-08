import sys

input = sys.stdin.readline
print = sys.stdout.write

words = []
Fizz = "Fizz"
Buzz = "Buzz"
ans = 0
FizzBuzz = Fizz + Buzz
arr = [FizzBuzz, 1, 2, Fizz, 4, Buzz,
       Fizz, 7, 8, Fizz, Buzz,
       11, Fizz, 13, 14]

for _ in range(3):
    words.append(input().rstrip())

for i in range(3):
    if (words[i].isdigit()):
        ans = int(words[i]) + (3 - i)
        break

a, b = divmod(ans, 15)
if (str(arr[b]).isdigit()):
    print(str(ans))
else:
    print(arr[b])