from collections import Counter

a = "aaagabbbbbcacccccee"
my_counter = Counter(a)
print(my_counter)
print(my_counter.values())
print(my_counter.keys())
print(my_counter.most_common(2))
