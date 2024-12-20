# Makefile

.PHONY: install run

install:
	pip install -r requirements.txt

run:
	python func/main.py

all: install run
# END