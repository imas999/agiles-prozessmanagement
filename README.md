# Agiles Prozessmanagement - Mobilfunksysteme

Wissenschaftliches Paper zum Generationsvergleich von Mobilfunksystemen.

## Struktur

- `main.tex` - Hauptdatei
- `images/` - Bilder und Grafiken
- `build/` - Build-Verzeichnis für generierte Dateien

## Build-Anleitung

### Voraussetzungen
- LaTeX-Distribution (z.B. MiKTeX oder TeX Live)
- latexmk (empfohlen)

### Kompilieren

Mit latexmk:
```bash
latexmk -pdf main.tex
```

Mit pdflatex:
```bash
pdflatex -output-directory=build main.tex
```

Die PDF wird im `build/` Verzeichnis erstellt.

## Autor

Sami El Aidi  
Hochschule Karlsruhe – Technik und Wirtschaft
