
# Atrast cik skaitļi norādītajā intervālā dalās ar lietotāja norādīto dalītāju.

start=int(input("sakuma vertiba:"))
end=int(input("beigu vertiba:"))
dala=int(input("Dalitaja vertiba:"))

cik=0

for i in range(start,end+1):
    if i%dala==0:
        cik+=1

print(f"{cik} skaiti ir starp {start} un {end}, kas dalas ar {dala}.")
