from time import sleep
from src.api import Operacoes, resultado
from src.interface import exibir_corpo
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--add", nargs=2, type=int)

args = parser.parse_args()

if args.add:
    a, b = args.add
    print(resultado(1, a, b))

exibir_corpo()


print("\n"*2)
print("=" * 30)