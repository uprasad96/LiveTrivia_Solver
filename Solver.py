# Search phone directory for screenshot
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

print ques

# clean and remove stop words from Ques
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words('english'))
word_tokens = word_tokenize(ques)
filtered_ques = ""
for w in word_tokens:
    if w not in stop_words:
        filtered_ques += (w + " ")

print filtered_ques

options = ""
for i in xrange(end, len(text)):
    options += text[i]

options = options.split('\n')
choices = []
for op in options:
    if len(op) > 0:
        choices.append(op)

for ch in choices:
    print ch
