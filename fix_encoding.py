# -*- coding: utf-8 -*-
"""
Script para corrigir encoding de arquivos corrompidos
Os arquivos originais têm caracteres UTF-8 que foram interpretados incorretamente
"""
import os
import glob

# Mapeamento de sequências corrompidas para caracteres corretos
# Encoding problem: UTF-8 bytes interpreted as Windows-1252
REPLACEMENTS = {
    # Portuguese accented vowels - lowercase
    '├í': 'á',  # C3 A1
    '├á': 'à',  # C3 A0 - NOVO
    '├ú': 'ã',  # C3 A3
    '├ó': 'â',  # C3 A2
    '├®': 'é',  # C3 A9
    '├¿': 'è',  # C3 A8 - NOVO
    '├¬': 'ê',  # C3 AA
    '├¡': 'í',  # C3 AD
    '├¼': 'ì',  # C3 AC - NOVO
    '├│': 'ó',  # C3 B3
    '├▓': 'ò',  # C3 B2 - NOVO
    '├┤': 'ô',  # C3 B4
    '├Á': 'õ',  # C3 B5
    '├║': 'ú',  # C3 BA
    '├╣': 'ù',  # C3 B9 - NOVO
    '├╝': 'ü',  # C3 BC - NOVO
    '├º': 'ç',  # C3 A7
    # Portuguese accented vowels - uppercase
    '├Ç': 'À',  # C3 80
    '├ü': 'Á',  # C3 81
    '├é': 'Â',  # C3 82 - NOVO
    '├â': 'Ã',  # C3 83 - NOVO
    '├ê': 'Ê',  # C3 8A - NOVO  
    '├ë': 'É',  # C3 89
    '├ì': 'Í',  # C3 8D
    '├ô': 'Ô',  # C3 94
    '├ò': 'Ó',  # C3 93 - NOVO
    '├ò': 'Ó',  # C3 93
    '├ò': 'Õ',  # C3 95 - NOVO
    '├Ü': 'Ú',  # C3 9A
    '├ç': 'Ç',  # C3 87 - NOVO
    # Spanish specific
    '├Ñ': 'Ñ',  # C3 91
    '├▒': 'ñ',  # C3 B1
    # Spaces and special
    '┬á': ' ',  # C2 A0 (non-breaking space)
    '┬░': '°',  # C2 B0
    '┬®': '®',  # C2 AE
    '┬©': '©',  # C2 A9
    '┬╗': '»',  # C2 BB
    '┬½': '½',  # C2 BD
    '┬í': '¡',  # C2 A1 - Spanish inverted exclamation
    '┬┐': '¿',  # C2 BF - Spanish inverted question mark
    '┐Q': 'Qué',  # contextual fix
    '┐q': 'qué',  # contextual fix
    '┐c': 'có',  # contextual fix
    # Aspas e apóstrofos (smart quotes)
    'ΓÇ£': '"',  # E2 80 9C
    'ΓÇ¥': '"',  # E2 80 9D
    'ΓÇ£': '"',
    'ΓÇÿ': ''',  # E2 80 98
    'ΓÇÖ': ''',  # E2 80 99
    'ΓÇô': '–',  # E2 80 93 (en dash)
    'ΓÇö': '—',  # E2 80 94 (em dash)
    'ΓÇª': '…',  # E2 80 A6 (ellipsis)
    'ΓÇó': '•',  # E2 80 A2 (bullet)
}

def fix_file(filepath):
    """Corrige o encoding de um arquivo"""
    try:
        # Tentar ler como UTF-8 primeiro
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        # Se falhar, tentar cp1252
        with open(filepath, 'r', encoding='cp1252') as f:
            content = f.read()
    
    original = content
    
    # Aplicar todas as substituições
    for bad, good in REPLACEMENTS.items():
        content = content.replace(bad, good)
    
    if content != original:
        # Salvar com encoding UTF-8
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    docs_dir = os.path.join(base_dir, 'docs')
    
    # Processar arquivos PT e ES
    patterns = [
        os.path.join(docs_dir, 'pt', '*.md'),
        os.path.join(docs_dir, 'es', '*.md'),
    ]
    
    fixed_count = 0
    for pattern in patterns:
        files = glob.glob(pattern)
        for filepath in files:
            filename = os.path.basename(filepath)
            if fix_file(filepath):
                print(f'✓ Corrigido: {filepath}')
                fixed_count += 1
            else:
                print(f'  Sem alteração: {filepath}')
    
    print(f'\nTotal de arquivos corrigidos: {fixed_count}')

if __name__ == '__main__':
    main()
