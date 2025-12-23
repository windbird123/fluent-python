import re

RE_WORD = re.compile(r'\w+')

class SentenceV2:
    def __init__(self, text) -> None:
        self.text = text
        self.words = RE_WORD.findall(text)

    def __iter__(self):
        for word in self.words:
            yield word


if __name__ == '__main__':
    # 앞의 Sentence class 를 __iter__() + yield 를 사용해 만듬
    s = SentenceV2('"The time has come," the Walrus said,')
    for word in s:
        print(word)
