#!/bin/sh

version=2.7.5
gittag=k4dirstat-2.7.5

git clone https://bitbucket.org/jeromerobert/k4dirstat.git
git archive --format=tar --prefix=k4dirstat-${version}/ --remote=k4dirstat ${gittag} | bzip2 --best -cf - > k4dirstat-${version}.tar.bz2
