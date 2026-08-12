# Data Source

Four batch files, one per scenario in `../SCENARIOS.md` — 430 lines each,
real transaction logs for a fictional business, not a public dataset. Item
names are either real public-domain book titles (bookstore — via
[Project Gutenberg](https://www.gutenberg.org/), titles/authors used only
as facts/flavor text, not a text redistribution) or plain, generic
domain-vocabulary items (restaurant/healthcare/athletic — ordinary common
nouns, not sourced from or representing any real company's actual catalog).

**430 rows is deliberate — long enough that you can't just eyeball the
whole file for problems.** You need real code to actually check it.

## What's actually in each file

Realistic ADD/REMOVE/SEARCH transactions against ~25 recurring items, plus
**14 deliberately planted edge cases, scattered throughout** (not
clustered at the end or the beginning) — different problem types, so
different students who each pick a few will likely find different ones.
You're required to actually handle **at least 3** distinct types (see
`MVP.md`) — here's the full list of what's actually in there, so you know
what you're looking for:

1. Blank lines (2 of them).
2. A malformed `ADD` line with a **missing quantity** field.
3. Two malformed `ADD` lines with a **non-numeric quantity** (`five`,
   `N/A` — two different ways this shows up).
4. Two `REMOVE` lines for an item that was **never added** in the first
   place.
5. A `REMOVE` line asking to remove **more than is actually in stock**.
6. A **lowercase command** (`add` instead of `ADD`).
7. A **misspelled command** (`ADDD`).
8. An `ADD` line with **stray whitespace** around the item name.
9. A line with **too many fields** (extra trailing commas/values).
10. A `REMOVE` line **missing its quantity field** entirely.
11. A `SEARCH` line **missing its name field** entirely.

Don't substitute a different file or hand-edit these out — everyone
choosing the same scenario tests against the same file, which keeps
grading consistent, and finding these for real (not being told exactly
where they are) is the actual point.
