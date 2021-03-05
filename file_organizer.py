import argparse


def file_data(file):


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', help='Folder where files are together', required=True)
    parser.add_argument('--destiny', help='Base folder where files must be moved', required=True)

    args = parser.parse_args()

if __name__ == '__main__':
    main()



