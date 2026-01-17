import os
import re

# Vimeo IDs para ES com thumbnails
vimeo_es = {
    'intro': '1085119221',
    'clase-1': '1085118505',
    'clase-2': '1085117525',
    'clase-3': '1085115043',
    'clase-4': '1085116885',
    'clase-5': '1085116133',
    'clase-6': '1085129268',
    'clase-7': '1085128394',
    'clase-8': '1085127642',
    'clase-9': '1085128853',
    'clase-10': '1085129648'
}

for filename, video_id in vimeo_es.items():
    filepath = f'docs/es/{filename}.md'
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        vimeo_url = f'https://vimeo.com/{video_id}'
        embed_url = f'https://player.vimeo.com/video/{video_id}?badge=0&autopause=0&player_id=0&app_id=58479'
        # Vimeo thumbnail
        thumbnail_url = f'https://vumbnail.com/{video_id}.jpg'
        
        new_video_section = f'''## :movie_camera: Video de la Clase

[![Ver Video]({thumbnail_url})]({vimeo_url})

:point_right: **[Haz clic aqui para ver en Vimeo]({vimeo_url})**

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="{embed_url}" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media" style="position:absolute;top:0;left:0;width:100%;height:100%;border-radius:12px;" title="Video"></iframe></div>

---'''
        
        # Substituir seção de vídeo existente
        pattern = r'##\s*:?(?:movie_camera:)?\s*(?:Video|Presentacion)\s*(?:de\s*la\s*)?(?:Clase|Curso)?.*?(?=\n##[^#]|\n---\n|\Z)'
        if re.search(pattern, content, re.DOTALL | re.IGNORECASE):
            content = re.sub(pattern, new_video_section, content, count=1, flags=re.DOTALL | re.IGNORECASE)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'ES: {filename} -> Vimeo {video_id} com thumbnail')
    else:
        print(f'Arquivo nao encontrado: {filepath}')

print('\nConcluido!')
