#!/bin/bash

rm -rf testrepo
mkdir -p testrepo
cd testrepo
git init

date > readme.txt
git add .
git commit -m 'master'

git checkout -b 'foo'
date > foo.txt
git add .
git commit -m 'foo1'

git checkout master
git merge foo --no-ff -m test1

git checkout 'foo'
date >> foo.txt
git commit -am 'foo2'

git checkout master
git merge foo --no-ff -m test2

git checkout master
git lg --all --graph
