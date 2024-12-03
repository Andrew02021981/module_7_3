import io
from pprint import pprint
class WordsFinder:
    def __init__(self, *file_names : list):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for name in self.file_names:
            with open(name, encoding='utf-8') as file:
                list_2 = []
                for line in file:
                    line = line.lower()
                    list_1 = [',', '.', '=', '!', '?', ';', ':', ' - ']
                    # for i in list_1:
                    #     if list_1[i] in line:
                    #         line.replace(list_1[i], '')
                    # return line.split()

                all_words.update({name : list_2})
            return all_words


finder2 = WordsFinder('test_file.txt')

print(finder2.get_all_words()) # Все слова
#
# print(finder2.find('TEXT')) # 3 слово по счёту
#
# print(finder2.count('teXT')) # 4 слова teXT в тексте всего