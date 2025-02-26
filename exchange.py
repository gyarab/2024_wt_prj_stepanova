import httpx

url = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt?date=13.02.2025"
r = httpx.get(url)

lines = r.text.split("\n")

row = ""
for line in lines:
    if "|EUR|" in line:
        row = line

row_arr = row.split("|")
kurz_str = row_arr[-1]
kurz_str = kurz_str.replace(",", ".")
kurz = float(kurz_str)

print("1 = EUR -> CZK, 2 = CZK -> EUR")
choice = input("Vyberte typ konverze: ")

amount = float(input("Zadejte částku: "))

if choice == "1":
    result = amount * kurz  
    print(f"{amount} EUR = {result} CZK")
elif choice == "2":
    result = amount / kurz  
    print(f"{amount} CZK = {result} EUR")
else:
    print("Neplatná volba.")