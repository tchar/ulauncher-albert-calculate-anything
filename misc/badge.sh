data=$(cat misc/python.svg | base64)

python -m pybadges \
    --left-text="python" \
    --right-text="3.6 | 3.7 | 3.8 | 3.9" \
    --left-color='#444D56' \
    --right-color='#007ec6' \
    --left-link=https://www.python.org/ \
    --right-link=https://www.python.org/doc/versions/ \
    --logo="data:image/svg+xml;base64,$data" \
    --embed-logo \
    --whole-title="Python versions" \
    --left-title="Python" \
    --right-title="versions supported" \
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