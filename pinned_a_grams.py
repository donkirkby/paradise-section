import re
from collections import defaultdict
from itertools import combinations
from pathlib import Path


def main():
    path = Path('/etc/dictionaries-common/words')
    with path.open() as f:
        all_words = (word.strip() for word in f)
        length_words = (word
                        for word in all_words
                        if 3 <= len(word) <= 7)
        lower_words = (word
                       for word in length_words
                       if re.match(r'^[a-z]+$', word))

        anagram_lists = defaultdict(list)
        for i, word in enumerate(lower_words):
            root = ''.join(sorted(word))
            anagrams = anagram_lists[root]
            anagrams.append(word)
            if i > 1000 and __name__ == '__live_coding__':
                break
        useful_anagrams = [anagrams
                           for root, anagrams in anagram_lists.items()
                           if len(anagrams) > 1]
        summaries = []
        for anagrams in useful_anagrams:
            for a, b in combinations(anagrams, 2):
                fixed_positions = [i
                                   for i, (ai, bi) in enumerate(zip(a, b))
                                   if ai == bi]
                if fixed_positions:
                    summaries.append(f'{len(a)} {fixed_positions} {a} {b}')
        summaries.sort()
        print('\n'.join(summaries))
        max_count = max(len(anagrams) for anagrams in anagram_lists.values())
        flexible_words = [word
                          for word, anagrams in anagram_lists.items()
                          if len(anagrams) >= max(3, max_count - 1)]
        for root in flexible_words:
            anagrams = anagram_lists[root]
            print(anagrams)

main()
