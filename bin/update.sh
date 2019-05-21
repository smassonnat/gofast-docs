#!/bin/bash

make gettext
LANGUAGES=""

for var in "$@"
do
    LANGUAGES="$LANGUAGES -l $var "
done

sphinx-intl update -p _build/locale $LANGUAGES

#sphinx-build -b html -D language=en . _build/html/en

