from pathlib import Path
import openpyxl

path = Path()
for i in path.glob('*'):
    print(i)

print(openpyxl.__version__)
