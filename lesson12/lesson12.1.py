import codecs
import re

def delete_html_tags(html_file: str, result_file: str = 'cleaned.txt') -> None:
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()


    cleaned = re.sub(r'<[^>]+>', '', html)
    cleaned = '\n'.join([line.strip() for line in cleaned.split('\n') if line.strip()])


    with codecs.open(result_file, 'w', 'utf-8') as output:
        output.write(cleaned)


delete_html_tags('draft.html', result_file='cleaned.txt')