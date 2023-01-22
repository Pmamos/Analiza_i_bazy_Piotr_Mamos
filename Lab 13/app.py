from textblob import TextBlob

def hello(name):
    output = f'Hello {name}'
    return output


def extract_sentiment(text):
    text = TextBlob(text)

    return text.sentiment.polarity

def text_contain_word(word: str, text: str):
    return word in text

def bubble_sort(unsorted: list[int]):
    flag = True
    while flag:
        flag = False
        for i in range(len(unsorted)-1):
            if unsorted[i+1] < unsorted[i]:
                unsorted[i+1], unsorted[i] = unsorted[i], unsorted[i+1]
                flag = True
    return unsorted