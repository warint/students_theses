from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
nltk.download('punkt')
import io
import gensim
from gensim import corpora
import pprint
from gensim.utils import simple_preprocess
import pyLDAvis
import pyLDAvis.gensim_models as gensimvis
from wordcloud import WordCloud, STOPWORDS
stopwords = set(STOPWORDS)
import matplotlib.pyplot as plt
from textblob import TextBlob
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

yearlist=[1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2020,2021]
for x in yearlist:
    filename= str(x) + ".txt"
    filename2= str(x) + "filteredtext.txt"
    Dictionary= {}
    file3 = open(filename2, encoding="utf-8")
    line3 = file3.read()
    words3 = line3.split()
    print("tokenization starts")
    doc_tokenized = [simple_preprocess(doc) for doc in words3]
    df = pd.Series(words3)
    dictionary= corpora.Dictionary()
    BoW_corpus = [dictionary.doc2bow(doc, allow_update=True) for doc in doc_tokenized]
    print("lda model")
    lda_model = gensim.models.ldamodel.LdaModel(BoW_corpus,num_topics = 4,id2word = dictionary, 
                                       passes = 10)
    print("lda model show")
    print(lda_model.show_topics())
    print("visualisation")
    visualisation = gensimvis.prepare(lda_model, BoW_corpus, dictionary)
    pyLDAvis.save_html(visualisation, str(x) +'_LDA_Visualization.html')

    def show_wordcloud(data):
        wordcloud = WordCloud(
            background_color='white',
            stopwords=stopwords,
            max_words=100,
            max_font_size=30,
            scale=3,
            random_state=1)
       
        wordcloud=wordcloud.generate(str(data))

        fig = plt.figure(1, figsize=(12, 12))
        plt.axis('off')

        plt.imshow(wordcloud)
        plt.savefig(str(x) + '_wordcloud.png',bbox_inches= 'tight')
        plt.close()

    show_wordcloud(doc_tokenized)

    ##sentiment analysis
    def plot_polarity_histogram(text):
        
        def _polarity(text):
            return TextBlob(text).sentiment.polarity
            
        polarity_score =text.apply(lambda x : _polarity(x))
        

        polarity_score.hist()
        plt.savefig(str(x) + "_polarity_histogram.png",bbox_inches= 'tight')
        plt.close()
        
    plot_polarity_histogram(df)


    #sentiment neutral negative bar chart
    def sentiment_vader(text, sid):
        ss = sid.polarity_scores(text)
        ss.pop('compound')
        return max(ss, key=ss.get)

    def sentiment_textblob(text):
            x = TextBlob(text).sentiment.polarity
            
            if x<0:
                return 'neg'
            elif x==0:
                return 'neu'
            else:
                return 'pos'

    def plot_sentiment_barchart(text, method='TextBlob'):
        if method == 'TextBlob':
            sentiment = text.map(lambda x: sentiment_textblob(x))
        elif method == 'Vader':
            nltk.download('vader_lexicon')
            sid = SentimentIntensityAnalyzer()
            sentiment = text.map(lambda x: sentiment_vader(x, sid=sid))
        else:
            raise ValueError('Textblob or Vader')
        
        plt.bar(sentiment.value_counts().index,
                sentiment.value_counts())
        plt.savefig(str(x) + "_sentiment_vader.png",bbox_inches= 'tight')
        plt.close()
    plot_sentiment_barchart(df, method='Vader')




