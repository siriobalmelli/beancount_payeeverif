#!/usr/bin/env python
"""
beancount_payeeverif
Verify that all transactions have a payee.
"""

__plugins__ = ('payeeverif', )

# Error reporting done with a custom collection
from collections import namedtuple
PayeeError = namedtuple('PayeeError', 'source message entry')


def payeeverif(entries, options):
    """
    Anything which has a "payee" field, we assert it is not empty
    """
    err = [PayeeError(ent.meta, 'missing payee', ent)
           for ent in entries
           # Beancount auto-generates Transactions for Pad statements (WHYYY)
           if hasattr(ent, 'payee') and ent.flag != 'P' and not ent.payee]
    return entries, err
