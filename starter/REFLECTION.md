# Written Reflection

Two required pieces. Fill both in *after* your script is working, based on
what you actually built — not a generic textbook answer.

## Function scope

In your own words: why doesn't a variable defined inside one of your
functions (e.g. a loop counter inside `process_transactions`) leak into or
overwrite a same-named variable elsewhere in the script? What would break if
Python worked the other way — every variable visible everywhere?

_TODO_

## Search complexity: linear scan vs. dict lookup

State which data structure you chose to hold your `Item` collection (a
list, a dict keyed by name, something else) and which approach `find_item`
actually uses to look something up by name. Then:

- Label your actual `find_item` implementation's time complexity — O(n) for
  a linear scan, or O(1) average-case for a dict-keyed lookup.
- Explain, tied to your own code (not a generic textbook example), why that
  complexity matters as the inventory grows — what happens to `find_item`'s
  runtime going from 10 items to 10,000?

_TODO_
