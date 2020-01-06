import sys
from emex import emex

def main():
    if(len(sys.argv) < 2):
        print("Specify a file so I can extract emojis from!")
        sys.exit(1)
    else:
        with open(sys.argv[1], 'r') as input_file:
            print(emex(input_file.read()))

if __name__ == "__main__":
    main()
