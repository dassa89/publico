n_linhas = int(input("Numero de linhas:"))

n_colunas = int(input("Numero de colunas:"))

tabela = []
cont = 0
numero = 0
tabela.append("<table>")
for linha in range(n_linhas):
    tabela.append("<tr>")
    while cont < n_colunas:
        cont += 1
        numero += 1
        tabela.append("<td>")
        tabela.append(numero)
        tabela.append("</td>")

    tabela.append("</tr>")
    cont = 0
tabela.append("</table>")

tabela = "".join(map(str, tabela))
print(tabela)
