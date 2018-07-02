dev = game/developer.py
empl = game/employee.py
soft = game/software.py
menu = game/main.py
dev_test = tests/unit_tests/test_dev.py
empl_test = tests/unit_tests/test_empl.py
soft_test = tests/unit_tests/test_soft.py
menu_test = tests/unit_tests/test_main.py

default: full

run:
	@python3 game/main.py

full: test cov behave style

test:
	@green3 .

cov:
	@coverage run -m py.test $(dev_test) $(empl_test) $(soft_test) $(menu_test)
	@coverage report -m $(dev) $(empl) $(soft) $(menu)
	@coverage html $(dev) $(empl) $(soft) $(menu)

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
