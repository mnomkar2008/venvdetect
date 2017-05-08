#!/usr/bin/python

"""Script to detect current working directory virtual environment"""
import os

def directory_has_activate(dir_path):
    # You should know the dir file related python modules
    file_path = os.path.join(dir_path, 'bin', 'activate')
    return os.path.isfile(file_path)

def main():
    dir_path = "/home/somkar/venv-appjenkins/venv-appjenkins"
    print directory_has_activate(dir_path)
    if directory_has_activate(dir_path):
        # Print the content of the directory path
        print "Contents of", dir_path
        for item in os.listdir(dir_path):
            print item,
    else:
        print "No such path exists : ", dir_path

if __name__ == '__main__':
    main()

# Output should be in the form of
# List of available venv and git directories
# Option 1 venv directory
# Option 2 git directory
# sort according to last used
# sort according to last commited
# delete entire content 
# summary / description


