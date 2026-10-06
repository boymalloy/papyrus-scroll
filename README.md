# Papyrus Scroll

Papyrus Scroll is an experimental web application for creating, managing and publishing structured documents.

It combines a browser-based editing experience with a documentation-as-code workflow, allowing source content to be maintained as Markdown while producing Microsoft Word documents for people who need to work in `.docx`.

The project explores whether the benefits commonly associated with software development — version control, reusable content, structured references and automated document generation — can be applied to large document sets without requiring authors to work directly with developer tooling.

## The Problem

Large document collections can become difficult to maintain when content is spread across multiple Word files.

Changes to document structure often require references to be updated manually, definitions can drift between documents, and managing multiple versions can create significant overhead.

Papyrus Scroll explores a different approach:

- Store source content as Markdown
- Edit content through a browser-based interface
- Use Git for version control
- Generate documentation automatically
- Maintain references between documents
- Export completed documents to Microsoft Word

The intention is not to replace Word as the final document format, but to separate the *source* of a document from the format in which it is ultimately distributed.

## How It Works

The application uses a Python and Flask backend.

Markdown source files are processed using Sphinx, which provides document structure, targets and cross-references. The generated HTML is then converted into Word documents using Pandoc.

The publishing pipeline looks like this:

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

This allows source documents to contain structured references such as:

```text
(payment-terms)=
### Payment terms
```

which can be referenced elsewhere using:

```text
See {ref}`Payment terms`
```

One of the challenges the project explores is preserving those relationships when content is exported as multiple independent Word documents.

## Architecture

The current implementation includes:

- Flask web application
- Browser-based document editing
- File-based Markdown storage
- Sphinx documentation generation
- HTML post-processing
- Automated Word document export via Pandoc

The export process includes custom handling to preserve relationships between generated documents by rewriting internal links before conversion.

## Technology Stack

### Backend

- Python
- Flask
- Jinja

### Documentation Processing

- Markdown
- Sphinx
- Pandoc
- pypandoc

### Frontend

- HTML
- CSS
- JavaScript

### Tooling

- Git
- GitHub

The project has also been used to experiment with browser-based structured editing technologies including:

- Toast UI Editor
- ProseMirror

## What I've Learned

Papyrus Scroll deliberately focuses on problems that were unfamiliar to me when the project began.

Some of the more interesting challenges have included:

- Understanding how Sphinx resolves targets and cross-references
- Inspecting and adapting generated HTML
- Preserving links during HTML-to-Word conversion
- Generating multiple related outputs from a single content set
- Manipulating document structure prior to export
- Integrating JavaScript editors with Flask
- Understanding editor document models versus rendered HTML
- Investigating how tools such as ProseMirror could support richer structured editing workflows

The design has evolved significantly as I've learned more about the problem space.

An early version converted Markdown directly into Word documents. As the project developed, Sphinx and an intermediate HTML stage were introduced because they provide much stronger support for document structure, references and future extensibility.

## Current Status

Papyrus Scroll is a work in progress.

The current focus is:

- Improving the editing experience
- Representing structured references within the editor
- Maintaining Markdown as the source format
- Preserving document relationships during export
- Exploring opportunities to reuse existing open-source tooling

Where established tools can solve a problem effectively, my preference is to understand and integrate them rather than build custom functionality unnecessarily.

## Why I Built It

The idea originated from problems I encountered while working with large, interdependent document sets.

I wanted to explore what would happen if approaches commonly used in software engineering — source control, automated builds, structured source files and reusable references — were applied to document production.

The project has since become both a useful tool and a way to continue developing my Python, JavaScript and software design skills through solving a real-world problem.
