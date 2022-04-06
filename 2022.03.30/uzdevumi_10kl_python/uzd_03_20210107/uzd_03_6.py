
# Izveidot reizināšanas tabulu lietotāja ievadītam skaitlim.
x= int(input("Ievadi skaitli:"))
if x<0:
    print("ar 0 nevar reizinat")
else:
    for i in range(10):
        print(f"{x}*{i+1}={x*(i+1)}")