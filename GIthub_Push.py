#Created by Justin Lo Sept 14 2018


import os

os.system("cd desktop")
os.system("cd CS")
os.system("cd Programming")
os.system("cd GitRepoYear9")
os.system("cd Year9DesignCS4-PythonJL")

text=input('What is your comment for commit: ')

os.system("git status")
os.system("git add .")

sentence = str('git commit -m "{0}"'.format(text))
os.system(sentence)

os.system("git push")
