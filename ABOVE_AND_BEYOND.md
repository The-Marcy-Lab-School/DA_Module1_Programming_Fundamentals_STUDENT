# Above & Beyond

**This is this project's backlog** (see `CHECKLIST_TIMELINE.md`'s sprint
framing) — real, worth-doing work that's deliberately not part of the
4-day sprint's scope. Finished the MVP with time to spare? Each of these
previews a skill
a later module assumes you already have, or pushes something you already
built further. Pick one or two — don't feel obligated to do all of them.
Files for the given-code ones live in `above_and_beyond/`.

- **Implement both search approaches and actually compare them.** Add a
  second lookup function using the *other* data structure from the one you
  picked for `find_item` (if you used a list, add a dict-keyed version, or
  vice versa), and turn your `REFLECTION.md` Big-O reasoning from "explain"
  into "prove": time both with Python's `time` module against a
  scaled-up copy of your data file (duplicate the ADD lines a few hundred
  times). Report real numbers, not just the theoretical complexity. This
  same profiling instinct — "which approach actually scales" stops being
  hypothetical — comes back for real in **Module 6** (statistical analysis)
  and **Module 9** (ETL/ELT pipelines).

- **Debug `above_and_beyond/debug_challenge.py` — no template this time.**
  A small, given grade-tracking script with 3 real bugs planted in it (an
  off-by-one loop bound, a function that returns the wrong thing because of
  a scope mistake, and a class method referencing an attribute that was
  never set). Run it, find all 3 precisely (name the exact line and what's
  wrong — "the loop seemed off" doesn't count), fix them, and write up what
  you found in `REFLECTION.md`. This is the same meticulous, systematic
  checking a working analyst applies when auditing a query or a model's
  output for a subtle error before it ships — the same `attention-to-detail`
  instinct **Module 14** (machine learning) assumes you already have when
  auditing a model's output for something subtly wrong.

- **Find and handle a 4th edge case** beyond the 3 MVP requires — there are
  more planted in the data file than the minimum asks for (see `data/
  SOURCE.md`), and a real business's data would have ones nobody planted
  on purpose at all.

- **Extend `tools/search.html` yourself.** It's given code, but nothing
  stops you from adding to it for real — sort results, add a filter by one
  of your specific attributes, show a count of low-stock items at the top.
  Note what you changed in `REFLECTION.md`.

- **Preview of Module 2 — code given, you don't need to write this
  yourself.** Run `above_and_beyond/preview_pandas.py` (needs `pip install
  pandas`) — it profiles your same transaction data through pandas
  instead of the loops/functions you wrote by hand. In `REFLECTION.md`,
  write 1-2 sentences comparing it to your own summary: does it agree? What
  did pandas handle differently than your own validation logic when it hit
  a malformed line? Real exploratory data analysis with pandas is what
  **Module 2** is about.

None of these change what counts as "done" per `MVP.md` — they're optional,
and a complete MVP without any of these is still a full, passing submission.
