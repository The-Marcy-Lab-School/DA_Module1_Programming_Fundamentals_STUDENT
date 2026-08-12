"""
Command-line inventory tracker -- you choose the scenario.

See ../SCENARIOS.md to pick your stakeholder and dataset. Design your own
class for tracking one inventory item, appropriate to what *your*
stakeholder actually needs -- there's no single right set of attributes
here, and that's on purpose. See ../MVP.md for the full required scope.
"""
import json


# TODO: define a class representing one inventory item for your chosen
# scenario. Re-read your stakeholder's actual words in SCENARIOS.md --
# what would you genuinely need to track to answer their real questions?
# At minimum you'll need a name and a quantity, but don't stop there just
# because that's the minimum -- design for what your specific stakeholder
# actually asked about.
#
# class YourClassName:
#     def __init__(self, ...):
#         # TODO: write a real docstring for every method you add below --
#         # see read_batch_file()'s docstring further down for the level
#         # of detail expected. This comment block is scaffolding, not a
#         # docstring itself -- delete it once your class is written.
#         pass
#
#     def is_low_stock(self):
#         # TODO
#         pass


def read_batch_file(filepath):
    """
    Read the batch file at `filepath` and return a list of its raw lines
    (strings), unmodified -- deciding whether a line is usable happens in
    validate_line(), not here. This docstring is your model for the ones
    you write below: what the function does, what it takes, what it
    returns.
    """
    # TODO: implement
    pass


def validate_line(line):
    """
    # TODO: write your own docstring: what makes a line valid for each of
    # ADD/REMOVE/SEARCH? What do you return for a valid line vs. an
    # invalid one?
    """
    # TODO: implement. One real design choice worth making deliberately:
    # a value can be *present* but the wrong *type* -- a quantity field
    # that isn't actually a number, for instance. A try/except around the
    # conversion (attempt int(quantity_str), catch ValueError if it
    # fails) is usually the cleaner way to handle that than checking
    # .isdigit() beforehand -- you're asking Python "did this work?"
    # instead of trying to predict every way it could fail in advance.
    pass


def process_transactions(lines):
    """
    # TODO: write your own docstring.
    """
    # TODO: implement. Return the collection you built -- don't print
    # from inside this function, that's print_summary's job, not this
    # one's.
    pass


def find_item(items, name):
    """
    # TODO: write your own docstring.
    """
    # TODO: implement
    pass


def export_to_json(items, filepath="inventory.json"):
    """
    # TODO: write your own docstring. This file is what tools/search.html
    # reads to power the interactive search tool (see MVP.md) -- you'll
    # need to turn each of your objects into something JSON can
    # represent (a dict) before json.dump can write it out.
    """
    # TODO: implement
    pass


def print_summary(items):
    """
    # TODO: write your own docstring.
    """
    # TODO: implement. This one really is just for printing to the
    # screen -- no meaningful return value needed here.
    pass


if __name__ == "__main__":
    # TODO: point this at whichever scenario's data file you chose
    lines = read_batch_file("data/____________.txt")
    items = process_transactions(lines)
    print_summary(items)
    export_to_json(items)
