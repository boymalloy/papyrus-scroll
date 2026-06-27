from pathlib import Path
import app

def test_list_source_files():
    
    source_files = app.list_source_files()
    
    # source_files should be a list
    assert isinstance(source_files, list)

    # List should not be empty
    assert source_files != []

    # check each item in the list
    for item in source_files:
        
        # each sub item is a string
        for subitem in item:
            assert isinstance(subitem, str)
        
        # the file_name subitem has the extension .md
        file_name = Path(item[0])
        assert file_name.suffix == ".md"