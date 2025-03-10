import string
from collections import Counter
import matplotlib.pyplot as plt
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.corpus import  stopwords
text = open('read.txt',encoding='utf-8').read()
lower_case = text.lower()
cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))
print("The Cleaned Text is :",cleaned_text)
tokenization = word_tokenize(cleaned_text,"english")
print("The tokenized list :",tokenization)

final_words = []
for word in tokenization:
    if word not in stopwords.words('english'):
        final_words.append(word)
print("The final words are : ",final_words)

emotions_list = []
w = []
with open('emotions.txt','r') as file:
    for line in file:
        clear_line = line.replace('\n','').replace(',','').replace("'",'').strip()
        word,emotion = clear_line.split(':')
        #print("Word :",word,"         Emotion :",emotion)
        if word in final_words:
            emotions_list.append(emotion)
            w.append(word)
print("Emotions in this file are : ",emotions_list)
print(w)

c = Counter(emotions_list)
print(c)

def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    print(score)
    pos = score['pos']
    neg = score['neg']
    neu = score['neu']

    if neg>pos:
        print("Negative Sentiment")
    elif pos>neg:
        print("Positive Sentiment")
    else:
        print("Neutral Sentiment")
    print(max(pos,neu,neg))
sentiment_analyse(cleaned_text)
# fig,axl = plt.subplots()
# axl.bar(c.keys(),c.values())
# fig.autofmt_xdate()
# plt.savefig("barchart.png")
# plt.show()