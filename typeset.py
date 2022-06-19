import sys,os,glob
filename = sys.argv[1]
fName = filename.split('.md')[0]
os.system(f'pandoc {filename} --template=cv.tex -o .{fName}.tex')
os.system(f'pdflatex .{fName}.tex')
os.system(f'bibtex .{fName}')
for filename in glob.glob('*.aux'):
    basename = filename.split('.aux')[0]
    os.system(f'bibtex {basename}')
os.system(f'pdflatex .{fName}.tex')
os.system(f'mv .{fName}.pdf {fName}.pdf')
