import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest
import sys as s

text = s.argv[1]
stop = list(STOP_WORDS)
#text = "Purpose and motivation for the course,Self-Exploration–what is it? - Its content and process; ‘Natural Acceptance’ and Experiential Validation- as the process for self-exploration,Continuous Happiness and Prosperity- A look at basic Human Aspirations,Right understanding, Relationship and Physical Facilitythe basic requirements for fulfillment of aspirations of every human being with their correct priority,Understanding Happiness and Prosperity correctly- A critical appraisal of the current scenario, Method to fulfil the above human aspirations: understanding and living in harmony at various levels."
#print(text)
nlp = spacy.load("en_core_web_sm")
doc = nlp(text)
token = [token.text for token in doc]
#print(token)
punctuation = punctuation + '\n'
#punctuation
word_freq = {}
for word in doc:
    if word.text.lower() not in stop:
        if word.text.lower() not in punctuation:
            if word.text not in word_freq.keys():
                word_freq[word.text] = 1
            else:
                word_freq[word.text] += 1
max_freq = max(word_freq.values())
for word in word_freq.keys():
    word_freq[word] = word_freq[word]/max_freq
sentences = [sentence for sentence in doc.sents]
sentence_score ={}
for senten in sentences:
    for word in senten:
        if word.text.lower() in word_freq.keys():
            if senten not in sentence_score.keys():
                sentence_score[senten] = word_freq[word.text.lower()]
            else:
                sentence_score[senten] +=word_freq[word.text.lower()]
#sentence_score
somesentence = int(len(sentences)*0.3)
summary = nlargest(somesentence,sentence_score,key=sentence_score.get)
summary = str(summary)
print(summary)