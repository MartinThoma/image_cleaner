docs:
	python setup.py upload_docs --upload-dir docs/_build/html

localinstall:
	sudo -H python setup.py install

update:
	python setup.py sdist upload --sign
	sudo -H pip install image_cleaner --upgrade

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