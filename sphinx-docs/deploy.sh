#!/bin/sh
echo "--> Building rst files"
sphinx-apidoc -o ./ ../pcy/

echo "--> Building HTML files"
make html
