# Slides - Bitcoin 4 All

This folder contains presentation slides built with **Marp**.

## What is Marp?

[Marp](https://marp.app/) converts Markdown files into beautiful presentations (PDF, PPTX, HTML).

## How to Use

### Option 1: VS Code Extension (Recommended)

1. Install the **Marp for VS Code** extension
2. Open any `.md` file in this folder
3. Click the Marp icon in the top-right corner
4. Export to PDF, PPTX, or HTML

### Option 2: Marp CLI

```bash
# Install
npm install -g @marp-team/marp-cli

# Convert to PDF
marp class-1-example.md -o class-1.pdf

# Convert to PPTX
marp class-1-example.md -o class-1.pptx

# Convert to HTML
marp class-1-example.md -o class-1.html

# With custom theme
marp class-1-example.md --theme bitcoin-theme.css -o class-1.pdf
```

## Files

| File | Description |
|------|-------------|
| `class-1-example.md` | Example slide deck for Class 1 |
| `bitcoin-theme.css` | Custom Bitcoin-orange theme |

## Creating Your Own Slides

1. Copy `class-1-example.md` as a template
2. Edit the content from the course scripts
3. Export using Marp

## Theme Colors

- Background: Dark blue gradient (`#1a1a2e` to `#16213e`)
- Accent: Bitcoin orange (`#f7931a`)
- Text: White (`#ffffff`)
