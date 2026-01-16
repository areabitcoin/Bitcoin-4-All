# Publishing Guide - Bitcoin 4 All

This guide explains how to publish the course as a book, documentation site, or presentation slides.

---

## :book: Option 1: Docsify (GitHub Pages)

**Best for:** Free documentation website hosted on GitHub

### Setup

1. **Enable GitHub Pages:**
   - Go to repository Settings > Pages
   - Source: Deploy from a branch
   - Branch: `main`
   - Folder: `/docs`
   - Save

2. **Access your site:**
   ```
   https://areabitcoin.github.io/Bitcoin-4-All/
   ```

### Features
- :white_check_mark: Free hosting on GitHub
- :white_check_mark: Automatic updates on push
- :white_check_mark: Search functionality
- :white_check_mark: Mobile responsive
- :white_check_mark: Dark theme with Bitcoin colors

---

## :books: Option 2: GitBook.com

**Best for:** Professional book-style documentation

### Setup

1. **Create GitBook account:**
   - Go to [gitbook.com](https://gitbook.com)
   - Sign up (free for open source)

2. **Connect GitHub:**
   - Create new space
   - Select "GitHub" as sync source
   - Choose `areabitcoin/Bitcoin-4-All` repository
   - Select `main` branch

3. **Configure:**
   - GitBook will automatically use `SUMMARY.md` and `book.json`
   - Content syncs automatically on every push

### Features
- :white_check_mark: Beautiful default theme
- :white_check_mark: Built-in search
- :white_check_mark: PDF/ePub export
- :white_check_mark: Custom domain support
- :white_check_mark: Analytics

---

## :clapper: Option 3: Marp (Presentation Slides)

**Best for:** Creating slide decks for meetups and workshops

### VS Code Setup (Recommended)

1. **Install extension:**
   - Open VS Code
   - Install "Marp for VS Code" extension

2. **Create slides:**
   - Open `slides/class-1-example.md`
   - Click Marp icon (top-right)
   - Preview appears in side panel

3. **Export:**
   - Click "Export slide deck"
   - Choose format: PDF, PPTX, or HTML

### CLI Setup

```bash
# Install Marp CLI
npm install -g @marp-team/marp-cli

# Convert to PDF
cd slides
marp class-1-example.md -o class-1.pdf

# Convert to PowerPoint
marp class-1-example.md -o class-1.pptx

# Convert all slides
marp *.md -o ./output/

# With custom theme
marp class-1-example.md --theme bitcoin-theme.css -o class-1.pdf
```

### Features
- :white_check_mark: Markdown to slides
- :white_check_mark: PDF, PPTX, HTML export
- :white_check_mark: Custom themes
- :white_check_mark: Speaker notes
- :white_check_mark: Live preview

---

## Quick Comparison

| Feature | Docsify | GitBook | Marp |
|---------|---------|---------|------|
| **Type** | Documentation | Book | Slides |
| **Hosting** | GitHub Pages | GitBook.com | Export files |
| **Cost** | Free | Free (open source) | Free |
| **Setup** | Easy | Easy | Easy |
| **Best for** | Online reading | Professional docs | Presentations |

---

## Recommended Workflow

1. **For online course:** Use **Docsify** (already configured!)
   - Just enable GitHub Pages in settings

2. **For professional book:** Use **GitBook**
   - Connect repository to gitbook.com

3. **For meetups:** Use **Marp**
   - Export slides to PDF/PPTX
   - Present at local events

---

## Files Structure

```
Bitcoin-4-All/
 docs/                    # Docsify site
    index.html          # Main page
    _sidebar.md         # Navigation
    README.md           # Home content
    pt/                 # Portuguese content
    en/                 # English content
    es/                 # Spanish content
 slides/                  # Marp slides
    class-1-example.md  # Example presentation
    bitcoin-theme.css   # Custom theme
    README.md           # Instructions
 SUMMARY.md              # GitBook table of contents
 book.json               # GitBook configuration
```

---

**Questions?** Open an issue on GitHub!
