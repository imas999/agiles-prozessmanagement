# Auxiliary directory for build files (not PDF)
$aux_dir = 'build';

# PDF stays in main directory
$out_dir = '.';

# Ensure the build directory exists
system("mkdir -p build");

# Ensure PDF is generated
$pdf_mode = 1;

# Use pdflatex
$pdflatex = 'pdflatex -interaction=nonstopmode -synctex=1 %O %S';

# Clean up options
$clean_ext = 'synctex.gz synctex.gz(busy) run.xml tex.bak bbl bcf fdb_latexmk run tdo %R-blx.bib';
