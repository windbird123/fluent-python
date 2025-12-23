import re

RE_WORD = re.compile(r'\w+')

class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)


if __name__ == '__main__':
    """
    Sentence class 를 정의해 word 단위로 출력 - word 단위로 분석은 regex 사용
    """
    s = Sentence('"The time has come," the Walrus said,')
    for word in s:
        print(word)

    print(s[0]) # The

    # 1. 파이썬이 객체 x를 반복해야 할 때마다, 자동으로 iter(x)를 호출
    # 2. __iter__ 를 찾고, 없으면 __getitem__

    it = iter(s)
    print(next(it)) # The
    print(next(it)) # time

