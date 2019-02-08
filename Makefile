.PHONY: clean tests cov docs release

VERSION = $(shell pipenv run python -c "print(__import__('django_pinject').__version__)")

install-deps:
	pipenv install

clean:
	rm -fr docs/_build build/ dist/
	pipenv run make -C docs clean

test:
	pipenv run py.test --cov

cov: test
	pipenv run coverage html
	@echo open htmlcov/index.html

apidoc:
	pipenv run make -C docs apidoc

docs:
	pipenv run make -C docs html
	@echo open docs/_build/html/index.html

release:
	@echo About to release ${VERSION}; read
	pipenv run python setup.py sdist upload
	pipenv run python setup.py bdist_wheel upload
	git tag -a "${VERSION}" -m "Version ${VERSION}" && git push --follow-tags
