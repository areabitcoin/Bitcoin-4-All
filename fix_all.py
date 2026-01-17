import os
import re

# 1. CORRIGIR README - emojis menores inline
readme_content = '''# Bitcoin 4 All

**Free and open source Bitcoin course for everyone!**

*Curso gratuito e de código aberto sobre Bitcoin para todos!*

---

## :world_map: Choose Your Language / Escolha seu Idioma

| :brazil: Português | :us: English | :es: Español |
|:------------------:|:------------:|:------------:|
| [Começar](pt/intro.md) | [Start](en/intro.md) | [Comenzar](es/intro.md) |

---

## :books: About the Course

**Bitcoin 4 All** is a complete course designed to teach anyone about Bitcoin, from zero to self-custody.

### What you will learn:

| Topic |
|:------|
| :question: What is Bitcoin and why was it created |
| :moneybag: Problems with fiat money |
| :chart_with_upwards_trend: Why Bitcoin is better money |
| :gear: How Bitcoin works (decentralization, blockchain, mining) |
| :rocket: Why Bitcoin should continue to appreciate |
| :shopping_cart: How to get bitcoin |
| :shield: Debunking FUDs about Bitcoin |
| :key: How to store Bitcoin safely |
| :crown: Financial sovereignty through self-custody |

---

## :link: Links

| | |
|:---|:---|
| :globe_with_meridians: **Website** | [areabitcoin.co](https://areabitcoin.co) |
| :bird: **Twitter/X** | [@areabitcoin](https://x.com/areabitcoin) |
| :tv: **YouTube** | [Area Bitcoin](https://youtube.com/@AreaBitcoin) |
| :camera: **Instagram** | [@area.bitcoin](https://instagram.com/area.bitcoin) |
| :octopus: **GitHub** | [areabitcoin/Bitcoin-4-All](https://github.com/areabitcoin/Bitcoin-4-All) |

---

## :balance_scale: License

This content is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

You are free to share and adapt this material, as long as you give appropriate credit and distribute under the same license.

---

Made with :orange_heart: by [Area Bitcoin](https://areabitcoin.co)
'''

with open('docs/README.md', 'w', encoding='utf-8') as f:
    f.write(readme_content)
print('README.md corrigido!')

# 2. PADRONIZAR INTRO EN
intro_en = '''# :books: Bitcoin 4 All

Welcome to **Bitcoin 4 All**! A complete, free and open source journey to understand Bitcoin from scratch.

## :movie_camera: Course Presentation

[![Watch Video](https://img.youtube.com/vi/XoySXkR1nJw/maxresdefault.jpg)](https://www.youtube.com/watch?v=XoySXkR1nJw)

:point_right: **[Click here to watch on YouTube](https://www.youtube.com/watch?v=XoySXkR1nJw)**

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://www.youtube.com/embed/XoySXkR1nJw?rel=0" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="position:absolute;top:0;left:0;width:100%;height:100%;border-radius:12px;" title="Intro"></iframe></div>

---

## :scroll: Full Script

Hello! Welcome to Bitcoin4All, a free and open source course created by Area Bitcoin.

If you're here, it's because you've heard about Bitcoin and want to learn more about how it works. And guess what? You're in the right place!

Our goal is to help you understand Bitcoin and inspire you to be a multiplier of this knowledge. We want anyone, regardless of their level of knowledge or background, to be able to learn about this revolutionary money and technology in a simple, direct and practical way.

You'll realize that Bitcoin is much more than numbers on a screen: it's about freedom, sovereignty and the chance to participate in a fairer, decentralized and resilient financial system. And the best part? All course materials are available for you and any educator in the world to use as you wish, because we believe that sharing knowledge is as important as learning.

### How does Bitcoin4All work?

Since Bitcoin4All is open source, it goes beyond a simple course. It's a tool you can use to teach others, organize meetups, create your own videos or even customize the materials to your reality. Under the Creative Commons BY-SA 4.0 license, you have the freedom to adapt everything - as long as credits are given to Bitcoin4All by Area Bitcoin and with the condition that it's used for educational purposes, never commercial, okay?

We believe that knowledge about Bitcoin needs to be universal and accessible to everyone, because it's a powerful tool to change lives. So it doesn't matter if you're just starting out or already understand a bit about the subject, Bitcoin4All is made for you to feel part of this revolution.

---

## :bookmark_tabs: Course Curriculum

We prepared a course with **10 classes**, each about 10 minutes long, to guide you through the main concepts and answer the most common questions about Bitcoin.

| Class | Topic |
|-------|-------|
| 1 | What is Bitcoin and why was it created? |
| 2 | What's the problem with today's money? |
| 3 | Why is Bitcoin better money? |
| 4 | Inside Bitcoin: how does it work? |
| 5 | Why should Bitcoin continue to appreciate? |
| 6 | Ways to get Bitcoin: Exchange, P2P or circular economies |
| 7 | Debunking lies (FUDs) about Bitcoin |
| 8 | Why self-custody and not leave everything on an exchange or bank? |
| 9 | What are Bitcoin wallets and how to use them? |
| 10 | How to withdraw from Exchange and achieve financial sovereignty with Bitcoin? |

---

## :sparkles: What can you do?

:mortar_board: **Learn**: watch the course at your own pace and discover how Bitcoin works, why it's important and how to protect your satoshis well.

:mega: **Share**: show this material to friends, family or that curious colleague who always asks you "what is Bitcoin anyway?".

:teacher: **Teach**: use the content to spread Bitcoin. Who knows, maybe you'll organize a meetup or help train a new generation of bitcoiners?

---

All files - videos, slides and other materials - are available on [areabitcoin.co](https://areabitcoin.co) and on [Area Bitcoin's GitHub](https://github.com/areabitcoin/Bitcoin-4-All). You can access everything easily and for free, whether to learn, share or teach.

We're here to help you understand, adopt and spread this transformative idea.

**Ready to start? Let's go!**

---

## :rocket: Start Now

[Start Class 1 :arrow_right:](en/class-1.md)

---

## :link: Links

- :globe_with_meridians: [Area Bitcoin](https://areabitcoin.co)
- :bird: [Twitter/X](https://x.com/areabitcoin)
- :tv: [YouTube](https://youtube.com/@AreaBitcoin)
- :camera: [Instagram](https://instagram.com/area.bitcoin)

:cc: Content under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license
'''

