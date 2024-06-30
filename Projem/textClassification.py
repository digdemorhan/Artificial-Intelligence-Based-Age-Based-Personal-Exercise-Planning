
#Veri setini yükleyip analiz edebilmek için Pandas kütüphanesini import edelim.
import pandas as pd

#Kelimelerimizi sayısal matrislere dönüştüren Scikit-learn'e ait CountVectorizer ekleyelim.
from sklearn.feature_extraction.text import CountVectorizer


#Text-classification işlemi için SVC kullanalım.
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

#Eğitim veri setini yükleyelim.
train_data = pd.read_csv("Training.csv")
X_train = train_data["text"].values
y_train = train_data["label"].values

#Test veri setini yükleyelim.
test_data = pd.read_csv("Validate.csv")
X_test = test_data["text"].values
y_test = test_data["label"].values

#CountVectorizer ile metinleri sayısal özelliklere dönüştürelim.
vectorizer = CountVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

#SVM modeli oluşturalım.
model = SVC(kernel='linear')

#Sayısal veri ve eğitim verilerini modelin öğrenmesini sağlayalım.
model.fit(X_train_vectorized, y_train)

#Test verisi ile tahminler yapalım.
y_pred = model.predict(X_test_vectorized)

#Doğruluk oranını hesaplayalım.
accuracy = accuracy_score(y_test, y_pred)
print("Model Doğruluk Oranı:", accuracy)

#Sınıflandırma işlemi için fonksiyon oluşturalım.
def classify_exercise():
    # Kullanıcıdan veri girişi alalım.
    age = int(input("Yaşınızı girin: "))
    weight = float(input("Kilonuzu girin (kg): "))
    gender = input("Cinsiyetinizi girin (Erkek/Kadın): ").lower()
    exercise_history = input("Egzersiz geçmişiniz var mı? (Evet/Hayır): ").lower()
    heartDisease = input("Herhangi bir kalp rahatsızlığınız var mı? (Evet/Hayır):").lower
    respiratoryDisease = input("Herhangi bir solunum yolu rahatsızlığınız var mı? (Evet/Hayır):").lower

    # Girilen verileri yazdıralım.
    input_text = f"Yaş: {age}, Kilo: {weight}, Cinsiyet: {gender}, Egzersiz Geçmişi: {exercise_history}, Kalp Rahatsızlığı: {heartDisease}, Solunum Yolu Rahatsızlığı: {respiratoryDisease}"

    # Kullanıcı girdisini transform yöntemiyle modelin anlayabileceği sayısal formata dönüştürelim.
    input_vectorized = vectorizer.transform([input_text])

    # Modelin anlayabileceği formatı sınıflandıralım.
    prediction = model.predict(input_vectorized)

    # Sonucu ekrana yazdıralım.
    print("\n--- Tahmin Sonucu ---")
    print("Tahmin Edilen Kategori:", prediction[0])

# Sınıflandırma işlemini başlatalım.
classify_exercise()

