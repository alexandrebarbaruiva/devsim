from behave import *
from unittest import TestCase
from game.developer import Developer
from game.software import Software


@given('we have a level 1 dev and an unfinished software')
def step_impl(context):
    context.dev = Developer()
    context.soft = Software("Test")


@when('dev codes 1 unit')
def step_impl(context):
    assert context.dev.develop(context.soft) is True


@then('software will complete 1 unit')
def step_impl(context):
    assert context.soft.stats["completion"] == 1


@given('there is a completion 99 software')
def step_impl(context):
    context.dev = Developer()
    context.soft = Software("Test")
    context.soft.stats["completion"] = 99


@then('software will reach 100 and become ready for release')
def step_impl(context):
    assert context.soft.stats["completion"] == 100
    assert context.soft.stats["releasable"] is True
    assert context.soft.stats["released"] is False


@given('there is a completion 100 software')
def step_impl(context):
    context.dev = Developer()
    context.soft = Software("Test", 100)


@when('dev releases software')
def step_impl(context):
    assert context.soft.stats["released"] is False
    assert context.dev.release(context.soft) is True


@then('software gets released')
def step_impl(context):
    assert context.soft.stats["released"] is True
