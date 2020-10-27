word = 'Automovilismo'
vocals = 0

for w in word:
    y = w.lower()
    vocals += 1 if y == 'a' or y == 'e' or y == 'i' or y == 'o' or y == 'u' else 0

print(vocals)