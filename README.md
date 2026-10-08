# Papyrus Scroll

Papyrus Scroll is an experimental web application for creating, managing and publishing collections of interlinking documents, such as contracts.

## The Problem

Large document collections can become difficult to maintain when content is spread across multiple Word files. Changes to document structure often require references to be updated manually, definitions can drift between documents, and managing multiple versions can create significant overhead.

This project explores whether the benefits commonly associated with software development — version control, reusable content, structured references and automated document generation — can be applied to large document sets without requiring authors to work directly with developer tooling. It combines browser-based editing with a documentation-as-code workflow, allowing source content to be maintained as Markdown which can be exported as Microsoft Word documents.

## Why I am building it

Recently I built [an application for creating, managing and visualising family trees](https://github.com/boymalloy/python-flask-d3-family-tree). This helped me to learn:

- Python
- Flask
- Test-driven development
- PostreSQL
- Git
- AWS

I wanted to apply what I'd learned to a real-life problem and challenge myself to learn more. So far I have learned about:

- Approaching a real problem that I have encountered at work
- Problem solving by experimentation
- Using established open source tools linked together in a new combination
- JavaScript

## How It Works

```text
Markdown
    ↓
  Sphinx
    ↓
   HTML
    ↓
  Pandoc
    ↓
Word (.docx)
```

Markdown source files are rendered as HTML using Sphinx, which provides document templates and auto updating cross-references. The generated HTML is then converted into Word documents using Pandoc.

## Technology Stack

### Backend

- Python
- Flask
- Jinja

### Documentation Processing

- Toast UI Editor or ProseMirror
- Markdown
- Sphinx
- Pandoc
- pypandoc

### Frontend

- HTML
- CSS
- JavaScript
