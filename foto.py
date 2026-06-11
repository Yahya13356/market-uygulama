import random
from time import sleep
import keyboard
#katalog diye sözlük oluşturduk
katalog = {
    "ceviz":30,
    "cevız":30,
    "cezıv":30,
    "pastıma":100,
    "pastırma":100,
    "pastıtma":100,
    "muz":28,
    "mul":28,
    "mzu":28
}
bakiye = 100
def satın():
    global bakiye
    kilo = int(input("kaç kilo aldınız⏲️"))
    tür = input("ne aldınız")
    tutar = katalog.get(tür)* kilo   #burda alınan kiloyu ve neyi aldığını öğrendik
    if bakiye < tutar:
        gerek = tutar - bakiye
        print(f"paran yetmiyor aga işlem {tutar}'kadardı ama sende {bakiye}'kadar vardı yani sana {gerek}'kadar para lazım")
        return



    if tür not in katalog:  #burda eğer bizde olmayan bişey girildiyse uyarıyoruz
        print("malesef öyle  bişeyimiz yok")
    print(f"tutar bu kadar: {tutar}") #burda ödemeyi yazıyoruz
    vrln = int(input("lütfen paranzıı ödeyiniz")) # bruda parayı istedik

    if vrln ==tutar: # burda yeterli para verdimi diye kontrol ettik
        bakiye -= vrln
        print("teşekkürler artık sizin")

    elif vrln <tutar:    # eğer az para verdiyse daha fazla istedik
        borç =  tutar - vrln
        bakiye -= vrln
        son = int(input(f"lütfen {borç}tl  ödeyin:"))
        if son == borç: #burda ise verdiyse olayı bitirdik
            bakiye -= son
            print("teşekkürler artık sizin")

    elif vrln > tutar: # eğerki kişi bize fazla verdiyse para üstü verdik
        üstü = vrln - tutar
        int(input(f"çok verdin aga al para üstün: {üstü}"))
    istek = input("çıkmak ister misiniz eğer öyle ise Z'ye basın değilse z dışı bişeye bas") # eğer çıkmak istenirse z basar kullanıcı eğer istemnez ise onun dışında bişeye basar

    if istek =="z" or istek =="Z": #burda çıkış yaptırdık z olması halinde
        quit("bay bay")




def parakazan():   # bu fonksiyon para kazanmak için
    global bakiye  #abkiye yi heryerde kullanmak için böyle yaptım
    print("para kazanma yerine hoş geldin ne oynayacaksın"
          "1)çark çevir"
          "2)20 saniye bekle 5 tl kazan"
          "3)şans oyunu oyna ve 1000 tl kazanma şansı yakala")
    print("*"*90)
    mal = int(input("seçim senin"))
    if mal ==1: # eğer 1 tıklarsa rastgele para kazanır
        kazanç = random.randint(1,40)
        bakiye += kazanç
        print(f"helal olsun {kazanç}TL kazandın şimdiki bakiyen {bakiye}TL ")
    elif mal ==2: # eğer 2 ye tıklarasa 20 saniye bekler ve 5 tl kazanır
        sleep(20)
        kazan = 5
        bakiye += kazan
        print(f"helal oslun sabırlısın paran {bakiye}TL")
    elif mal ==3:      # kasa her zaman kazanır
        çık = random.randint(1,100)
        bakiye -= çık
        print("ahh dostum çok yakındık nerdeyse kazanıyorduk bir daha oynarsan kazanabilirsin belki büyük ödül 1000tl")
        print(f"paran bu arada {bakiye}")




while True: # bura zaten döngümüz
    print("İNANILMAZ KAMPANYA PASTIRMA 6.06.2026 TARİHİNE KADAR 100TL💵")
    try:   #try içine aldık çünkü uygulam çökerdi ama artık çökmeyecek tabi başlangıçta

        sçm = int(input("""
            ne yapmak istersin
            1) alışveriş
            2) para kazan ----->"""))

    except ValueError:
        print("olmadı bu")
    try:   #burasıda aynı mantık çökmemesi için ama bunlar def içine de girmeli

        if sçm ==1:
            satın()
        elif sçm ==2:
            parakazan()
    except NameError:
        print("yine yanlış girdin")
    else:
        print("kral öyle bir seçenek yok")


ıjorg