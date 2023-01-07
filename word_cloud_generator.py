# run <pip install wordcloud> beforehand
from wordcloud import WordCloud


wc = WordCloud()
wc.generate('hello world word cloud generator') # words for the cloud
wc.to_file('cloud.png') # save word cloud