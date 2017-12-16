#!/bin/bash

VERSION=$1

script="$0"
basename="$(dirname $script)"
cd $basename/../src

python setup.py bdist_wheel

gpg2 --detach-sign -a dist/iglo-$VERSION-py2.py3-none-any.whl

twine upload dist/iglo-$VERSION-py2.py3-none-any.whl dist/iglo-$VERSION-py2.py3-none-any.whl.asc