
all: update start docs ignorecase regex multiplefiles

update:
	python src/generate_grep_exercise.py

start:
	grep start data/exercise1_grep.txt

docs:
	grep docs data/exercise1_grep.txt

ignorecase:
	grep ignore-case data/exercise1_grep.txt

regex:
	grep regex data/exercise1_grep.txt

multiplefiles:
	grep 'multiple files' data/exercise1_grep.txt


