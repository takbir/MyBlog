initdb:
		python db/init/init_all.py
test:
		py.test tests -s