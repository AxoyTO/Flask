import re


def all_matches(text, pattern):
    print(pattern)
    regobj = re.compile(pattern)
    for m in regobj.finditer(text):
        print(str(m.start()) + '-' + str(m.end()) + ':' + text[m.start(): m.end()])


## xy'den sonra tekrarlayan her y
# all_matches('xyyxxxxxyyyyxxxxyy', 'xy*')

# xy ve daha sonra teklarlayan her y (+)
# all_matches('xyyxxxxxyyyyxxxxyy', 'xy+')

# x ve x'den sonra tekrarlayan her y (?)
# all_matches('xyyxxxxxyyyyxxxxyy', 'xy?')

# x'den sonra 2y
# all_matches('xyyxxxxxyyyyxxxxyy', 'xy{2}')

# x'den sonra en az 2y
# all_matches('xyyxxxxxyyyyxxxxyy', 'xy{2,}')

# x'den sonra en az 3 en fazla 4y
# all_matches('xyyxxxxxyyyyxxxxyy', 'xy{3,4}')

# x ya da y
# all_matches('xyyxxxxxyyyyxxxxyy', '[xy]')

# xy'den sonra x ya da y
# all_matches('xyyxxxxxyyyyxxxxyy', 'xy[xy]')

# nokta ve boşluk haricindeki her karakter
# all_matches('xx..y ..yyyxxx.. ', '[^. ]')

# noktalar ve boşluklar arasındaki stringler
# all_matches('xx..y ..yyyxxx.. ', '[^. ]+')

# A-Z arasındaki herhangi bir harfin 0-9 arasındaki herhangi bi sayıyla devamı
# all_matches('A94B2c4 xyz08', '[A-Z][0-9]')

# A-Z veya a-z arasındaki herhangi bir harfin 0-9 arasındaki herhangi bi sayıyla devamı
# all_matches('A94B2c4 xyz08', '[A-Za-z][0-9]')

# S'den sonra gelen ilk karakter
# all_matches('Silk road SZ', 'S.')

# S'den sonra gelen string
# all_matches('What is Silk Road', 'S.+')

# S'den sonra gelen stringdeki son k ile biten string
# all_matches('What is Silk Roadk', 'S.+k')

# Sadece rakamlar
# all_matches('This is the 1-st and 2-nd example', r'\d+')

# Rakamlar harıç her şey
# all_matches('This is the 1-st and 2-nd example', r'\D+')

# Sadece boşluk
# all_matches('This is the 1-st and 2-nd example', r'\s+')

# Boşluk hariç her şey
# all_matches('This is the 1-st and 2-nd example', r'\S+')

# İşaretler ve boşluk vb. hariç her şey(Alfa-numerik)
# all_matches('This is the 1-st and 2-nd example', r'\w+')

# İşaretler ve boşluk
# all_matches('This is the 1-st and 2-nd example!', r'\W+')

# ilk kelime boşluk ya da sembole kadar
# all_matches('Relative positioning in regular expression!', r'^\w+')

# ilk kelime(boşluk ya da sembole kadar)
# all_matches('Relative positioning in regular expression!', r'\A\w+')

# son kelime(boşluk ya da sembole kadar)
# all_matches('Relative positioning in regular expression', r'\w+$')

# son kelime(boşluk ya da sembole kadar)
# all_matches('Relative positioning in regular expression', r'\w+\Z')

# b(harf) -> r, yani ilk r harfi
# all_matches('Relative positioning in regular expression', r'\br')

# Kelimenin ortasındaki g harfi
all_matches('Relative positioning in regular expression', r'\Bg\B')
