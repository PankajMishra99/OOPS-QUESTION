import string
import nltk
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
from nltk.corpus import stopwords
import pandas as pd
nltk.download('stopwords')

class TextPreprocessor:
    def __init__(self):
        self.stop_words=set(stopwords.words('english'))

    
    def text_preprocessing(self,text):
        text=text.lower()
        text=text.translate(str.maketrans('','',string.punctuation))
         # removing stopword..
        tokens =[word for word in text.split() if word not in self.stop_words]
        return ' '.join(tokens)

class Featureextraction:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
    
    def fit_transform(self,corpus):
        return self.vectorizer.fit_transform(corpus)
    
    def transform(self,texts):
        return self.vectorizer.transform(texts)

class SentimentAnalyzer:
    def __init__(self):
        self.model = LogisticRegression()    
    def train(self,x,y):
        self.model.fit(x,y)
    
    def predict(self,text_feature):
        return self.model.predict(text_feature)

if __name__=="__main__":
    data = {
        "review": [
            "This phone is amazing, I love the camera!",
            "Worst purchase ever, battery drains fast.",
            "Excellent quality and fast delivery.",
            "Terrible product, completely useless.",
            "Very satisfied with the laptop performance.",
        ],
        "sentiment": ["positive", "negative", "positive", "negative", "positive"],
    }
    df=pd.DataFrame(data)
    # print(df)
    preporcessor = TextPreprocessor()
    
    df['cleaned']=df['review'].apply(preporcessor.text_preprocessing)
    # print(df)
    extractor = Featureextraction()
    x=extractor.fit_transform(df['cleaned'])
    y=df['sentiment']
    # train test split..
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2, random_state=42)

    analyzer= SentimentAnalyzer()
    analyzer.train(x_train,y_train)
    y_pred = analyzer.predict(x_test)
    # print('Accuracy : ',y_test,y_pred)

    new_text = "The phone works perfectly and battery is great!"
    clean_review = preporcessor.text_preprocessing(new_text)
    feature = extractor.transform([clean_review])
    prediction = analyzer.predict(feature)
    print(prediction[0])


    