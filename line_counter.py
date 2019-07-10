import sys
import pathlib

def arg_help():
    print("Wrong input format: " + str(sys.argv[1:]) + "\n")
    print("Please use something like: python3 line_counter.py [PATH] [FILENAME]")
    print("I.e. python3 line_counter.py /home/user/javaproject *.java")

def main():
    p = pathlib.Path(sys.argv[1]).glob('**/' + sys.argv[2])
    files = [str(x) for x in p if x.is_file()]
    #print("\nFiles: " + str(files) + "\n")
    total_lines = 0
    try:
        for file in files:
            file_lines = 0
            file_lines += sum(1 for line in open(file) if (line != "\n" and
            "/*" not in line and "*/" not in line and "//" not in line))
            total_lines += file_lines
            print("Reading " + str(file) + "\nLines: " + str(file_lines))
        print("\nFiles: " + str(len(files)))
        print("\nTotal lines: " + str(total_lines) + "\n")
    except UnicodeDecodeError:
        print("Error: Cannot read " + str(sys.argv[2]) + " files")


if __name__ == '__main__':
    if(len(sys.argv) == 3):
        main()
    else:
        arg_help()
