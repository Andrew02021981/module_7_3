class WordsFinder:
    def __init__(self, *file_names : list):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for name in self.file_names:
            with open(name, encoding='utf-8') as file:
                line_1 = file.read()
                for line in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                   line_1 = line_1.lower().replace(line, '')
            all_words[name] = line_1.split()
        return all_words

    def find(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        word_position = {}
        for name, words in all_words.items():
            if word in words:
                word_position[name] = words.index(word) + 1
        return word_position

    def count(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        word_counts = {}
        for name, words in all_words.items():
            word_counts[name] = words.count(word)
        return word_counts

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

print()

finder3 = WordsFinder('Mother Goose - Monday’s Child.txt',)
print(finder3.get_all_words())
print(finder3.find('Child'))
print(finder3.count('Child'))

print()

finder4 = WordsFinder('Rudyard Kipling - If.txt',)
print(finder4.get_all_words())
print(finder4.find('if'))
print(finder4.count('if'))

print()

finder5 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder5.get_all_words())
print(finder5.find('captain'))
print(finder5.count('captain'))
