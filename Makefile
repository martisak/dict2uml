TEST_PATH=./

clean-pyc:
	-find . -name '*.pyc' -exec rm -f {} +
	-find . -name '*.pyo' -exec rm -f {} +

clean-build:
	-rm -rf build/
	-rm -rf dist/
	-rm -rf *.egg-info

test: clean-pyc
	py.test --verbose --color=yes $(TEST_PATH)

