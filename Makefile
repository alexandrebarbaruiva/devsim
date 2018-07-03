dev = game/developer.py
empl = game/employee.py
soft = game/software.py
comp = game/company.py
menu = game/main.py
dev_test = tests/unit_tests/test_dev.py
empl_test = tests/unit_tests/test_empl.py
soft_test = tests/unit_tests/test_soft.py
comp_test = tests/unit_tests/test_comp.py
menu_test = tests/unit_tests/test_main.py
working_comp_test = tests/integration_tests/test_working_comp.py
all_unit_tests = $(dev_test) $(empl_test) $(soft_test) $(comp_test) $(menu_test)
all_integration_tests = $(working_comp_test)
all_tests = $(all_unit_tests) $(all_integration_tests)
all_classes = $(dev) $(empl) $(soft) $(comp) $(menu)

default: full

run:
	@python3 game/main.py

full: test cov behave style

test:
	@green3 .

cov:
	@coverage run -m py.test $(all_tests)
	@coverage report -m $(all_classes)
	@coverage html $(all_classes)

html:
	@open -a /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome htmlcov/index.html

style:
	@pycodestyle game/. tests/. --ignore=E402,W504

doc:
	pydocstyle game/. tests/.

install:
	pip install -r requirements.txt

behave:
	@behave tests/features

travis: test style
	coverage run -m py.test $(dev_test) $(empl_test) $(soft_test) $(menu_test)
