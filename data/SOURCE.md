# Data Source

`inventory_transactions.txt` is a constructed sample batch file for this
project's fictional lending-library scenario — it's not a public dataset,
it's a script you write to test against. The book titles used as item names
(*Pride and Prejudice*, *Frankenstein*, *Dracula*, *Moby-Dick*, *The Time
Machine*, *Alice's Adventures in Wonderland*, *A Tale of Two Cities*,
*Little Women*) are real, well-known works whose full texts are in the
public domain via [Project Gutenberg](https://www.gutenberg.org/) — used
here only as realistic flavor text (titles/authors as facts, not
copyrightable subject matter on their own), not as a redistribution of any
actual book text. `The Odyssey` and `Sherlock Holmes` also appear, deliberately,
as edge cases (see below) — they aren't meant to succeed.

## Deliberate edge cases in this file

Your script needs to survive a real run against this exact file without
crashing, not just handle these cases in theory:

- A **blank line** between the initial ADD block and the REMOVE/SEARCH block.
- `REMOVE,The Odyssey,1` — a REMOVE for an item that was **never added**.
- `ADD,Sherlock Holmes,,Mystery` — a malformed ADD line with a **missing
  quantity**.

Don't substitute a different batch file — everyone in this cohort tests
against this same one, which keeps grading consistent.
