from wordcloud import WordCloud,STOPWORDS
import wikipedia
from PIL import Image

stop_w = set(STOPWORDS)
content = wikipedia.summary("Python Programming Language")
# f=open("aman.txt","r")
# content = f.read()
# print(content)
word_cloud = WordCloud(stopwords=stop_w).generate(content)
img = word_cloud.to_image()
img.show()