# Search phone directory for screenshot
import datetime
starttime = datetime.datetime.now()
import ssReader
# image saved in current directory as ss.jpg

# OCR imports
from PIL import Image
import pytesseract
import cv2

# preprocess ss.jpg
gray = cv2.imread('ss.jpg', 0)
gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
filename = "ssPreProc.png"
# cv2.imshow("Processed", gray)
# cv2.waitKey(0)
cv2.imwrite(filename, gray)
# preprocessed image saved as ssPreProc.jpg

# OCR using Google's tesseract engine
text = pytesseract.image_to_string(Image.open(filename))

# Segment text into question and options

ques = ""
start = 0
for i in xrange(len(text)-1):
    if (text[i].isalpha() and text[i+1].isalpha()) == True :
        break;
    else:
        start +=1

end = start
for i in xrange(start, len(text)-1):
    if text[i] == '\n':
        ques += " "
    elif text[i] == ' ':
        ques += ' '
    elif text[i] == '?':
        end = i + 1
        break;
    else:
        ques += text[i]

print "Question is: ", ques, "?"

# clean and remove stop words from Ques
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words('english'))
stop_words.remove('not')
stop_words.remove('most')
stop_words.update(['.','-','?','!',',','...',':',"'s"])
word_tokens = word_tokenize(ques)
filtered_ques = ""
for w in word_tokens:
    if w not in stop_words:
        try:
            w = w.decode('utf-8')
        except UnicodeEncodeError:
            wnew = ""
            for i in w:
                flag = True
                try:
                    i.decode('utf-8')
                except UnicodeEncodeError:
                    flag = False
                    continue
                if flag == True:
                    wnew += i
            w = wnew
        filtered_ques += (w + " ")

print "Filtered Ques: ", filtered_ques

options = ""
for i in xrange(end, len(text)):
    options += text[i]

options = options.split('\n')
choices = []
for op in options:
    if len(op) > 0:
        choices.append(op)

print "Choices are :"
for ch in choices:
    print ch

# Search google for filtered_ques
print "Searching...."
import operator
from googlesearch.googlesearch import GoogleSearch
response = GoogleSearch().search(filtered_ques)

filtered_results = []
for result in response.results:
    print result.title
    word_tokens = word_tokenize(result.title)
    for w in word_tokens:
        if w not in stop_words:
            filtered_results.append(w)
    try:
        word_tokens = word_tokenize(result.getText())
        for w in word_tokens:
            if w not in stop_words:
                filtered_results.append(w)
    except UnicodeEncodeError:
        pass

tf = {}
for o in range(len(choices)):
    tf[o] = 0

for o in range(len(choices)):
    ch = choices[o]
    c = ch.split()
    for ci in c:
        for fi in filtered_results:
            if ci == fi:
                tf[o] += 1

for o in range(len(choices)):
    print choices[o], ", Frequency: ", tf[o]

ans = max(tf.iteritems(), key=operator.itemgetter(1))[0]
freq = max(tf.iteritems(), key=operator.itemgetter(1))[1]
print "Answer is: ", choices[ans]
endtime = datetime.datetime.now()
diff = endtime - starttime
print "Time taken = ", diff.total_seconds()
