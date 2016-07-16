initdb:
		python db/init/init_all.py
test:
		py.test tests -s
develop:
		pip install -r dev_requirements.txt