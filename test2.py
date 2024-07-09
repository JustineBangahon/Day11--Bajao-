
word = ['D', 'S', 'M', 'R', 'A', 'E']

a = len(word)
b = len(word) - 1

for i in range(a):
    print(f"[1] Outer Loop: {i}  |  {word}")
    for j in range(b):
        print(f"Inner Loop: {i}  |  {word}")
        if word[j] > word[j + 1]:
            swap = word[j]
            word[j] = word[j + 1]
            word[j + 1] = swap
print(f"[4] Outside: {i}  |  {word}")
