from setuptools import setup
with open("readme.md", "r", encoding="utf-8") as  fh:
        description = fh.read()

AUTHOR_NAME='Ryuga-17'
SRC_REPO='src'
REQUIREMENTS=['streamlit']

setup(
        name='SRC_REPO',
        version='0.0.1',
        author=AUTHOR_NAME,
        author_email='vsawantlm17@gmail.com',
        description='A web app for students and professors',
        long_description = description,
        long_description_content_type='text/markdown',
        url='',
        package=[SRC_REPO],
        python_requires = '>=3.6',
        install_requires=REQUIREMENTS,







)







