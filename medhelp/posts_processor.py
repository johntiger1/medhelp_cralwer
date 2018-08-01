import glob
import os
from termcolor import colored
from sklearn.model_selection import train_test_split

def process_file(filename):
    with open("../posts/" + filename, "r") as file:
        # remove all the new lines
        next(file)
        content = file.read()
        # print(os.getcwd())

        try:
            with open(os.path.join(".." , "processed",  filename + "p"), "w") as write_file:

                x = content.replace("\n", "").strip()
                if len(x.splitlines()) > 1:
                    print("hmm")
                    print(file)
                write_file.write(x)
        except Exception as e:
            print (colored(e, "red"))
            pass


def proc_files():

    # This is a deprecated approach!
    counter = 0
    real_glob =[]
    for file in glob.iglob("../posts/*", recursive=True):
        counter += 1
        real_glob.append(file.split('/')[-1])
    print (counter)

    counter = 0
    os_walk = []
    for (dirpath, dirnames, filenames) in os.walk("../posts"):

        for filename in filenames:
            counter +=1
            os_walk.append(filename)

            if (filename not in real_glob):

                print(filename)

            process_file(filename)
        # print("the file is " + filenames)


    print(counter)


# for file in glob.iglob("../posts/*.*", recursive=True):
#     print("the file is " + file.replace("\r", ""))
    # process_file(file)

def create_masterfile():
    counter = 0
    with open("../processed/masterfile.txt", "w") as catfile:
        for (dirpath, dirnames, filenames) in os.walk("../processed"):

            for file in filenames:

                # There is an interesting self-read problem here!
                if file == "masterfile.txt": continue
                counter+=1
                with open(os.path.join(dirpath,file)) as curr_file:
                    content = curr_file.read()
                    content_lines = content.splitlines()
                    if len(content_lines) > 1:
                        print ("hmm")
                        print(file)

                    catfile.write("{}\n".format(content))
        print(counter)
# creates the test train split
def create_test_train_split():

    # We can do it for just one file to demonstrate that it works
    with open("../processed/masterfile.txt", "r") as catfile:
        lines = catfile.readlines()

        print(len(lines))
        train, test = train_test_split(lines, test_size=0.2)
        test, dev = train_test_split(test, test_size=0.5)

        print ("train has {} lines".format(len(train)))
        print ("test has {} lines".format(len(test)))
        print ("dev has {} lines".format(len(dev)))


    pass
proc_files()
create_masterfile()
create_test_train_split()


# process_file(filename = "/h/johnchen/Desktop/git_stuff/medhelp_crawler/medhelp/posts/(Diet) same everyday#1939708")