with open('docs/en/intro.md', 'w', encoding='utf-8') as f:
    f.write(intro_en)
print('EN intro.md padronizado!')

# 3. PADRONIZAR INTRO ES
intro_es = '''# :books: Bitcoin 4 All

¡Bienvenido a **Bitcoin 4 All**! Un viaje completo, gratuito y de código abierto para entender Bitcoin desde cero.

## :movie_camera: Presentación del Curso

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/1085119221?badge=0&autopause=0&player_id=0&app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media" style="position:absolute;top:0;left:0;width:100%;height:100%;border-radius:12px;" title="Intro"></iframe></div>

---

## :scroll: Guión Completo

¡Hola! Bienvenido a Bitcoin4All, un curso gratuito y open source creado por Area Bitcoin.

Si estás aquí, es porque ya has oído hablar de Bitcoin y quieres saber más sobre cómo funciona. ¿Y adivina qué? ¡Estás en el lugar correcto!

El objetivo es ayudarte a entender Bitcoin e inspirarte a ser un multiplicador de este conocimiento. Queremos que cualquier persona, independientemente de su nivel de conocimiento o formación, pueda aprender sobre este dinero y tecnología revolucionaria de una manera simple, directa y práctica.

Te darás cuenta de que Bitcoin es mucho más que números en una pantalla: se trata de libertad, soberanía y la oportunidad de participar en un sistema financiero más justo, descentralizado y resistente. ¿Y la mejor parte? Todo el material del curso está disponible para ti y para cualquier educador en el mundo para usar como quieras, porque creemos que compartir conocimiento es tan importante como aprender.

### ¿Cómo funciona Bitcoin4All?

Como Bitcoin4All es open source, va más allá de un simple curso. Es una herramienta que puedes usar para enseñar a otros, organizar encuentros como meetups, crear tus propios videos o incluso personalizar los materiales para tu realidad. Bajo la licencia Creative Commons BY-SA 4.0, tienes libertad para adaptar todo - siempre que se den los créditos a Bitcoin4All de Area Bitcoin y con la condición de que sea usado para fines educativos, nunca comerciales, ¿vale?

Creemos que el conocimiento sobre Bitcoin necesita ser universal y accesible para todos, porque es una herramienta poderosa para cambiar vidas. Así que no importa si estás empezando ahora o ya entiendes un poco sobre el tema, Bitcoin4All está hecho para que te sientas parte de esta revolución.

---

## :bookmark_tabs: Contenido Programático

Preparamos un curso con **10 clases**, cada una con cerca de 10 minutos, para guiarte por los principales conceptos y responder a las dudas más comunes sobre Bitcoin.

| Clase | Tema |
|-------|------|
| 1 | ¿Qué es Bitcoin y por qué fue creado? |
| 2 | ¿Cuál es el problema del dinero actual? |
| 3 | ¿Por qué Bitcoin es un dinero mejor? |
| 4 | Dentro de Bitcoin: ¿cómo funciona? |
| 5 | ¿Por qué Bitcoin debe continuar valorizándose? |
| 6 | Formas de tener Bitcoin: Exchange, P2P o economías circulares |
| 7 | Refutando mentiras (FUDs) sobre Bitcoin |
| 8 | ¿Por qué hacer auto-custodia y no dejar todo en el exchange o banco? |
| 9 | ¿Qué son y cómo usar billeteras de Bitcoin? |
| 10 | ¿Cómo retirar del Exchange y conquistar soberanía financiera con Bitcoin? |

---

## :sparkles: ¿Qué puedes hacer?

:mortar_board: **Aprende**: mira el curso a tu ritmo y descubre cómo funciona Bitcoin, por qué es importante y cómo proteger bien tus satoshis.

:mega: **Comparte**: muestra este material a amigos, familia o a ese colega curioso que siempre te pregunta "¿qué es Bitcoin exactamente?".

:teacher: **Enseña**: usa el contenido para llevar Bitcoin adelante. ¿Quién sabe si organizas un meetup o ayudas a formar una nueva generación de bitcoiners?

---

Todos los archivos - videos, slides y otros materiales - están disponibles en [areabitcoin.co](https://areabitcoin.co) y en el [GitHub de Area Bitcoin](https://github.com/areabitcoin/Bitcoin-4-All). Puedes acceder a todo de forma práctica y gratuita, sea para aprender, compartir o enseñar.

Estamos aquí para ayudarte a entender, adoptar y esparcir esta idea transformadora.

**¿Listo para empezar? ¡Vamos!**

---

## :rocket: Empezar Ahora

[Empezar Clase 1 :arrow_right:](es/clase-1.md)

---

## :link: Links

- :globe_with_meridians: [Area Bitcoin](https://areabitcoin.co)
- :bird: [Twitter/X](https://x.com/areabitcoin)
- :tv: [YouTube](https://youtube.com/@AreaBitcoin)
- :camera: [Instagram](https://instagram.com/area.bitcoin)

:cc: Contenido bajo licencia [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
'''

