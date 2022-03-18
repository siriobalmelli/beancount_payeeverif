# beancount payeeverif

`beancount_payeeverif` is the "payee verification" plugin for [beancount][],
fulfilling the following functions:

1. Every transaction has a non-NULL `payee` field:

    ```beancount
    ; this will throw an error
    2020-06-01  *   ""   "fix faucet leak"
      Expenses:General
      Assets:Bank -150 bean

    ; this will pass validation
    2020-06-02  *   "plumber"   "fix faucet leak"
      Expenses:General
      Assets:Bank -150 bean
    ```

1. *TODO: coming soon* Transactions touching certain accounts must match
    an `allowed_payees` regex.

## installation

```bash
pip install beancount_payeeverif
```

## usage

In your toplevel `.beancount` file, include:

```beancount
plugin  "beancount_payeeverif"
```

See the `.beancount` files in [test](./test) for examples.

## developing

Install package and dev requirements locally:

```bash
python3 -m pip install -e .[dev]
```

Run tests:

```bash
python3 -m pytest
```

Build both binary and source distributions locally:

```bash
python3 setup.py bdist_wheel sdist
```

See [sanitize.sh](./sanitize.sh) for maintainer's personal tooling.

[beancount]: http://furius.ca/beancount/
