.PHONY: install-packages clean


install-packages:
	pip install -r requirements.txt

clean:
	git clean -xdf -e .idea/
