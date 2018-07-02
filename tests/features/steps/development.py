from behave import *
from unittest import TestCase
from game.developer import Developer
from game.software import Software


@given('we have a dev and an unfinished software')
def step_impl(context):
    context.dev = Developer()
    context.soft = Software()


@when('dev codes 1 unit')
def step_impl(context):
    assert context.dev.develop(context.soft) is True


@then('software will complete 1 unit')
def step_impl(context):
    assert context.soft.stats["completion"] == 1
