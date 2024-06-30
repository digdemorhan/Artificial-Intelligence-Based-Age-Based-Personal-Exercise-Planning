
#TRAIN DATASET'İ PYTHON KODLARIYLA OLUŞTURUP BUNU CSV DOSYASINA ÇEVİRECEĞİZ.


while True:
  try:
    #Yaş aralığı 20-40, minimum:20 ve maksimum:40
    var1 = int(input('Yaş (20-40 arasında): '))
    if var1 < 20 or var1 > 40:
      raise ValueError('Yaş 20 ile 40 arasında olmalıdır!')

    #Kilo aralığı 50-100, minimum:50 ve maksimum:100
    var2 = int(input('Kilo (50-100 arasında): '))
    if var2 < 50 or var2 > 100:
      raise ValueError('Kilo 50 ile 100 arasında olmalıdır!')

    #Cinsiyet değer seçim aralığı 1-0, kadın:1 ve erkek:0
    while True:
      var3 = input('Cinsiyet (Kadın:1, Erkek:0): ')
      if var3 in ['1', '0']:
        var3 = int(var3)
        break
      else:
        print('Hatalı değer girdiniz. Lütfen 1 (Kadın) veya 0 (Erkek) giriniz: ')

    #Egzersiz geçmişi değer seçim aralığı 1-0, egzersiz geçmişi var:1 ve egzersiz geçmişi yok:0
    while True:
      var4 = input('Egzersiz Geçmişi (Var:1, Yok:0): ')
      if var4 in ['1', '0']:
        var4 = int(var4)
        break
      else:
        print('Hatalı değer girdiniz. Lütfen 1 (var) veya 0 (yok) giriniz.')

  except ValueError as e:
    print(e)
    print('Lütfen tekrar deneyin.')
  else:
    print('Girilen Değerler:')
    print('Yaş:', var1)
    print('Kilo:', var2)
    print('Cinsiyet:', 'Kadın' if var3 == 1 else 'Erkek')
    print('Egzersiz Geçmişi:', 'Var' if var4 == 1 else 'Yok')
    break    


generalArr = []

#Numaralandırıcı tanımlayalım ve ilk değerini atayalım.
count = 0

for var1 in range(40, 45):
    for var2 in range(50, 101):
        for var3 in [0, 1]:
            for var4 in [0, 1]:
                if var3 == 1 and var4 == 1: 
                    total = str(var1) + ' yasinda ' + str(var2) + ' kilo ' + ' erkek ' + ' egzersiz gecmisi yok '
                    obj = {"text": total, "label": 4}
                    generalArr.append(obj)
                    count += 1

#Pandas kütüphanesini import edelim.
import pandas as pd 

#DataFrame'i oluşturalım.
df = pd.DataFrame(generalArr)

#Numaralandırıcıyı kaldıralım.
df.index = range(len(df))

#Değerleri CSV dosyasına yazalım.
df.to_csv('Training.csv', index=False)



