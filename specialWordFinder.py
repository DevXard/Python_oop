from wordfinder import WordFinder

class specialWordFinder(WordFinder):

    def __init__(self, direct):
        self.direct = direct

    def special(self):
        result = []
        fi = open(f'{self.direct}', 'r')
        lines = fi.readlines()
        for line in lines:
            if line[0] != '#' and line.strip() != '':
                result.append(line.strip())
        return result