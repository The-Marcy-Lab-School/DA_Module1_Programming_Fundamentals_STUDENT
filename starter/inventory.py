"""
Command-line inventory tracker for a small lending library.

Reads a batch file of ADD/REMOVE/SEARCH transaction lines, updates a running
collection of Item objects, and prints a formatted summary plus a low-stock
alert list at the end.

See ../MVP.md for the required scope, ../ABOVE_AND_BEYOND.md for stretch
goals, and REFLECTION.md (same folder as this file) for the written
reflection your finished script needs to support.
"""

LOW_STOCK_THRESHOLD = 5  # an item with fewer than this many units on hand counts as low stock


class Item:
    """One inventory item: a name, a quantity on hand, and a category."""

    def __init__(self, name, quantity, category):
        # TODO: store name, quantity, and category as instance attributes
        pass

    def is_low_stock(self):
        """Return True if this item's quantity is below LOW_STOCK_THRESHOLD."""
        # TODO: implement this
        pass


def read_batch_file(filepath):
    """
    Read the batch file at `filepath` and return a list of raw transaction
    lines (strings). Keep this function focused on *reading* -- deciding
    whether a line is usable happens in validate_line(), not here.
    """
    # TODO: open the file, read it line by line, return the lines
    pass


def validate_line(line):
    """
    Given one raw line from the batch file, decide whether it's a usable
    transaction. Return a parsed representation (your choice of shape -- a
    tuple, a dict, whatever fits) if it's valid, or a value you can check
    for (e.g. None) if it isn't.

    A valid ADD line needs a name, a quantity that's actually a whole
    number, and a category. A valid REMOVE needs a name and a quantity. A
    valid SEARCH needs just a name. A blank line is never a valid
    transaction.
    """
    # TODO: implement this
    pass


def process_transactions(lines):
    """
    Given the raw lines from read_batch_file(), validate each one and apply
    the valid ones to a running collection of Item objects: ADD creates a
    new Item or restocks an existing one, REMOVE decreases an existing
    Item's quantity, SEARCH looks one up by name. Return whatever collection
    type you choose to hold the items in -- see REFLECTION.md for how that
    choice affects search speed.

    A malformed line (per validate_line) should be skipped with a specific,
    printed message naming what was wrong with it -- never let one bad line
    crash the whole run. Same for a REMOVE naming an item that was never
    added: report it, don't crash.
    """
    # TODO: implement this
    pass


def find_item(items, name):
    """
    Look up one Item by name in whatever collection process_transactions()
    built. This is the function your REFLECTION.md Big-O comparison needs
    to be about -- implement ONE approach for real (a linear scan through a
    list, or a dict keyed by name) and reason about its actual complexity.
    """
    # TODO: implement this
    pass


def print_summary(items):
    """
    Print a formatted inventory summary -- every item, its quantity, and
    its category -- followed by a separate low-stock alert list containing
    only the items where is_low_stock() is True.
    """
    # TODO: implement this
    pass


if __name__ == "__main__":
    lines = read_batch_file("data/inventory_transactions.txt")
    items = process_transactions(lines)
    print_summary(items)
