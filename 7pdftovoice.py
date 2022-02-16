# import pyttsx3
# speaker = pyttsx3.init()
# speaker.say('Hello Yashaswini')
# speaker.runAndWait()

import pyttsx3
import PyPDF2
book = open('1.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
for i in range(0,pages):

    speaker = pyttsx3.init()
    page = pdfReader.getPage(i)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()