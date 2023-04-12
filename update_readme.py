import os
import codecs
from github import Github


def login():
    global user, username
    username = os.environ.get('GITHUB_LOGIN')
    password = os.environ.get('GITHUB_TOKEN')
    user = Github(username, password)

def get_repo():
    global repo
    repo = user.get_repo(os.environ.get('GITHUB_REPOSITORY'))

def get_solution_files():
    contents = repo.get_contents("")
    global solution_file_list
    solution_file_list = []
    for content_file in contents:
        if content_file.type == 'file' \
                and content_file.name.endswith('.md') \
                and not content_file.name == 'README.md':
            solution_file_list.append((content_file.name[:-3], content_file.html_url))
    print(solution_file_list)

def generate_readme_md_content():
    content = f'# My CSS Battle Solutions\n'
    for solution_file in solution_file_list:
        content += f'- [{solution_file[0]}]({solution_file[1]})\n'
    print(content)
    return content


def update_readme_md_file(content):
    with codecs.open('README.md', 'w', encoding='utf-8') as f:
        f.writelines(content)
        f.flush()
        f.close()

if __name__ == '__main__':
    login()
    get_repo()
    get_solution_files()
    content = generate_readme_md_content()
    update_readme_md_file(content)
