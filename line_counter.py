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
        in_comment = False
        for file in files:
            file_lines = 0
            for line in open(file):
                line = line.replace(" ", "").replace("\t", "")
                if(line != "\n" and "//" != line[0:2]):
                    if "/*" in line:
                        in_comment = True
                    if "*/" in line:
                        in_comment = False
                    if not in_comment:
                        #print("Line: " + line)
                        file_lines +=1
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
