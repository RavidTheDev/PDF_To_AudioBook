from PyPDF2 import PdfReader
import requests
import config


voice_url="http://api.voicerss.org/?"
API_KEY=config.API_KEY
LNG="en-us"


file=config.file

PDF_file=open(file,'rb')

reader=PdfReader(file)
num_of_pages=len(reader.pages)

text=reader.pages[0].extract_text()


tts_params={
    "key":API_KEY,
    "src":text,
    "hl":LNG,
    "v":"John",
    "c":"MP3"
}

response=requests.get(url=voice_url,params=tts_params)
with open('audiobook.mp3', 'wb') as audiobook:
    audiobook.write(response.content)
