# Output directory for all build files
$out_dir = 'build';

# Ensure PDF is generated
$pdf_mode = 1;

# Use pdflatex
$pdflatex = 'pdflatex -interaction=nonstopmode -synctex=1 %O %S';

# Clean up options
$clean_ext = 'synctex.gz synctex.gz(busy) run.xml tex.bak bbl bcf fdb_latexmk run tdo %R-blx.bib';
