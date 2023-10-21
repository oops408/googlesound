import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

f = open("output.txt", "r")

text = f.read()

if not text:
    print("No text found.")
    print(text)

else:
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(text)

    freqTable = dict()
    for word in words:
        word = word.lower()
        if word in stopWords:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1
    sentences = sent_tokenize(text)
    sentenceValue = dict()
    for sentence in sentences:
        for word, freq in freqTable.items():
            if word in sentence.lower():
                if sentence in sentenceValue:
                    sentenceValue[sentence] += freq
                else:
                    sentenceValue[sentence] = freq
    sumValues = 0
    for sentence in sentenceValue:
        sumValues += sentenceValue[sentence]

    if len(sentenceValue) > 0:
        average = int(sumValues / len(sentenceValue))
    else:
        average = 0

    summary = ''
    for sentence in sentences:
        if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
            summary += " " + sentence

    print("Summary:")
    print(summary)

    print("Word Count: ")
    print(len(words))
    
    print("Sentence Count: ")
    print(len(sentenceValue))

with open("summary.txt", "w") as text_file:
    text_file.write(summary)