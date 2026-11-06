.PHONY: activate

activate:
	@if [ ! -d venv ]; then \
		python3 -m venv venv; \
		echo "The environment folder was created and the python 🐍 environment was activated"; \
	else \
		echo "Python 🐍 environment was activated"; \
	fi

install:
	pip3 install -r requirements.txt

run:
	fastapi dev src/main.py