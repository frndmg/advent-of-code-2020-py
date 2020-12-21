# Advent of Code 2020

> Python approach

## Development

Install `pyenv` and `poetry` and install the dependencies.

```
$ poetry install
```

Then run the tests with coverage

```
$ poetry run pytest --cov . --doctest-modules --cov-report xml:cov.xml --cov-report term -f .
```

You can also run the tests without coverage but it is less fancy

```
$ poetry run pytest --doctest-modules -f .
```

If you use VSCode you can check the [Coverage Gutters](https://marketplace.visualstudio.com/items?itemName=ryanluker.vscode-coverage-gutters) extension to display covered lines.
