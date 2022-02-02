maint:
	pip install -r requirements/dev.txt
	pre-commit autoupdate && pre-commit run --all-files
	pip-compile -U setup.py
	pip-compile -U requirements/ci.in
	pip-compile -U requirements/dev.in

docs:
	python setup.py upload_docs --upload-dir docs/_build/html

localinstall:
	sudo -H python setup.py install

upload:
	make clean
	python setup.py sdist bdist_wheel && twine upload -s dist/*

test:
	nosetests --with-coverage --cover-erase --cover-package image_cleaner --logging-level=INFO --cover-html

testall:
	make test
	cheesecake_index -n image_cleaner -v

count:
	cloc . --exclude-dir=docs,cover,dist,image_cleaner.egg-info

countc:
	cloc . --exclude-dir=docs,cover,dist,image_cleaner.egg-info,tests

countt:
	cloc tests

clean:
	rm -f *.hdf5 *.yml *.csv
	find . -name "*.pyc" -exec rm -rf {} \;
	find . -type d -name "__pycache__" -delete
	sudo rm -rf build
	sudo rm -rf cover
	sudo rm -rf dist
	sudo rm -rf image_cleaner.egg-info
