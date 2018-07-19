from distutils.core import setup

def readFile(fileName):
    with open(fileName) as file: return file.read()

setup(
    name="sqlScanner",
    version="1.0.0",
    author="Henning Arvid Ladewig",
    author_email="anne@opentrash.com",
    py_modules=["sqlScanner"]
    description="Scans .db-files for SQL tables.",
    long_description=readFile("README.md")
)
