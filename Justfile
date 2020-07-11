install:
    poetry update && poetry install

run:
    poetry run flask run

poetry-gen-reqs:
    poetry export --without-hashes -f requirements.txt > requirements.txt

test:
    poetry run pytest --cache-clear --new-first --failed-first --verbose
