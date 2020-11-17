dias = int(input())

anos = dias/365
meses = (dias % 365)/30
dias = (dias % 365)%30

print("{} ano(s)".format(int(anos)))
print("{} mes(es)".format(int(meses)))
print("{} dia(s)".format(int(dias)))