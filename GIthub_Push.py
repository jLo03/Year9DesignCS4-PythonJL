#Created by Justin Lo Sept 14 2018


import os

os.system("cd desktop")
os.system("cd CS")

text=input('What is your comment for commit: ')

os.system("git status")
os.system("git add .")

sentence = str('git commit -m "{0}"'.format(text))
os.system(sentence)

os.system("git push")
