default: pdf

compile:
	latex scl.tex </dev/null
	latex scl.tex </dev/null

clean:
	rm -rf scl.aux scl.log scl.toc scl.dvi

clean_all: clean
	rm -rf scl.pdf

pdf: compile clean
