import collections
import heapq

inverted_index = collections.defaultdict(set)
for line in open("/usr/share/dict/words"):
    word = line.strip().lower()  # ignore case
    for letter in word:
        inverted_index[letter].add(word)

#print sorted(inverted_index["a"] & inverted_index["j"])[:5]    
print heapq.nsmallest(5, inverted_index["a"] & inverted_index["j"])    