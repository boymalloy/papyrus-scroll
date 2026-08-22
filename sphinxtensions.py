from pathlib import Path
import pypandoc
import subprocess
import os
import shutil

# Insert headings after each reference target
def insert_headings(md_file):

    copy_result = shutil.copyfile("source/"+ md_file,"source_backup/" + md_file)

    with open('source/'+ md_file, 'r') as file:
        search_text = ")=\n"
        replace_text = ")=\n### "
        data = file.read()
        data = data.replace(search_text, replace_text)

    with open('source/'+ md_file, 'w') as file:
        file.write(data)

    return "got to the end"

def insert_headings_all():
    for root, dirs, files in os.walk("source/"):
            for file in files:
                file_path = Path(file)
                if file_path.suffix == ".md" and file != "index.md":
                    insert_headings(file)

    return "end"

# restore md file
def restore_md(md_file):

    copy_result = shutil.copyfile("source_backup/"+ md_file,"source/" + md_file)

    print("check")
    return "restored"

def restore_md_all():
    for root, dirs, files in os.walk("source_backup/"):
            for file in files:
                file_path = Path(file)
                if file_path.suffix == ".md" and file != "index.md":
                    restore_md(file)

    return "end"

class DocxExporter:
    def __init__(self, html_dir="build/html", output_dir="docs"):
        self.html_dir = Path(html_dir)
        self.output_dir = Path(output_dir)
        self.temp_file = self.html_dir / "temp.html"

    # Run sphinx to create html versions of every md file
    def sphinx_make_html(self):

        clean = subprocess.run(
            ["make", "clean"],
            capture_output=True,
            text=True
        )
        result = subprocess.run(
            ["make", "html"],
            capture_output=True,
            text=True
        )

        return result.returncode

    # Convert an html file to a docx file, including updating the links within the files
    def html_docx_convert(self, html_file):
        html_path = Path(html_file)
        slug = html_path.stem

        with open(html_file, 'r') as file:
            
            # find .html links within the html file and replace them with .docx links
            search_text = ".html"
            replace_text = ".docx"
            data = file.read()
            data = data.replace(search_text, replace_text)

        # Write the updated file as a temp file
        with open('build/html/temp.html', 'w') as file:
            file.write(data)
        
        # Convert the temp file to a docx file using pandoc
        pypandoc.convert_file("build/html/temp.html", "docx", outputfile="docs/" + slug + ".docx")

        # return a data version of the updated html file for testing
        return data

    def convert_all(self):

        # Insert headings after each reference target
        insert_headings_all()
        print("headings")
        
        # Make fresh versions of all the html files
        self.sphinx_make_html()
        
        # Get all the files in the html folder
        all_files = [
            os.path.join(root, file)
            for root, dirs, files in os.walk("build/html")
            for file in files
        ]

        # Loop through all the files
        for file in all_files:
            file_path = Path(file)
            # where the file is an html file
            if file_path.suffix == ".html":
                # ... convert it to a docx and update the links within it
                self.html_docx_convert(file)
                # Remove the temp html file that needs to be created each time 
                os.remove("build/html/temp.html")

        # put the original versions of the md files without the headings back in the source folder
        restore_md_all()