.PHONY:install run test

install:
	pip install flask requests -U

test:
	python test.py

run:
	python api.py



