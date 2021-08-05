#!/bin/sh

python -m pybadges \
    --left-text="platforms" \
    --right-text="Linux | Windows | macOS " \
    --left-color='#444D56' \
    --right-color='#818181' \
    --whole-title="Platforms supported" \
    --left-title="Plaforms" \
    --right-title="platforms supported" \
    --browser

# python -m pybadges \
#     --right-text=example \
#     --left-color='#444D56' \
#     --right-color='#28A745' \
#     --left-link=http://www.complete.com/ \
#     --right-link=http://www.example.com \
#     --logo='data/misc/python.svg' \
#     --embed-logo \
#     --whole-title="Badge Title" \
#     --left-title="Left Title" \
#     --right-title="Right Title" \
#     --browser