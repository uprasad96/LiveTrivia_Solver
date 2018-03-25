# LiveTrivia_Solver
How to use
1. Install all the neccessary libraries. This involves heavy usage of cv2, Pillow, pytesseract, pyautogui, nltk.
2. Install the app Screencast in your android phone.
3. Open any trivia game such as Loco, Iq Live, BrainBazzi, etc.
4. Cast your phone's screen using the Screencast app on the browser's local url.
5. Split the computer screen into two such that the phone's mirrored cast is on the left and the terminal is on the right.
6. Run python Solver.py.
7. It will crop the question and choices from the cast and apply an OCR, pytesseract (google's tesseract engine for python).
8. It then segments the question and the diffrent choices. It then filters the question of the stopwords for relevant keywords    search.
9. It will use a google api and search 10 webpages with their content for the filtered question.
10. It will then look for term frequency of the given choices in the retrieved search results.
11. It then returns the choice with the maximum term frequency which is probably the answer.
