from src.api import Operacoes, resultado, TipoOperacao, Historico
from time import sleep
from datetime import datetime
from src.logger import logger
from colorama import Fore, Style
from pathlib import Path
import sys, os

BASE_DIR = Path(__file__).resolve().parent.parent
CAMINHO = BASE_DIR / "resultados" / "historico.json"


sys.set_int_max_str_digits(10000)

def exibir_corpo():
    while True:
        os.makedirs("resultados", exist_ok=True)
        horario = datetime.now()
        hor_format = horario.strftime("%d/%m/%Y %H:%M:%S")
        # Menu
        Historico.limpar()
        print("\n")
        print(Fore.CYAN + "+" + "-" * 28 + "+")

        print(Fore.CYAN + "|" + "CALCULADORA".center(28) + "|")

        print(Fore.CYAN + "+" + "-" * 28 + "+")

        print(Fore.CYAN + "| [ 1 ] Adição".ljust(29) + "|")
        print(Fore.CYAN + "| [ 2 ] Subtração".ljust(29) + "|")
        print(Fore.CYAN + "| [ 3 ] Divisão".ljust(29) + "|")
        print(Fore.CYAN + "| [ 4 ] Multipliacação".ljust(29) + "|")
        print(Fore.CYAN + "| [ 5 ] Potenciação".ljust(29) + "|")
        print(Fore.CYAN + "| [ 6 ] Histórico".ljust(29) + "|")
        print(Fore.CYAN + "+" + "-" * 28 + "+\n" + Style.RESET_ALL)
        

        # Verificar operação
        try:
            ope = int(input("| Escolha uma opção: "))
        except ValueError:
            print("\n\033[31mOpção inválida\033[0m")
            continue
        
        except KeyboardInterrupt:
            print(Fore.RED +"\nPrograma encerrado."+ Style.RESET_ALL)
            sleep(1)
            break     
        
        if ope not in [1, 2, 3, 4, 5, 6]:
                print("\n\033[31mOpção inválida\033[0m")
                continue
        
        print("="*30)

            # Escolha Histórico
        if ope == 6:
            while True:
                Historico.limpar()
                print(Fore.CYAN + "+" + "-" * 28 + "+")
                print(Fore.CYAN + "|" + "HISTÓRICO".center(28) + "|")
                print(Fore.CYAN + "+" + "-" * 28 + "+")
                print(Fore.CYAN + "| [ 1 ] Limpar histórico".ljust(29) + "|")
                print(Fore.CYAN + "| [ 2 ] Última operação".ljust(29) + "|")
                print(Fore.CYAN + "| [ 3 ] Total de calculos".ljust(29) + "|")
                print(Fore.CYAN + "| [ 4 ] Estatisticas".ljust(29) + "|")
                print(Fore.CYAN + "| [ 5 ] Exportar histórico".ljust(29) + "|")
                print(Fore.CYAN + "| [ 6 ] Voltar".ljust(29) + "|")
                print(Fore.CYAN + "+" + "-" * 28 + "+\n" + Style.RESET_ALL)

                try:
                    op_hist = int(input("Escolha uma opção: "))
                except ValueError:
                    print("\n\033[31mOpção inválida\033[0m")
                    continue

                if op_hist == 6:
                    Historico.limpar()
                    break
                
                print("+" + "-" * 28 + "+")
                print("\033[1;32mRESULTADO\033[m".center(39))
                print("+" + "-" * 28 + "+")
                res = Historico.res_historico(op_hist)
                input("\nPressione Enter para continuar...")
                Historico.limpar()

                logger.info("Nova alteracao no HISTORICO")
                logger.info(f"Foi alterado a OPCAO: {op_hist}")
            continue    
                        


        # Escolha dos valores
        try:
            valor1 = int(input("| Digite o primeiro valor: "))
            valor2 = int(input("| Digite o segundo valor: "))

            if ope == 5 and valor2 > 100:
                print(Fore.RED +"Expoente muito grande."+ Style.RESET_ALL)
                continue

        except ValueError:
            print("\n\033[31mOpção inválida\033[0m")
            continue
        
        except KeyboardInterrupt:
            print(Fore.RED + "\nPrograma encerrado."+ Style.RESET_ALL)
            sleep(1)
            break  
        print("="*30)

        op = TipoOperacao(ope)

        if op == 4 and valor2 == 0:
            print(Fore.RED +"Não é possível dividir por zero."+ Style.RESET_ALL)
            continue

        # Calculos
        res = resultado(ope, valor1, valor2)
        
        
        # Adicionar Histórico Txt, Logger e JSON
        with open("resultados/calculo.txt", "a") as arquivo:
            arquivo.write(f"| {valor1} {op.tipos(ope)} {valor2} = {res} | {hor_format}\n")

        logger.info("Nova OPERACAO realizada")
        logger.info(f"{valor1} + {valor2} = {res}")

        Historico.salvar_operacao({
            "valor1": valor1,
            "valor2": valor2,
            "operacao": op.tipos(ope),
            "resultado": res,
            "data": hor_format
        })


        # Resposta
        print("+" + "-" * 28 + "+")
        print("|" + "RESPOSTA".center(28) + "|")
        print("|" + f"\033[32m{res}\033[0m".center(37) + "|")
        print("+" + "-" * 28 + "+\n")

        sleep(1.6)


        # Opção Sair do programa
        print("+" + "-" * 28 + "+")
        print("| Deseja sair?".ljust(29) + "|")
        print("| [ 1 ] Sim".ljust(29) + "|")
        print("| [ 2 ] Não".ljust(29) + "|")
        print("+" + "-" * 28 + "+\n")
        try:
            sair = int(input("Escolha uma opção: "))

        except ValueError:
            print("\n\033[31mOpção inválida\033[0m")
            break

        except KeyboardInterrupt:
            print(Fore.RED +"\nPrograma encerrado."+ Style.RESET_ALL)
            sleep(1)
            break  
        
        if sair not in [1, 2]:
            print("\n\033[31mOpção inválida\033[0m")
            break 

        if sair == 1:
            print(Fore.RED +"\nPrograma encerrado."+ Style.RESET_ALL)
            sleep(1)
            Historico.limpar()
            break
        else:
            continue