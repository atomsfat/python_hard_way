from sys import argv
from os.path import exists

script, filename, to_file = argv

print(f"Copying from file {filename} to {to_file}")
in_file = open(filename)
in_data = in_file.read()

print(f"The input file is {len(in_data)} bytes long")
print(f"Does the output file exist {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort")
input()
out_file = open(to_file, 'w')
out_file.write(in_data)
print("Allright, all done")
out_file.close()
in_file.close()
