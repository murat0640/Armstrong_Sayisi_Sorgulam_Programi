print(""""
Armstrong Sayisi Sorguma Progaramina Hosgeldiniz
""")

x=raw_input("Sorgulanmasini istediginiz sayiyi giriniz:")
basamak_sayisi=len(x)
x=int(x)

a=0
b=0

y=x
while (y>0):
    a=y%10
    b+= a**basamak_sayisi
    y //= 10

if (b==x):
    print(x,"sayisi bir armstrong sayisidir.")
else :
    print(x,"sayisi bir armstrong sayisi degildir.")