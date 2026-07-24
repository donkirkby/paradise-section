from collections import defaultdict
from pathlib import Path


def main():
    path = Path('/etc/dictionaries-common/words')
    with path.open() as f:
        all_words = (word.strip() for word in f)
        length_words = (word
                        for word in all_words
                        if len(word) == 6)
        lower_words = (word
                       for word in length_words
                       if word.islower())

        anagram_lists = defaultdict(list)
        for i, word in enumerate(lower_words):
            root = ''.join(sorted(word))
            anagrams = anagram_lists[root]
            anagrams.append(word)
            if i > 1000 and __name__ == '__live_coding__':
                break
        max_count = max(len(anagrams) for anagrams in anagram_lists.values())
        flexible_words = [word
                          for word, anagrams in anagram_lists.items()
                          if len(anagrams) >= max(3, max_count - 1)]
        for root in flexible_words:
            anagrams = anagram_lists[root]
            print(anagrams)

main()
