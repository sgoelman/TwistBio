from behave import *

from src.logic import Logic
from src.main import main

use_step_matcher("re")


# in file "test.txt""
@step("""I validate that receive the correct "(.+)" in "(.+)" file""")
def step_impl(context, output, file_name):
    """
    :type context: behave.runner.Context
    :type output - the required file output : str
    """

    with open(file_name, 'r') as file:
        data = file.read().replace('\n', '')
        file.close()
        assert output in data


@given("""I create a test file "(.+)" with the"(?P<DNA>.+)".""")
def step_impl(context, file_name, DNA):
    """
    :type context: behave.runner.Context
    :type DNA: str
    """
    with open(file_name, "a") as myfile:
        myfile.truncate(0)
        myfile.write(DNA)
    myfile.close()


@when('I convert DNA to amino acid translation from "(.+)" file')
def step_impl(context,file_name):
    """
    :type context: behave.runner.Context
    """
    main(file_name)

    # 'TGCTTATGAAAATTTTAATCTCCCAGGTAACAAACCAACCAACTTTCGATCTCTTGTAGA"'