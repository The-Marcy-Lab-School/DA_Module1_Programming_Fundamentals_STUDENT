# Written Reflection

Four required pieces. Fill each in *after* your script is working, based on
what you actually built — not a generic textbook answer.

## The 3+ edge cases you found and handled

List each one: the exact line from your data file, what was wrong with it,
and what your code actually does about it. (See `data/SOURCE.md` for the
full list of what's planted in the file — you don't need to find all of
them, just at least 3, for real.)

1. _TODO_
2. _TODO_
3. _TODO_

## Function scope

In your own words: why doesn't a variable defined inside one of your
functions leak into or overwrite a same-named variable elsewhere in the
script? What would break if Python worked the other way — every variable
visible everywhere?

_TODO_

## Search complexity: linear scan vs. dict lookup

State which data structure you chose to hold your item collection (a
list, a dict keyed by name, something else) and which approach `find_item`
actually uses to look something up by name. Then:

- Label your actual `find_item` implementation's time complexity — O(n) for
  a linear scan, or O(1) average-case for a dict-keyed lookup.
- Explain, tied to your own code (not a generic textbook example), why that
  complexity matters as the inventory grows — what happens to `find_item`'s
  runtime going from your ~25 recurring items to 10,000?

_TODO_

## AI-assisted edge-case discovery

You were told to find *at least* 3 edge cases — the data file actually has
several more planted in it, and a real batch of transactions from an
actual business would have edge cases nobody planted on purpose at all.

Write 1-2 sentences on: what prompt (or short back-and-forth) would you
actually give an AI assistant to help you think of *more* categories of
malformed/unexpected input than the ones you already found by hand? Then,
just as important: how would you **validate** whatever it suggests before
trusting it — what's your actual check that a suggested edge case is real
and worth handling, versus the AI confidently describing a problem that
doesn't actually apply to your data or your code?

_TODO_
