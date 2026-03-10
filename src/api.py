import os
import json
from pathlib import Path

class TipoOperacao:
    def __init__(self, a):
        self.a = a

    def tipos(self, tipos):
        match tipos: 
            case 1: 
                return "+"
            case 2:
                return "-"
            case 3:
                return "/"
            case 4: 
                return "x"
            case 5: 
                return "**"
            case _:
                return "Opção inválida"
class Operacoes:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def mais(self):
        return self.a + self.b 
    
    def menos(self):
        return self.a - self.b
    
    def dividir(self):
        return self.a / self.b 
    
    def vezes(self):
        return self.a * self.b
    
    def potencia(self):
        return self.a ** self.b

def resultado(operacao, a, b):
    calc = Operacoes(a, b)

    match operacao: 
        case 1: 
            return calc.mais()
        case 2:
            return calc.menos()
        case 3:
            return calc.dividir()
        case 4: 
            return calc.vezes()
        case 5: 
            return calc.potencia()
        case _:
            return "Opção inválida"
        
class Historico:
    def mostrar_historico():
        try:
            with open("resultados/calculo.txt", "r") as arquivo:
                print("\n=== HISTÓRICO DE CÁLCULOS ===\n")
                print(arquivo.read())
        except FileNotFoundError:
            print("Nenhum histórico encontrado.")

    def limpar_historico():
        open("resultados/calculo.txt", "w").close()
        return "Histórico limpo com sucesso."

    def ultima_operacao():
        with open("resultados/historico.json", "r") as f:
            historico = json.load(f)

        if not historico:
            return {"mensagem": "Histórico vazio"}

        return historico[-1]

    def limpar():
        os.system("cls" if os.name == "nt" else "clear")

    def total_calculos():
        with open("resultados/calculo.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            print("Total de operações: ", len(linhas))

    def exportar_historico():
        try:
            with open("resultados/calculo.txt", "r") as origem:
                dados = origem.read()

            with open("resultados/backup_calculos.txt", "w") as destino:
                destino.write(dados)

            print("Histórico exportado com sucesso!")

        except FileNotFoundError:
            print("Não existe histórico para exportar.")

    def estatistica():
        try:
            with open("resultados/calculo.txt", "r") as arquivo:
                linhas = arquivo.readlines()

            soma = 0
            sub = 0
            mult = 0
            div = 0
            pot = 0

            for linha in linhas:

                if "+" in linha:
                    soma += 1
                elif "-" in linha:
                    sub += 1
                elif "x" in linha:
                    mult += 1
                elif "/" in linha:
                    div += 1
                elif "**" in linha:
                    pot += 1

            print("\n=== ESTATÍSTICAS ===")
            print(f"Somas: {soma}")
            print(f"Subtrações: {sub}")
            print(f"Multiplicações: {mult}")
            print(f"Divisões: {div}")
            print(f"Potências: {pot}")
            print(f"Total de cálculos: {len(linhas)}")

        except FileNotFoundError:
            print("Nenhum histórico encontrado.")

    def res_historico(res):
        match res: 
            case 1: 
                return Historico.limpar_historico()
            case 2:
                return Historico.ultima_operacao()
            case 3:
                return Historico.total_calculos()
            case 4: 
                return Historico.estatistica()
            case 5: 
                return Historico.exportar_historico()
            case _:
                return "Opção inválida"
            
    def salvar_operacao(dados):
        os.makedirs("resultados", exist_ok=True)
        with open("resultados/historico.json", "r") as f: 
            historico = json.load(f)

        historico.append(dados)

        with open("resultados/historico.json", "w") as f: 
            json.dump(historico, f, indent=4)