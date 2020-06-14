from behave import *

from src.logic import Logic

use_step_matcher("re")


@given("I am logged in to application")
def step_impl(context):
    # this is not an app that is why I did not implement
    pass


@when('I convert DNA to amino acid translation on "(?P<DNA>.+)" I should')
def step_impl(context, DNA):
    """
    :type context: behave.runner.Context
    :type DNA - input string  : str
    """
    logic = Logic()
    logic.convert_DNA_to_AA(DNA, False)
    total_combinations = logic.convert_back_to_DNA()
    logic.write_output(total_combinations)
    print("Test conversion result:" + str(logic.amino_acid_output) + str(logic.min_seq_length))


@step('I validate that I receive the correct "(.+)"')
def step_impl(context, output):
    """
    :type context: behave.runner.Context
    :type output - the required file output : str
    """

    with open('output.txt', 'r') as file:
        data = file.read().replace('\n', '')
        assert output in data
