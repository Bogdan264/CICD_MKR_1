import pytest
import main
import os


#python -m pytest -s -v test_section/

@pytest.fixture
def input_file():
    with open("test1.txt", "w") as f:
        f.write("not neccessary\n")
        f.write("you should stop right now\n")
        f.write("this is human rights\n")
        f.write("dont hurt animals\n")
    yield "test1.txt"
    os.remove("test1.txt")
    os.remove("filtered.txt")


@pytest.mark.parametrize("keyword, expected_output", [
    ("not", "not neccessary\n"),
    ("stop", "you should stop right now\n"),
    ("rights", "this is human rights\n"),
    ("hurt", "dont hurt animals\n"),
    ("Python", "")
])
def test_filter_file(input_file, keyword, expected_output):

    main.removal_by_word_file(input_file, keyword)
    with open("filtered.txt", "r") as f:
        output = f.read()

    assert output == expected_output