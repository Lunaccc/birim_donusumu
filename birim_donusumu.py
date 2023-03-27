def birim_donusumu():

    birimler = {
        'km': 0.6214,
        'mi': 1.6093,
        'c': lambda x: x * 9/5 + 32,
        'f': lambda x: (x - 32) * 5/9,
        'kg': 2.2046,
        'lb': 0.4536,
        'm': 3.2808,
        'ft': 0.3048,
    }

    birim = input('Hangi birimi çevirmek istersiniz? (örn: km, mi, c, f, kg, lb, m, ft): ').lower()
    deger = float(input('Çevirmek istediğiniz değeri giriniz: '))

    if birim in birimler.keys():
        if birim in ['c', 'f']:
            sonuc = birimler[birim](deger)
        else:
            sonuc = deger * birimler[birim]
        print(f"{deger} {birim} = {sonuc:.2f} {'mi' if birim == 'km' else 'km' if birim == 'mi' else 'lb' if birim == 'kg' else 'kg' if birim == 'lb' else 'ft' if birim == 'm' else 'm' if birim == 'ft' else birim}")
    else:
        print("Hatalı birim. Lütfen geçerli bir birim girin.")

birim_donusumu()
