import os
import shutil
from datetime import datetime
import sys

def main():
    """
    Cria um backup automático dos arquivos da pasta 'data'
    e salva em uma pasta 'backup' com timestamp.
    """
    origem = "data"
    destino = f"backup/{datetime.now():%Y%m%d_%H%M%S}"

    if not os.path.exists(origem):
        print(f"Pasta '{origem}' não encontrada. Nenhum backup foi feito.")
        return 1

    os.makedirs(destino, exist_ok=True)

    for arquivo in os.listdir(origem):
        caminho_origem = os.path.join(origem, arquivo)
        caminho_destino = os.path.join(destino, arquivo)
        if os.path.isfile(caminho_origem):
            shutil.copy2(caminho_origem, caminho_destino)
            print(f"Copiado: {arquivo}")

    print(f"Backup concluído em '{destino}'.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
