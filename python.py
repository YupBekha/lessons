"""yoshlar = int(input("Yoshingiz nechida? " ))
if yoshlar < 4:
    print("Siz uchun bepul")
elif yoshlar < 12:
    print("Siz uchun kirish narxi 5 000 so'm")
elif yoshlar < 18:
    print("Siz uchun kirish narxi 10 000 so'm")
else:
    print("Siz uchun kirish narxi 15 000 so'm")
        """
        
        
        
        

#yoshlar = int(input("Yoshingiz nechida? " ))
#if yoshlar <= 4:
#    narh = 0
#elif yoshlar <= 12:
#    narh = 5000
#elif yoshlar <= 18:
#    narh = 10000
#else:
#    narh = 15000
#print(f"Siz uchun kirish narxi {narh} so'mni tashkil etadi")


#kun = input("Bugun qanaqa kun? ")
#if kun.lower()=='shanba' or kun.lower()=="yakshanba":
#    print("Bugun dam olish kuni")
#else:
#    print("Bugun ish kuni")


#kun = input("Bugun nima kun? ")
#harorat = float(input('Bugun havo harorati nechchi? '))
#if kun.lower()=="shanba" or 'yakshanba' and harorat >= 30:
#    print("Qani ketdik cho'milishga")
#elif kun.lower()=="shanba" or 'yakshanba' and harorat <= 30:
#    print("Uyda qolamiz")
#elif kun.lower()=="dushanba" or 'seshanba' or 'chorshanba' or 'payshanba' or 'juma' and harorat <= 30 or harorat >= 30:
#    print("Ishga sur")
#else:
#    print('Bilganingni qile')

#narh = 15000
#salat = True
#choy = False 
#if choy and salat:
#    narh = narh + 10000
#elif choy or salat:
#    narh = narh + 5000
#print(f"Jami {narh} so'm")

#narh = 10000
#salat = True
#non = True
#kompot = False
#assorti = True
#fanta = False
#if salat:
#    narh = narh + 7000
#if non:
#    narh = narh + 3500
#if kompot:
#    narh = narh = 8000
#if assorti:
#    narh = narh + 12000
#if fanta:
#    narh = narh + 10000
#
#print(f"Jami {narh} so'm")
#

#menu = ['osh', 'manti', 'kabob', 'barak']
#ovqat = input('Nima ovqat yeysiz? ')
#
#if ovqat.lower() in menu:
#    print("Buyurtma qabul qilindi.")
#else:
#    print(f"Uzur menuda '{ovqat}' yo'q ekan. ")

"""buyurtmalar = ['osh', 'manti', 'kabob', 'barak']
menu = ['osh', 'manti', 'kabob', 'barak', 'shashlik', 'honim']
taom = []
#for taom in menu:
#    if taom in buyurtmalar:
#        print(f"Menuda {taom} bor")
#    else:
#        print(f"menida {taom} yo'q")
if buyurtmalar:
    print(f"royxatda {len(buyurtmalar)} ta buyurtma bor.")
else:
    print("royxar bo'sh")"""

#car = {'rangi':'Qizil', 'model':'Ferrari', 'turi':'supercar' }
#print(car['rangi'])
#print(car['model'])
#print(car['turi'])

#uz_en = {'noutbuk':'laptop', 'olma':'apple', 'mouse':'sichqon'}
#print(uz_en['noutbuk'])

#talaba_0 = {'ism':'murod olimov','yosh':20,'t_yil':2000}
#talaba_0['kurs'] = 4 # yangi, 'kurs' nomli kalit so'zga 4 qiymatini yuklaymiz
#talaba_0['fakultet'] = 'informatika' # 'fakultet' ga esa 'informatika' 
#print(f"{talaba_0['ism'].title()},\
#{talaba_0['t_yil']}-yilda tu'gilgan,\
#{talaba_0['yosh']} yoshda, \
#{talaba_0['kurs']}-kurs,\
#{talaba_0['fakultet']} fakulteti")
 
#telefonlar = {
#    'ali':'iphone x',
#    'vali':'galaxy s9',
#    'olim':'mi 10 pro',
#    'orif':'nokia 3310'
#    }
#
#phone = telefonlar.get('hasan','Bunday ism mavjud emas')

#talaba_0 = {
#    'Ism' : 'Ali',
#    'Yosh' : '22',
#    'Manzil' : 'Samarqand'
#    }
#
#for kalit, qiymat in talaba_0.items():
#    print(f"Kalit: {kalit}")
#    print(f"Qiymat: {qiymat} \n")

#telefonlar = {
#    'ali':'iphone x',
#    'vali':'galaxy s9',
#    'olim':'mi 10 pro',
#    'orif':'nokia 3310'
#}
#
#for k, v in telefonlar.items():
#    print(f"{k}ning telefoni: {v}")


#mahsulotlat = {
#    'olma' : 10000,
#    'anor' : 20000,
#    'limon' : 5000,
#    'shaftoli' : 50000
#}
#
#for mahsulot in mahsulotlat.keys():
#    print(mahsulot.title())

#mahsulotlat = {
#    'olma' : 10000,
#    'anor' : 20000,
#    'limon' : 5000,
#    'shaftoli' : 50000
#}
#
#for mahsulot in mahsulotlat.values():
#    print(mahsulot)


telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310',
    'hamida':'galaxy s9',
    'maryam':'huawei p30',
    'tohir':'iphone x',
    'umar':'iphone x'    
    }

print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
for tel in set(telefonlar.values()):
    print(tel)