import os
import re

# YouTube IDs para cada aula PT
youtube_ids = {
    'intro': 'pTgQ6Z_ozf0',
    'aula-1': '6Ly0L8_9Pu8',
    'aula-2': '55vAZdwc3Bs',
    'aula-3': 'mAaE4PPSMls',
    'aula-4': 'j23TW7gnX2Y',
    'aula-5': 'oHKTpPsJBDY',
    'aula-6': 'RIMKaC3xiQU',
    'aula-7': 'VC1oAtXppcY',
    'aula-8': 'TSGHnKX1bTs',
    'aula-9': 'cUTJOPAI0Wg',
    'aula-10': 'cUTJOPAI0Wg'
}

for filename, video_id in youtube_ids.items():
    filepath = f'docs/pt/{filename}.md'
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        youtube_url = f'https://www.youtube.com/watch?v={video_id}'
        thumbnail_url = f'https://img.youtube.com/vi/{video_id}/maxresdefault.jpg'
        embed_url = f'https://www.youtube.com/embed/{video_id}?rel=0'
        
        # Formato que funciona em ambas plataformas:
        # - Thumbnail clicável (funciona no GitBook)
        # - iframe (funciona no Docsify/GitHub Pages)
        new_video_section = f'''## :movie_camera: Video da Aula

[![Assistir Video]({thumbnail_url})]({youtube_url})

:point_right: **[Clique aqui para assistir no YouTube]({youtube_url})**

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="{embed_url}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="position:absolute;top:0;left:0;width:100%;height:100%;border-radius:12px;" title="Video"></iframe></div>

---'''
        
        # Substituir seção de vídeo existente
        pattern = r'##\s*:?(?:movie_camera:)?\s*V[ií]deo da Aula.*?(?=\n##[^#]|\n---\n|\Z)'
        if re.search(pattern, content, re.DOTALL | re.IGNORECASE):
            content = re.sub(pattern, new_video_section, content, count=1, flags=re.DOTALL | re.IGNORECASE)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'OK: {filename}')
        else:
            print(f'PADRAO NAO ENCONTRADO: {filename}')
    else:
        print(f'ARQUIVO NAO ENCONTRADO: {filename}')

print('Concluido!')
