from gtts import gTTS
import pdfplumber

pdf_file = "how-to-start-a-business.pdf"

# Read the pdf file and attach each page text to a string into a list
texts_per_page = []
with pdfplumber.open(pdf_file) as pdf:
    pages = pdf.pages
    for page in pages:
        texts_per_page.append(page.extract_text())


# Generate MP3 from each item of the list
for i, text in enumerate(texts_per_page):
    to_speech = text
    language = 'en'
    myobj = gTTS(text=to_speech, lang=language, slow=False)
    myobj.save(f"page{i}.mp3")
