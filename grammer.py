from textblob import TextBlob
a= TextBlob("Heklo, geod mornng")
a=a.correct()
print(a)