with open('docs/es/intro.md', 'w', encoding='utf-8') as f:
    f.write(intro_es)
print('ES intro.md padronizado!')

# 4. ADICIONAR VIDEOS YOUTUBE EM EN
youtube_en = {
    'class-1': 'XwcvWsniEEM',
    'class-2': 'EPl8Ip64qM8',
    'class-3': 'Z64I8iTy0no',
    'class-4': '81z_nZbmoIc',
    'class-5': 'Fw56Z332YAg',
    'class-6': 'JlRkhmiLH5M',
    'class-7': 'JlRkhmiLH5M',
    'class-8': 'TfKG7nEyq24',
    'class-9': 'AP5h_Ph-wVU',
    'class-10': 'wpNCCAipL8M'
}

for filename, video_id in youtube_en.items():
    filepath = f'docs/en/{filename}.md'
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        youtube_url = f'https://www.youtube.com/watch?v={video_id}'
        thumbnail_url = f'https://img.youtube.com/vi/{video_id}/maxresdefault.jpg'
        embed_url = f'https://www.youtube.com/embed/{video_id}?rel=0'
        
        new_video_section = f'''## :movie_camera: Class Video

[![Watch Video]({thumbnail_url})]({youtube_url})

:point_right: **[Click here to watch on YouTube]({youtube_url})**

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="{embed_url}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="position:absolute;top:0;left:0;width:100%;height:100%;border-radius:12px;" title="Video"></iframe></div>

---'''
        
        # Substituir seção de vídeo existente
        pattern = r'##\s*:?(?:movie_camera:)?\s*(?:Class\s*)?Video.*?(?=\n##[^#]|\n---\n|\Z)'
        if re.search(pattern, content, re.DOTALL | re.IGNORECASE):
            content = re.sub(pattern, new_video_section, content, count=1, flags=re.DOTALL | re.IGNORECASE)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'EN: {filename} -> YouTube {video_id}')

# 5. ADICIONAR VIDEOS VIMEO EM ES
vimeo_es = {
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
        
        new_video_section = f'''## :movie_camera: Video de la Clase

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="{embed_url}" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media" style="position:absolute;top:0;left:0;width:100%;height:100%;border-radius:12px;" title="Video"></iframe></div>

:point_right: **[Ver en Vimeo]({vimeo_url})**

---'''
        
        # Substituir seção de vídeo existente
        pattern = r'##\s*:?(?:movie_camera:)?\s*Video\s*(?:de\s*la\s*)?(?:Clase)?.*?(?=\n##[^#]|\n---\n|\Z)'
        if re.search(pattern, content, re.DOTALL | re.IGNORECASE):
            content = re.sub(pattern, new_video_section, content, count=1, flags=re.DOTALL | re.IGNORECASE)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'ES: {filename} -> Vimeo {video_id}')

print('\nTudo concluido!')
