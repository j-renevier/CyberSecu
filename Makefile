# Makefile

.PHONY: install mail run

install:
	pip install -r requirements.txt

mail:
	python func/send_mail.py

run:
	python func/main.py

all: install main run
# END