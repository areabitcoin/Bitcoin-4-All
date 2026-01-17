import re
import os
import glob

def fix_slides(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Adiciona linha em branco após cada imagem de slide se não houver
    # Padrão: ![Slide X](...) seguido diretamente por texto (sem linha em branco)
    pattern = r'(!\[Slide \d+\]\([^\)]+\))\n([^\n])'
    replacement = r'\1\n\n\2'
    
    new_content = re.sub(pattern, replacement, content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

# Processar todos os arquivos
langs = ['pt', 'en', 'es']
total_fixed = 0

for lang in langs:
    folder = f'docs/{lang}'
    for filepath in glob.glob(f'{folder}/*.md'):
        if fix_slides(filepath):
            print(f' Corrigido: {filepath}')
            total_fixed += 1
        else:
            print(f'- Já OK: {filepath}')

print(f'\nTotal corrigidos: {total_fixed}')
