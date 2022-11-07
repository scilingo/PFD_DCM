arquivo_backup = ["IMG0001.PDF", "IMG0002.DCM", "IMG0003.DCM", "IMG0004.PDF", "IMG0005.PDF"]
arquivo_sistema = ["IMG0001.PDF", "IMG0002.DCM", "IMG0003.PDF"]

print("O total de arquivos no backup é de:", len(arquivo_backup), "arquivos")
print("O total de arquivos no sistema é de:", len(arquivo_sistema), "arquivos")

print("Os arquivos que contém no backup e no sistema são: ")
for arq1 in arquivo_backup:
    if arq1 in arquivo_sistema:
        print(arq1)

print("Os arquivos que faltam são: ")
for arq1 in arquivo_sistema:
    if arq1 in arquivo_backup:
        arquivo_backup.remove(arq1)
for arq1 in arquivo_backup:
    print(arq1)


