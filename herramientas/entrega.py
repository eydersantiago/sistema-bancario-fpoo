#!/usr/bin/env python3
"""Arma el .zip de la entrega del Sistema bancario (FPOO).

Uso: make entrega   (o en VS Code: Terminal -> Run Task -> «Preparar entrega (.zip)»)

Mete en el zip todo el proyecto menos lo compilado (build/, el ejecutable) y la carpeta .git.
El nombre lleva el usuario, para que el profesor sepa de quien es cada entrega.
"""
import getpass
import os
import re
import sys
import zipfile
from datetime import datetime

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXCLUIR_CARPETAS = {".git", "build", "__pycache__", ".vscode-server"}
EXCLUIR_ARCHIVOS = {"banco", "banco.exe"}
EXCLUIR_EXTENSIONES = (".o", ".d", ".zip", ".exe")


def usuario():
    try:
        nombre = getpass.getuser()
    except Exception:
        nombre = "estudiante"
    # En el editor del curso el usuario es ws-<cuenta de GitHub>.
    nombre = re.sub(r"^ws-", "", nombre)
    return re.sub(r"[^A-Za-z0-9._-]+", "-", nombre) or "estudiante"


def main():
    destino = os.path.join(RAIZ, f"entrega-{usuario()}-sistema-bancario.zip")
    total = 0
    with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED) as zf:
        for carpeta, subcarpetas, archivos in os.walk(RAIZ):
            subcarpetas[:] = sorted(d for d in subcarpetas if d not in EXCLUIR_CARPETAS)
            for nombre in sorted(archivos):
                ruta = os.path.join(carpeta, nombre)
                relativa = os.path.relpath(ruta, RAIZ)
                if nombre in EXCLUIR_ARCHIVOS or nombre.endswith(EXCLUIR_EXTENSIONES):
                    continue
                zf.write(ruta, os.path.join("sistema-bancario", relativa))
                total += 1
    print()
    print(f"Listo: {os.path.basename(destino)} ({total} archivos, {datetime.now():%Y-%m-%d %H:%M}).")
    print("Para descargarlo: en el Explorador de VS Code, clic derecho sobre ese archivo -> Download.")
    print("Despues subelo al Campus donde indique el profesor.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
