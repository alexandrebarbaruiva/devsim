from invoke import task
import webbrowser


dev = "game/developer.py"
empl = "game/employee.py"
soft = "game/software.py"
comp = "game/company.py"
menu = "game/main.py"
dev_test = "tests/unit_tests/test_dev.py"
empl_test = "tests/unit_tests/test_empl.py"
soft_test = "tests/unit_tests/test_soft.py"
comp_test = "tests/unit_tests/test_comp.py"
menu_test = "tests/unit_tests/test_main.py"
working_comp_test = "tests/integration_tests/test_working_comp.py"
all_unit_tests = f"{dev_test} {empl_test} {soft_test} {comp_test} {menu_test}"
all_integration_tests = f"{working_comp_test}"
all_tests = f"{all_unit_tests} {all_integration_tests}"
all_classes = f"{dev} {empl} {soft} {comp} {menu}"


@task
def run(c):
    """ Runs game """
    c.run(f"python3 {menu}")


@task
def full(c):
    """ Runs full battery of tests """
    test(c)
    cov(c)
    behave(c)
    style(c)


@task
def test(c):
    """ Runs all unit and integration tests """
    c.run("green3 .")


@task
def cov(c):
    """ Checks code coverage """
    c.run(f"coverage run -m py.test {all_tests}")
    c.run(f"coverage report -m {all_classes}")
    c.run(f"coverage html {all_classes}")


@task
def html(c):
    """ Opens code coverage html """
    c.run("python -m webbrowser -t \"htmlcov/index.html\"")


@task
def style(c):
    """ Checks for PEP8 mistakes """
    c.run("pycodestyle game/. tests/. tasks.py --ignore=E402,W504")


@task
def doc(c):
    """ Checks for PEP8 mistakes """
    c.run("pydocstyle game/. tests/.")


@task
def install(c):
    """ Install all required packages """
    c.run("pip install -r requirements.txt")


@task
def behave(c):
    """ Runs behavior tests """
    c.run("behave tests/features")


@task(pre=[test, style])
def travis(c):
    c.run(f"coverage run -m py.test {all_tests}")
