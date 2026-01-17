import os
import re

# Configuração
base_url = "https://areabitcoin.github.io/Bitcoin-4-All/"

# Textos por idioma
share_texts = {
    'pt': {
        'title': '### :loudspeaker: Compartilhe esta aula!',
        'twitter': 'Twitter',
        'linkedin': 'LinkedIn', 
        'whatsapp': 'WhatsApp',
        'telegram': 'Telegram',
        'progress_title': '### :chart_with_upwards_trend: Seu Progresso no Curso',
        'lesson_word': 'Aula'
    },
    'en': {
        'title': '### :loudspeaker: Share this lesson!',
        'twitter': 'Twitter',
        'linkedin': 'LinkedIn',
        'whatsapp': 'WhatsApp', 
        'telegram': 'Telegram',
        'progress_title': '### :chart_with_upwards_trend: Your Course Progress',
        'lesson_word': 'Class'
    },
    'es': {
        'title': '### :loudspeaker: Comparte esta clase!',
        'twitter': 'Twitter',
        'linkedin': 'LinkedIn',
        'whatsapp': 'WhatsApp',
        'telegram': 'Telegram',
        'progress_title': '### :chart_with_upwards_trend: Tu Progreso en el Curso',
        'lesson_word': 'Clase'
    }
}

# Arquivos por idioma
files = {
    'pt': [f'aula-{i}.md' for i in range(1, 11)],
    'en': [f'class-{i}.md' for i in range(1, 11)],
    'es': [f'clase-{i}.md' for i in range(1, 11)]
}

def get_lesson_number(filename, lang):
    match = re.search(r'(\d+)', filename)
    return int(match.group(1)) if match else 0

def create_share_buttons(lang, filename, page_title):
    texts = share_texts[lang]
    lesson_num = get_lesson_number(filename, lang)
    
    # URL encode do título
    page_url = f"{base_url}{lang}/{filename.replace('.md', '')}"
    
    tweet_text = f"Estou aprendendo sobre Bitcoin! {texts['lesson_word']} {lesson_num} do curso Bitcoin 4 All " if lang == 'pt' else \
                 f"I'm learning about Bitcoin! {texts['lesson_word']} {lesson_num} from Bitcoin 4 All course " if lang == 'en' else \
                 f"Estoy aprendiendo sobre Bitcoin! {texts['lesson_word']} {lesson_num} del curso Bitcoin 4 All "
    
    share_section = f"""
---

{texts['title']}

<div class="share-buttons">
<a href="https://twitter.com/intent/tweet?text={tweet_text.replace(' ', '%20')}&url={page_url}&via=aaborges_" target="_blank" class="share-btn share-btn-twitter">
 {texts['twitter']}
</a>
<a href="https://www.linkedin.com/sharing/share-offsite/?url={page_url}" target="_blank" class="share-btn share-btn-linkedin">
 {texts['linkedin']}
</a>
<a href="https://wa.me/?text={tweet_text.replace(' ', '%20')}%20{page_url}" target="_blank" class="share-btn share-btn-whatsapp">
 {texts['whatsapp']}
</a>
<a href="https://t.me/share/url?url={page_url}&text={tweet_text.replace(' ', '%20')}" target="_blank" class="share-btn share-btn-telegram">
 {texts['telegram']}
</a>
</div>

{texts['progress_title']}

<div class="course-progress">
<strong>{texts['lesson_word']} {lesson_num} de 10</strong> ({lesson_num * 10}% completo)
<div class="course-progress-bar">
<div class="course-progress-fill" style="width: {lesson_num * 10}%"></div>
</div>
</div>
"""
    return share_section

def process_file(lang, filename):
    filepath = os.path.join('docs', lang, filename)
    
    if not os.path.exists(filepath):
        print(f"   {filename} não encontrado")
        return
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Verifica se já tem botões de compartilhamento
    if ':loudspeaker:' in content or 'share-buttons' in content:
        print(f"  - {filename} já tem botões de compartilhamento")
        return
    
    # Adiciona antes da navegação final (se existir)
    nav_patterns = [
        r'\n\*\*\*\n\n\[Anterior\]',
        r'\n---\n\n\[Anterior\]',
        r'\n\[Anterior\]',
        r'\n\*\*\*\n\n\[Previous\]',
        r'\n---\n\n\[Previous\]',
        r'\n\[Previous\]',
        r'\n:arrow_left:'
    ]
    
    share_section = create_share_buttons(lang, filename, "")
    
    inserted = False
    for pattern in nav_patterns:
        if re.search(pattern, content):
            content = re.sub(pattern, share_section + '\n' + pattern.replace(r'\n', '\n').replace('\\', ''), content, count=1)
            inserted = True
            break
    
    if not inserted:
        # Adiciona no final
        content += share_section
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"   {filename} atualizado")

# Processar todos os arquivos
for lang, filenames in files.items():
    print(f"\n--- {lang.upper()} ---")
    for filename in filenames:
        process_file(lang, filename)

print("\n Concluído!")
