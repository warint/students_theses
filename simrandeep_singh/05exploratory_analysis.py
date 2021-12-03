
import nltk
nltk.download('stopwords')
import io
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from nltk.corpus import stopwords
from collections import  Counter
from sklearn.feature_extraction.text import CountVectorizer

stop_words = set(stopwords.words('english'))

yearlist=[1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021]
for a in yearlist:
    filename= str(a) + ".txt"
    filename2= str(a) + "filteredtext.txt"
    file1 = open(filename2, encoding="utf-8")
    line = file1.read()
    words = line.split()
    df= pd.Series(words)
    file2 = open(filename, encoding="utf-8")
    line2 = file2.read()
    words2 = line2.split()
    df1= pd.Series(words2)

    def plot_top_non_stopwords_barchart(text):
        stop=set(stopwords.words('english'))
        
        new= text.str.split()
        new=new.values.tolist()
        corpus=[word for i in new for word in i]

        counter=Counter(corpus)
        most=counter.most_common()
        x, y=[], []
        for word,count in most[:40]:
            if (word not in stop):
                x.append(word)
                y.append(count)
                
        sns.barplot(x=y,y=x)
        plt.savefig(str(a)+ '_top_nonstop_words.png',bbox_inches='tight')
        plt.close()
    plot_top_non_stopwords_barchart(df)


    #PLOTTING N GRAMS FOR N=2 AND N=3
    def plot_top_ngrams_barchart(text, n=2):
        stop=set(stopwords.words('english'))

        new= text.str.split()
        new=new.values.tolist()
        corpus=[word for i in new for word in i]

        def _get_top_ngram(corpus, n=None):
            vec = CountVectorizer(ngram_range=(n, n)).fit(corpus)
            bag_of_words = vec.transform(corpus)
            sum_words = bag_of_words.sum(axis=0) 
            words_freq = [(word, sum_words[0, idx]) 
                          for word, idx in vec.vocabulary_.items()]
            words_freq =sorted(words_freq, key = lambda x: x[1], reverse=True)
            return words_freq[:10]

        top_n_bigrams=_get_top_ngram(text,n)[:10]
        x,y=map(list,zip(*top_n_bigrams))
        sns.barplot(x=y,y=x)
        plt.savefig(str(a)+ '_n=2gram.png',bbox_inches='tight')
        plt.close()
    plot_top_ngrams_barchart(df,2)
    
    def plot_top_ngrams_barchart(text, n=2):
        stop=set(stopwords.words('english'))

        new= text.str.split()
        new=new.values.tolist()
        corpus=[word for i in new for word in i]

        def _get_top_ngram(corpus, n=None):
            vec = CountVectorizer(ngram_range=(n, n)).fit(corpus)
            bag_of_words = vec.transform(corpus)
            sum_words = bag_of_words.sum(axis=0) 
            words_freq = [(word, sum_words[0, idx]) 
                          for word, idx in vec.vocabulary_.items()]
            words_freq =sorted(words_freq, key = lambda x: x[1], reverse=True)
            return words_freq[:10]

        top_n_bigrams=_get_top_ngram(text,n)[:10]
        x,y=map(list,zip(*top_n_bigrams))
        sns.barplot(x=y,y=x)
        plt.savefig(str(a)+ '_n=3gram.png',bbox_inches='tight')
        plt.close()
    plot_top_ngrams_barchart(df,3)
    


    #PLOTTING TOP STOP WORDS IN TEXT
        
    def plot_top_stopwords_barchart(text):
        stop=set(stopwords.words('english'))
        
        new= text.str.split()
        new=new.values.tolist()
        corpus=[word for i in new for word in i]
        from collections import defaultdict
        dic=defaultdict(int)
        for word in corpus:
            if word in stop:
                dic[word]+=1
                
        top=sorted(dic.items(), key=lambda x:x[1],reverse=True)[:10] 
        x,y=zip(*top)
        plt.bar(x,y)
        plt.savefig(str(a)+ '_top_stop_words',bbox_inches='tight')
        plt.close()

    plot_top_stopwords_barchart(df1)





    #WORD NUMBER HISTOGRAM


    def plot_word_number_histogram(text):
        text.str.split()
        map(lambda x: len(x))
        plt.hist()
        plt.show()
            
            
        
    #plot_word_number_histogram(df)

    #WORD LENGTH HISTOGRAM

    import numpy as np

    def plot_word_length_histogram(text):
        text.str.split().\
            apply(lambda x : [len(i) for i in x]). \
            map(lambda x: np.mean(x)).\
            hist()

    #plot_word_length_histogram(df)



