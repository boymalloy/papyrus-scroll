import app
import os

def test_sphinx_make_html():
    assert app.sphinx_make_html() == 0

def test_html_docx_convert():
    # Read the content of the control file (the thing to test against) into a variable
    with open("test_files/html_after_control.html", 'r') as target_state_file:
        target_state = target_state_file.read()

    # The function builds the temp html file that will be converted to a docx
    app.html_docx_convert("test_files/html_before.html")

    # Read the content of the temp file into a variable
    with open("build/html/temp.html", 'r') as temp_file:
        temp = temp_file.read()

    # The temp file should match the target state (with .html replaced with .docx)
    assert temp == target_state

    # Delete the temp file
    os.remove("build/html/temp.html")