
# Atrast pozitīva skaitļa ciparu summu. Piemērs: 14214 => 12

x =input("Ievadi skaitli:")
sum=0
if int(x)<0:
    print("nav ievadits pozzetivs skaitlis")
else:
    for i in x:
        sum+=int(i)
print(f"skaitla {x} ciparu summa ir {sum}")