#!/bin/sh
echo "--> Building rst files"
sphinx-apidoc -o ./ ../pcy/

echo "--> Building HTML files"
make html

echo "--> Moving the HTML files to the correct directory"
cp -r ./_build/html/* ../doc_build/
