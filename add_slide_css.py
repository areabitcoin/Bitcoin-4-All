import re

# Ler o arquivo index.html
with open('docs/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# CSS adicional para slides
slide_css = '''
    /* Slide Images - Larger and Centered */
    .markdown-section img[alt^="Slide"] {
      display: block;
      max-width: 100%;
      width: 100%;
      margin: 30px auto;
      border-radius: 12px;
      box-shadow: 0 4px 20px rgba(247, 147, 26, 0.15);
    }

    /* All images in content */
    .markdown-section img {
      display: block;
      max-width: 100%;
      margin: 20px auto;
      border-radius: 8px;
    }

    /* Slide caption styling */
    .markdown-section img[alt^="Slide"] + p {
      margin-top: 25px;
    }
'''

# Inserir o CSS antes do fechamento do </style>
if 'img[alt^="Slide"]' not in content:
    content = content.replace('  </style>', slide_css + '\n  </style>')
    
    with open('docs/index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(' CSS para slides adicionado!')
else:
    print('- CSS para slides já existe')
