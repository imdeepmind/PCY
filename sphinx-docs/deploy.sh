#!/bin/sh
sphinx-apidoc -o ./ ../pcy/
make html
cp -r ./_build/html/* ../docs/
touch ../docs/.nojekyll
