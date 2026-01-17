import os
import re

docs_path = "docs"

def fix_links_in_file(filepath, lang_prefix):
    """Remove prefixo de língua dos links relativos"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Padrão: (pt/arquivo.md) -> (arquivo.md)
    # Ou (en/arquivo.md) -> (arquivo.md)
    # Ou (es/arquivo.md) -> (arquivo.md)
    pattern = rf'\({lang_prefix}/([^)]+\.md)\)'
    content = re.sub(pattern, r'(\1)', content)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

# Processar cada língua
languages = {
    'pt': ['intro.md', 'aula-1.md', 'aula-2.md', 'aula-3.md', 'aula-4.md', 
           'aula-5.md', 'aula-6.md', 'aula-7.md', 'aula-8.md', 'aula-9.md', 'aula-10.md'],
    'en': ['intro.md', 'class-1.md', 'class-2.md', 'class-3.md', 'class-4.md',
           'class-5.md', 'class-6.md', 'class-7.md', 'class-8.md', 'class-9.md', 'class-10.md'],
    'es': ['intro.md', 'clase-1.md', 'clase-2.md', 'clase-3.md', 'clase-4.md',
           'clase-5.md', 'clase-6.md', 'clase-7.md', 'clase-8.md', 'clase-9.md', 'clase-10.md']
}

print("=== Corrigindo todos os links ===\n")

for lang, files in languages.items():
    print(f"--- {lang.upper()} ---")
    for filename in files:
        filepath = os.path.join(docs_path, lang, filename)
        if os.path.exists(filepath):
            if fix_links_in_file(filepath, lang):
                print(f"  ✓ {filename} - links corrigidos")
            else:
                print(f"  - {filename} - sem alterações")
        else:
            print(f"  ✗ {filename} - arquivo não encontrado")
    print()

print("=== Verificando links após correção ===\n")

# Verificar se ainda há links com prefixo incorreto
for lang, files in languages.items():
    print(f"--- {lang.upper()} ---")
    for filename in files:
        filepath = os.path.join(docs_path, lang, filename)
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Procurar links com prefixo de língua
            bad_links = re.findall(rf'\({lang}/[^)]+\.md\)', content)
            if bad_links:
                print(f"  ✗ {filename}: ainda tem links incorretos: {bad_links}")
            else:
                # Verificar se os links apontam para arquivos existentes
                links = re.findall(r'\(([^)]+\.md)\)', content)
                all_ok = True
                for link in links:
                    # Ignorar links externos
                    if link.startswith('http'):
                        continue
                    target = os.path.join(docs_path, lang, link)
                    if not os.path.exists(target):
                        print(f"  ⚠ {filename}: link quebrado -> {link}")
                        all_ok = False
                if all_ok and links:
                    print(f"  ✓ {filename}: todos os links OK")
    print()

print("Concluído!")
