#!/bin/bash

(for q in 'hello' 'hi' 'sup' 'eh' 'hiiiiiiii' 'flying-from-sfo'; do php app.php $q; python app.py $q; done) | uniq -c

