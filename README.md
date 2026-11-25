# Exercism Python Solutions

My solutions to the[Exercism profile](https://exercism.org/profiles/m000n-ux) kept here as a record of my practice in core Python.

## Why this repo

I'm a Data Science student working toward data engineering, and Python is the language I use most. I use Exercism to strengthen the fundamentals through small, focused exercises, each with its own test suite. This repo tracks that progress over time.

## How it works

Solutions are synced automatically from my Exercism account using the [Exercism Solutions Syncer](https://github.com/apps/exercism-solutions-syncer). Each time I submit an iteration on Exercism, the syncer opens a pull request here, which I review and merge into `main`.

## Structure

```
solutions/
└── python/
    └── <exercise-name>/
        └── <iteration>/
            ├── <exercise>.py        # my solution
            └── <exercise>_test.py   # tests provided by Exercism
```

## Running the tests

Each exercise comes with its tests. From inside an exercise folder:

```bash
pip install pytest
pytest
```
