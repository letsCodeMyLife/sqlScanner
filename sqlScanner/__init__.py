import sys
import re

def main():
    if len(sys.argv) == 2:
        file = sys.argv[1]

        tables = getTables(file)

    print(tables)

def getTables(file):
    fileStream = open(file, "rb")
    fileData = fileStream.read()

    fileStream.seek(0)

    matches = tuple(re.finditer(b"CREATE TABLE ", fileData))

    names = list()

    for match in matches:
        names.append("")
        fileStream.seek(match.span()[-1])

        while True:
            char = fileStream.read(1)

            if not char == b" ":
                names[-1] += char.decode()
            else:
                break

    return names

if __name__ == "__main__":
    main()
