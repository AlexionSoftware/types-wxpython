poetry run python -m generator
poetry run isort wx-stubs
poetry run yapf -i -p -r wx-stubs
