from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
nltk.download('punkt')
import io
yearlist=[1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021]
stop_words = set(stopwords.words('english'))

for x in yearlist:
    filename= str(x) + ".txt"
    filename2= str(x) + "filteredtext.txt"
    file1 = open(filename, encoding="utf-8")
    print("reading pdfs from year:", filename)
    line = file1.read() 

    words= line.split()
    filtered_sentence = [] 
    lemma_word = []
    lower_word=[]
    wordnet_lemmatizer = WordNetLemmatizer()
    for w in words:
        appendFile = open(filename2,'a', encoding="utf-8")
        if w not in stop_words:
            a=w.lower()
            word1 = wordnet_lemmatizer.lemmatize(a, pos = "n")
            word2 = wordnet_lemmatizer.lemmatize(word1, pos = "v")
            word3 = wordnet_lemmatizer.lemmatize(word2, pos = ("a"))
            appendFile.write(" " + word3)
            appendFile.close()


        
