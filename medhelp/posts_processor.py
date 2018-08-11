import glob
import os
from termcolor import colored
from sklearn.model_selection import train_test_split
import gensim
import spacy

# Utility script to process crawled medhelp files
#
nlp = spacy.load('en_core_web_sm')

def process_file(filename):
    with open("./posts/" + filename, "r") as file:
        # remove all the new lines
        next(file)
        content = file.read()
        # print(os.getcwd())

        try:
            with open(os.path.join(".." , "aug11_preproc",  filename + "p"), "w") as write_file:

                x = content.replace("\n", "").strip()

                doc = nlp(content)
                for sent in doc.sents:
                    # empirically this would be good
                    # we definitley want the punctuation

                    if len(str(sent).split()) > 3:
                        print (sent)
                        # write_file.write(str(sent))
                        # write_file.write("\n")

                if len(x.splitlines()) > 1:
                    print("hmm")
                    print(file)
                write_file.write(x)
        except Exception as e:
            print (colored(e, "red"))
            pass


def proc_files():


    with open("dummy.txt", "w") as file:
        file.write("adw")

    # This is a deprecated approach!
    counter = 0
    real_glob =[]
    for file in glob.iglob("./posts/*", recursive=True):
        counter += 1
        real_glob.append(file.split('/')[-1])
    print (counter)



    counter = 0
    os_walk = []
    for (dirpath, dirnames, filenames) in os.walk("./posts"):

        for filename in filenames:
            counter +=1
            os_walk.append(filename)

            if (filename not in real_glob):

                print(filename)

            process_file(filename)
            input()
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

        with open("/h/johnchen/Desktop/git_stuff/medhelp_crawler/medical.train.0", "w") as train_file, open ("/h/johnchen/Desktop/git_stuff/medhelp_crawler/medical.test.0", "w") as test_file, open("/h/johnchen/Desktop/git_stuff/medhelp_crawler/medical.dev.0", "w") as dev_file:
            # train_file.write("wjhewhqqeh what is going on")
            train_file.write("".join(train))
            test_file.write("".join(test))
            dev_file.write("".join(dev))

def create_test_train_split_mimic():

    # We can do it for just one file to demonstrate that it works
    with open("/h/johnchen/psql_results/baseline_catfile.txt", "r") as catfile:
        lines = catfile.readlines()

        print(len(lines))
        train, test = train_test_split(lines, test_size=0.2)
        test, dev = train_test_split(test, test_size=0.5)

        print ("train has {} lines".format(len(train)))
        print ("test has {} lines".format(len(test)))
        print ("dev has {} lines".format(len(dev)))

        with open("/h/johnchen/Desktop/git_stuff/medhelp_crawler/medical.train.1", "w") as train_file, open ("/h/johnchen/Desktop/git_stuff/medhelp_crawler/medical.test.1", "w") as test_file, open("/h/johnchen/Desktop/git_stuff/medhelp_crawler/medical.dev.1", "w") as dev_file:
            # train_file.write("wjhewhqqeh what is going on")
            train_file.write("".join(train))
            test_file.write("".join(test))
            dev_file.write("".join(dev))


print(os.getcwd())
proc_files()
# create_masterfile()
# create_test_train_split_mimic()
# with open("/h/johnchen/medical.train.0", "w") as train_file, open("medical.test.0", "w") as test_file, open("medical.dev.0",                                                                                 "w") as dev_file:
#     train_file.write("wjhewhqqeh what is going on")

# process_file(filename = "/h/johnchen/Desktop/git_stuff/medhelp_crawler/medhelp/posts/(Diet) same everyday#1939708")