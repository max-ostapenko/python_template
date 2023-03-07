init:
	# Create virual env
	python3 -m pip install --upgrade --quiet pip
	python3 -m venv env
	source env/bin/activate
	pip3 install --upgrade --quiet -r requirements.txt

test:
	# Install pytest
	python3 -m pip install --upgrade --quiet pytest
	python3 -m pytest --version
	pytest tests/.*

lint:
	# Install black
	python3 -m pip install --upgrade --quiet black
	python3 -m black --version
	black .

	# Install flake8
	python3 -m pip install --upgrade --quiet flake8
	python3 -m flake8 --version
	flake8 .

