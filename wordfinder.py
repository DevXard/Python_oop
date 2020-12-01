from random import choice

"""Word Finder: finds random words from a dictionary."""
class WordFinder:
 
    ...
    def __init__(self, direct):
        self.direct = direct
        print(self.open_file(), ' words read')

    def open_file(self):
        f = open(f'{self.direct}', 'r')
        lines = f.readlines()

        return len(lines)

    def random(self):
        f = open(f'{self.direct}', 'r')
        return choice(f.read().split()).strip()