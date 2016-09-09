test_exercises: start help ignorecase multiplefiles
generate_exercises: generate_grep generate_awk

testrule:
	echo this is a Makefile rule
	echo You can associate it to as many commands you want

notebook:
	jupyter nbconvert --to notebook --execute PEB\ Bash\ Workshop.ipynb

generate_grep:
	python src/generate_grep_exercise.py

generate_awk:
	Rscript src/generate_awk_exercise.R

start:
	grep start data/exercise1_grep.txt

help:
	grep help data/exercise1_grep.txt

ignorecase:
	grep -i -c ignorecase data/exercise1_grep.txt
	grep 21 data/exercise1_grep.txt

multiplefiles:
	grep 'regex' data/multiplefiles/*

piping:
	grep ORGANISM data/genes/mgat_genes.gb | grep 'Homo sapiens'
	grep ORGANISM data/genes/mgat_genes.gb | grep taurus

regex:
	grep 'AAA..TTT' data/genes/sequences.fasta


awk1:
	awk '$$1=="chr8" && $$4>100000 && $$5<200000 ' data/genes/chr8.gff

slides: slides_bash slides_bioc

slides_bash:
	jupyter nbconvert --to slides  PEB\ Bash\ Workshop.ipynb

slides_bioc:
	jupyter nbconvert --to slides  PEB\ Bioconductor\ workshop.ipynb


cow:
	@cowsay -W 12 'I hope you have enjoyed the workshop :-)'
	@cowthink -W 12 "Now let's go to the beach"
