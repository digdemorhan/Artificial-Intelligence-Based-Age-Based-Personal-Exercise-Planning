
#Python tabanlı web uygulamalar oluşturmak için Flask'ı ekleyelim.
from flask import Flask, render_template, request


#Veri setini yükleyip analiz edebilmek için Pandas kütüphanesini import edelim.
import pandas as pd

#Kelimelerimizi sayısal matrislere dönüştüren Scikit-learn'e ait CountVectorizer ekleyelim.
from sklearn.feature_extraction.text import CountVectorizer


#Text-classification işlemi için SVC kullanalım.
from sklearn.svm import SVC

##Eğitim veri setini yükleyelim.
train_data = pd.read_csv("Training.csv")
X_train = train_data["text"].values
y_train = train_data["label"].values

#CountVectorizer ile metinleri sayısal özelliklere dönüştürelim.
vectorizer = CountVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)

#Multinomial NaiveBayes modeli oluşturalım.
#model = MultinomialNB()

model = SVC(kernel='linear')

#Saysal veri ve eğitim verilerini modelin öğrenmesini sağlayalım.
model.fit(X_train_vectorized, y_train)

#Flask uygulamasını başlatarak ana nesnesini oluşturalım.
app = Flask(__name__)

#/ rotası için yönlendirme yapalım.
@app.route('/')
def index():
    return render_template('index.html')

#Classify rotası için POST isteği yapalım.
@app.route('/classify', methods=['POST'])

def classify():
    age = int(request.form['age'])
    weight = float(request.form['weight'])
    gender = request.form['gender'].lower()
    exercise_history = request.form['exercise_history'].lower()
    heartDisease = request.form['heartDisease'].lower()
    respiratoryDisease = request.form['respiratoryDisease'].lower()


    #Girilen verileri yazdıralım.
    input_text = f"Yaş: {age}, Kilo: {weight}, Cinsiyet: {gender}, Egzersiz Geçmişi: {exercise_history}, Kalp Rahatsızlığı: {heartDisease}, Solunum Yolu Rahatsızlığı: {respiratoryDisease}"

    #Kullanıcı girdisini transform yöntemiyle modelin anlayabileceği sayısal formata dönüştürelim.
    input_vectorized = vectorizer.transform([input_text])

    #Modelin anlayabileceği formatı sınıflandıralım.
    prediction = model.predict(input_vectorized)
    
    #Flask'te HTML isteğini işleyelim.
    return render_template('index.html', prediction=prediction[0])

#Flask'in doğru çalışıp çalışmadığını kontrol edelim.
if __name__ == '__main__':
    app.run(debug=True)

