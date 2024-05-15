# 1) taskınız ilk olaraq bir text faylı yaradıb içərisinə istədiyiniz bir cümlə yazırsınız .
# 2) daha sonra həmin textin ilk sətrindəki  sözlərin bütün hərflərini böyük hərflərə çeviririk .
# 3) Ən sonda bu sözləri başqa  bir text faylı yaradıb onun içərisində yazırıq.
with open("cumle.txt","w", encoding = "utf-8") as file:
    cumle = "nuray ismayilova\n"
    file.write(cumle)

with open("cumle.txt","r",encoding="utf-8") as file:
        
    boyuk = file.readline().capitalize()
    # print(boyuk)
with open("cumle2.txt","w",encoding="utf-8") as file:
    file.write(boyuk)
    