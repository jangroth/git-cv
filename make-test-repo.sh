#!/bin/bash

rm -rf testrepo
mkdir -p testrepo
cd testrepo
git init

date > readme.txt
git add .
git commit -m 'master'

git checkout -b 'education'
date > foo.txt
git add .
git commit -m 'foo1'

git checkout -b 'developer'
date > bar.txt
git add .
git commit -m 'software engineer'
git tag 'acme.com'

git checkout master
git merge foo --no-ff -m test1

git checkout 'education'
date >> foo.txt
git commit -am 'foo2'
git tag 'thistag3'

git checkout master
git merge 'education' --no-ff -m test2

# end
git checkout master
git log --all --graph \
	--date=short \
	--pretty='%d %cd - %s'
