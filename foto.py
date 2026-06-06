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

def satın():
    kilo = int(input("kaç kilo aldınız⏲️"))
    tür = input("ne aldınız")
    tutar = katalog.get(tür)* kilo   #burda alınan kiloyu ve neyi aldığını öğrendik

    if tür not in katalog:  #burda eğer bizde olmayan bişey girildiyse uyarıyoruz
        print("malesef öyle  bişeyimiz yok")
    print(f"tutar bu kadar: {tutar}") #burda ödemeyi yazıyoruz
    vrln = int(input("lütfen paranzıı ödeyiniz")) # bruda parayı istedik

    if vrln ==tutar: # burda yeterli para verdimi diye kontrol ettik
        print("teşekkürler artık sizin")

    elif vrln <tutar:    # eğer az para verdiyse daha fazla istedik
        borç =  tutar - vrln
        son = int(input(f"lütfen {borç}tl  ödeyin:"))
        if son == borç: #burda ise verdiyse olayı bitirdik
            print("teşekkürler artık sizin")

    elif vrln > tutar: # eğerki kişi bize fazla verdiyse para üstü verdik
        üstü = vrln - tutar
        int(input(f"çok verdin aga al para üstün: {üstü}"))
    istek = input("çıkmak ister misiniz eğer öyle ise Z'ye basın değilse z dışı bişeye bas") # eğer çıkmak istenirse z basar kullanıcı eğer istemnez ise onun dışında bişeye basar

    if istek =="z" or istek =="Z": #burda çıkış yaptırdık z olması halinde
        quit("bay bay")





while True: # bura zaten döngümüz
    print("İNANILMAZ KAMPANYA PASTIRMA 6.06.2026 TARİHİNE KADAR 100TL💵")
    satın()
