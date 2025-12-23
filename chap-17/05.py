import re

RE_WORD = re.compile(r'\w+')

if __name__ == '__main__':
    """
    generator expression 사용 
    """
    def __init__(self, text):
        self.text = text

    def __iter__(self):
        it = RE_WORD.finditer(self.text)
        return (match.group() for match in it)
