from bs4 import BeautifulSoup

def html_to_md(html_file, md_file):
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(soup.get_text())


input_file='/Users/dru/Downloads' + '/程序员的底层思维.html'
html_to_md(input_file, 'output.md')

