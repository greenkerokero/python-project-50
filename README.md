### Hexlet tests and linter status:
[![Actions Status](https://github.com/greenkerokero/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/greenkerokero/python-project-50/actions)
[![Python CI](https://github.com/greenkerokero/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/greenkerokero/python-project-50/actions/workflows/pyci.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/70c44d23dc5e0e1f6d9e/maintainability)](https://codeclimate.com/github/greenkerokero/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/70c44d23dc5e0e1f6d9e/test_coverage)](https://codeclimate.com/github/greenkerokero/python-project-50/test_coverage)

Gendiff compares two json or yaml files and shows a difference

Gendiff — a utility for comparing json or yaml files
Compares two json or yaml files and shows the differences between them. It supports different output formats, allowing you to customize how the results are displayed.

## System requirements
- Python >= 3.11

## Setup
make install
make build
make package-install

## Usage
gendiff [options] FILE1 FILE2
Options:
- -h, --help
Show help information about the utility and exit.

- -f FORMAT, --format FORMAT
Specify the output format for the differences. Available formats:
 - stylish (default) — a formatted and easy-to-read output with colors and indentation.
 - plain — a simple text output without extra decorations.
 - json — output in JSON format, useful for further processing or integration with other tools.

[![asciicast](https://asciinema.org/a/Zwvonc5f5wM3gIlHIYCw7sQwa.svg)](https://asciinema.org/a/Zwvonc5f5wM3gIlHIYCw7sQwa)

## Examples
Differense between flat json files with stylish (default) output
[![asciicast](https://asciinema.org/a/lCafl3wylk6fnfQezgRXKvUjR.svg)](https://asciinema.org/a/lCafl3wylk6fnfQezgRXKvUjR)

Differense between flat yaml files with stylish (default) output
[![asciicast](https://asciinema.org/a/slQs6wY8UsqHn1JdKzhRVWI86.svg)](https://asciinema.org/a/slQs6wY8UsqHn1JdKzhRVWI86)

Differense between nested json files with stylish (default) output
[![asciicast](https://asciinema.org/a/nGxcbICeEK2aSLBDMIXjkKVVc.svg)](https://asciinema.org/a/nGxcbICeEK2aSLBDMIXjkKVVc)

Differense between nested yaml files with stylish (default) output
[![asciicast](https://asciinema.org/a/7sR9PocvFaKBSVMZmYQ4xsNYV.svg)](https://asciinema.org/a/7sR9PocvFaKBSVMZmYQ4xsNYV)

Differense between nested json files with plain output
[![asciicast](https://asciinema.org/a/4VQC2MMyy3MggcUlH7Ckq31Q2.svg)](https://asciinema.org/a/4VQC2MMyy3MggcUlH7Ckq31Q2)

Differense between nested yaml files with plain output
[![asciicast](https://asciinema.org/a/yMDLD17hVTeMrf89h4a1YOqwk.svg)](https://asciinema.org/a/yMDLD17hVTeMrf89h4a1YOqwk)

Differense between nested json files with json output
[![asciicast](https://asciinema.org/a/Z9CAQRomgBVXfRnDVOrcwTZgb.svg)](https://asciinema.org/a/Z9CAQRomgBVXfRnDVOrcwTZgb)

Differense between nested yaml files with json output
[![asciicast](https://asciinema.org/a/GJSOOFWhXCYz7eSpRR8Ejuy4r.svg)](https://asciinema.org/a/GJSOOFWhXCYz7eSpRR8Ejuy4r)
