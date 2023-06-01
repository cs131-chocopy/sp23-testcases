#!/usr/bin/python3
import os
import subprocess
import shutil

prefix = "sp23-chocopy1-"
pa = 1

def pull_repo(names):
    for name in names:
        repo = prefix + name
        if os.path.exists(repo):
            os.system(f"cd {repo} && git pull")
        else:
            repo_git = f"git@github.com:cs131-chocopy/{repo}.git"
            os.system(f"git clone --depth=1 {repo_git}")

def move_testcases(names):
    assert os.path.exists(f"../../pa{pa}/")
    dest = f"../../pa{pa}/student"
    if os.path.exists(dest):
        shutil.rmtree(dest)
    os.mkdir(dest)
    for name in names:
        repo = prefix + name
        src = f"{repo}/tests/pa{pa}/student"
        if os.path.exists(src):
            files = os.listdir(src)
            assert(len(files) >= 4)
            for file in files:
                src_file = f"{src}/{file}"
                dest_file = f"{dest}/{file}"
                shutil.copyfile(src_file, dest_file)
        else:
            print(f"{name} no testcase")

if not os.path.exists("temp"):
    os.mkdir("temp")
os.chdir("temp")
for pa in range(1, 1 + 4):
    prefix = f"sp23-chocopy{pa}-"
    if pa == 1:
        names = ["Ameiyo", "HenryZ16", "chichu0111", "caoster", "DFPMTS", "GKxxQAQ"]
    else:
        names = ["sp23-team-1", "sp23-team-3", "wa-automaton"]
    if not os.path.exists(f"pa{pa}"):
        os.mkdir(f"pa{pa}")
    os.chdir(f"pa{pa}")
    pull_repo(names)
    move_testcases(names)
    os.chdir("..")