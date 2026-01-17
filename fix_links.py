import os
import re

# Corrigir links nas intros - remover prefixo de pasta duplicado
fixes = {
    'docs/pt/intro.md': [
        ('(pt/aula-1.md)', '(aula-1.md)'),
        ('(pt/aula-2.md)', '(aula-2.md)'),
    ],
    'docs/en/intro.md': [
        ('(en/class-1.md)', '(class-1.md)'),
        ('(en/class-2.md)', '(class-2.md)'),
    ],
    'docs/es/intro.md': [
        ('(es/clase-1.md)', '(clase-1.md)'),
        ('(es/clase-2.md)', '(clase-2.md)'),
    ],
}

for filepath, replacements in fixes.items():
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        for old, new in replacements:
            if old in content:
                content = content.replace(old, new)
                print(f'{filepath}: {old} -> {new}')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

# Verificar links em todas as aulas PT
print('\n--- Verificando links em PT ---')
pt_files = ['intro', 'aula-1', 'aula-2', 'aula-3', 'aula-4', 'aula-5', 'aula-6', 'aula-7', 'aula-8', 'aula-9', 'aula-10']
for i, filename in enumerate(pt_files):
    filepath = f'docs/pt/{filename}.md'
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Verificar links de navegação
        links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
        for text, url in links:
            if url.startswith('pt/') and not url.startswith('http'):
                print(f'  ERRO {filename}: link incorreto -> {url}')
                # Corrigir
                content = content.replace(f']({url})', f']({url.replace("pt/", "")})')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
    else:
        print(f'  NAO ENCONTRADO: {filepath}')

# Verificar links em todas as aulas EN
print('\n--- Verificando links em EN ---')
en_files = ['intro', 'class-1', 'class-2', 'class-3', 'class-4', 'class-5', 'class-6', 'class-7', 'class-8', 'class-9', 'class-10']
for filename in en_files:
    filepath = f'docs/en/{filename}.md'
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
        for text, url in links:
            if url.startswith('en/') and not url.startswith('http'):
                print(f'  ERRO {filename}: link incorreto -> {url}')
                content = content.replace(f']({url})', f']({url.replace("en/", "")})')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
    else:
        print(f'  NAO ENCONTRADO: {filepath}')

# Verificar links em todas as aulas ES
print('\n--- Verificando links em ES ---')
es_files = ['intro', 'clase-1', 'clase-2', 'clase-3', 'clase-4', 'clase-5', 'clase-6', 'clase-7', 'clase-8', 'clase-9', 'clase-10']
for filename in es_files:
    filepath = f'docs/es/{filename}.md'
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
        for text, url in links:
            if url.startswith('es/') and not url.startswith('http'):
                print(f'  ERRO {filename}: link incorreto -> {url}')
                content = content.replace(f']({url})', f']({url.replace("es/", "")})')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
    else:
        print(f'  NAO ENCONTRADO: {filepath}')

print('\nLinks corrigidos!')
