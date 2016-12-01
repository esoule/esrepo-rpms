#!/bin/sh
export LANG=C
export LC_ALL=C
export TZ=UTC

version=1.3.6
gittag=1.3.6

git clone https://github.com/symless/synergy.git
git archive --format=tar --prefix=synergy-${version}/ --remote=synergy ${gittag} | gzip -9 -n -cf - > synergy-${version}.tar.gz
