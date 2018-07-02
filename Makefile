dev = game/developer.py
empl = game/employee.py
soft = game/software.py
dev_test = tests/unit_tests/test_dev.py
empl_test = tests/unit_tests/test_empl.py
soft_test = tests/unit_tests/test_soft.py

default: full

full: test behave style

test:
	green3 .

cov:
	coverage run -m py.test $(dev_test) $(empl_test) $(soft_test)
	coverage report -m $(dev) $(empl) $(soft)
	coverage html $(dev) $(empl) $(soft)

style:
	@pycodestyle game/. tests/. --ignore=E402,W504

doc:
	pydocstyle game/. tests/.

install:
	pip install -r requirements.txt

behave:
	behave tests/features
