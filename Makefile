ifneq (,$(wildcard .env))
$(info Found .env file.)
	include .env
	export
endif

export PYTHONPATH := $(shell pwd):$(PYTHONPATH)


black:
	black .
isort:
	isort .
style:
	flake8 .
types:
	mypy .
test:
	pytest --lf -vv --cov=nl_economist --cov-branch .
check:
	make black isort style types test
