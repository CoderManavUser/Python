from textblob import TextBlob
blob=TextBlob("Hola amigos")
print(blob.detect_language())
print(blob.translate(to='en'))
print(blob.translate(to='zh'))
print(blob.translate(to='es'))