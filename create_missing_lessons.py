# -*- coding: utf-8 -*-
"""Script para criar as aulas faltantes com slides"""

import os

def create_lesson(filepath, title, video_id, slides_base_url, slide_count, prev_link, next_link, lang='pt'):
    """Cria uma página de aula com vídeo e slides"""
    
    # Labels por idioma
    labels = {
        'pt': {
            'video_title': 'Vídeo da Aula',
            'script_title': 'Roteiro Completo',
            'script_notice': '**Roteiro em elaboração** - O texto completo desta aula será adicionado em breve. Por enquanto, assista ao vídeo acima e acompanhe os slides abaixo.',
            'slides_title': 'Slides da Aula',
            'material_title': 'Material Complementar',
            'ebook': 'E-book da Aula',
            'slides': 'Slides da Aula',
            'prev': 'Anterior',
            'next': 'Próxima'
        },
        'en': {
            'video_title': 'Class Video',
            'script_title': 'Complete Script',
            'script_notice': '**Script in progress** - The complete text for this class will be added soon. In the meantime, watch the video above and follow the slides below.',
            'slides_title': 'Class Slides',
            'material_title': 'Supplementary Material',
            'ebook': 'E-book',
            'slides': 'Slides',
            'prev': 'Previous',
            'next': 'Next'
        },
        'es': {
            'video_title': 'Video de la Clase',
            'script_title': 'Guión Completo',
            'script_notice': '**Guión en elaboración** - El texto completo de esta clase se añadirá pronto. Por ahora, mira el video de arriba y sigue las diapositivas a continuación.',
            'slides_title': 'Diapositivas de la Clase',
            'material_title': 'Material Complementario',
            'ebook': 'E-book',
            'slides': 'Diapositivas',
            'prev': 'Anterior',
            'next': 'Siguiente'
        }
    }
    
    L = labels[lang]
    
    # Gerar slides
    slides_md = '\n\n'.join([f'![Slide {i}]({slides_base_url}{i:02d}.jpg)' for i in range(1, slide_count + 1)])
    
    # Gerar conteúdo
    content = f'''# {title}

## :movie_camera: {L['video_title']}

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/{video_id}?badge=0&autopause=0&player_id=0&app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media" style="position:absolute;top:0;left:0;width:100%;height:100%;border-radius:12px;" title="{title}"></iframe></div>

---

## :page_facing_up: {L['script_title']}

> :construction: {L['script_notice']}

---

## :framed_picture: {L['slides_title']}

{slides_md}

---

## :books: {L['material_title']}

- [{L['ebook']}](https://github.com/areabitcoin/Bitcoin-4-All)
- [{L['slides']}](https://github.com/areabitcoin/Bitcoin-4-All)

---

[:arrow_left: {L['prev']}]({prev_link}) | [{L['next']} :arrow_right:]({next_link})
'''
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'✓ Created: {filepath}')


# EN Class 4
create_lesson(
    'docs/en/class-4.md',
    ':four: Class 4 - Inside Bitcoin: Decentralization, Blockchain and Game Theory',
    '1083559829',
    'https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/main/Bitcoin%204%20All%20-%20English/Slides/Class%204/slide-',
    20,
    'en/class-3.md',
    'en/class-5.md',
    'en'
)

# EN Class 5
create_lesson(
    'docs/en/class-5.md',
    ':five: Class 5 - Inside Bitcoin: Mining, Halving and the Cycles',
    '1083560908',
    'https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/main/Bitcoin%204%20All%20-%20English/Slides/Class%205/slide-',
    30,
    'en/class-4.md',
    'en/class-6.md',
    'en'
)

# ES Clase 4
create_lesson(
    'docs/es/clase-4.md',
    ':four: Clase 4 - Dentro de Bitcoin: Descentralización, Blockchain y Teoría de Juegos',
    '1085122029',
    'https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/main/Bitcoin%204%20All%20-%20Spanish/Slides/AULA%204/slide-',
    20,
    'es/clase-3.md',
    'es/clase-5.md',
    'es'
)

# ES Clase 5
create_lesson(
    'docs/es/clase-5.md',
    ':five: Clase 5 - Dentro de Bitcoin: Minería, Halving y los Ciclos',
    '1085123457',
    'https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/main/Bitcoin%204%20All%20-%20Spanish/Slides/AULA%205/slide-',
    30,
    'es/clase-4.md',
    'es/clase-6.md',
    'es'
)

# ES Clase 10
create_lesson(
    'docs/es/clase-10.md',
    ':keycap_ten: Clase 10 - Cómo retirar del exchange y tener soberanía con tu Bitcoin',
    '1085129648',
    'https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/main/Bitcoin%204%20All%20-%20Spanish/Slides/AULA%2010/Sem%20ti%CC%81tulo-24-',
    5,
    'es/clase-9.md',
    'es/intro.md',
    'es'
)

print('\nAll missing lessons created!')
