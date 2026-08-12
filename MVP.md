# MVP — Minimum Bar

This is done when all of the following are true:

- [ ] **Scenario chosen.** One of the 4 options in `SCENARIOS.md` picked,
  the other 3 data files deleted from your repo so it's clear which one
  you're actually using.
- [ ] **Your own class.** A class representing one inventory item, with
  attributes *you* decided actually matter for your stakeholder's real
  need (not copied from another scenario) — used consistently everywhere
  item data is touched, no parallel raw dicts/lists holding the same data
  outside the class.
- [ ] **At least 2 standalone functions**, not methods, each with real
  parameters and an explicit `return` (not a bare `print`) — e.g. reading
  the batch file, validating a line, updating the collection.
  `print_summary` is the one function that's allowed to just print.
- [ ] **Batch processing.** A loop + conditional logic handles ADD/REMOVE/
  SEARCH lines from your chosen scenario's data file, updating a running
  collection of your item objects.
- [ ] **At least 3 distinct edge cases handled without crashing** — real
  ones, actually present in your data file (see `data/SOURCE.md` for the
  full list of what's planted), each with a specific, printed message
  naming what was wrong. Not the same *type* of problem 3 times — 3
  genuinely different kinds.
- [ ] **At least one `try`/`except`** used for real, for validating a value
  that's present but the wrong type (a quantity field that isn't actually
  a number, e.g.) — see `starter/inventory.py`'s note on why this is
  usually cleaner than checking `.isdigit()` first.
- [ ] **`find_item` implemented** — a real search by name, genuinely one of
  a linear scan or a dict lookup (this is the function your `REFLECTION.md`
  Big-O comparison needs to be about).
- [ ] **`print_summary` implemented** — a formatted inventory summary
  (every item, its key details) and a separate low-stock alert list
  containing only the items your low-stock check flags.
- [ ] **`export_to_json` implemented and actually called** — writes
  `inventory.json`, which `tools/search.html` (given code — see that file)
  reads. Use it to interactively confirm your 3+ edge cases actually did
  what you think they did before calling this done.
- [ ] **Real docstrings you wrote yourself** on every function and every
  method — `read_batch_file`'s docstring in the starter file is your only
  model; every other one needs to be genuinely yours, not a copy.
- [ ] **`REFLECTION.md` filled in completely** — the 3+ edge cases you
  found (with the exact line and what your code does about it), the
  function-scope explanation, the Big-O comparison tied to your actual
  `find_item`, and the AI-assisted edge-case-discovery reflection.
- [ ] **A short project deck — 6 slides max, including a live demo.**
  Explain your chosen scenario/stakeholder, your class design decisions
  (what you tracked and why), your batch-processing approach, and
  **demonstrate your 3+ edge cases actually being handled** (a live run,
  or screenshots of the real output). Build it in whatever tool you
  already use (Slides, PowerPoint, Canva) — no specific format required
  beyond the 6-slide cap.
- [ ] **Clean submission.** No leftover `print()` debugging statements, no
  unused variables or imports left in the final version.
- [ ] **GitHub repo.** Public, contains your inventory script,
  `REFLECTION.md`, `inventory.json`, and a `README.md`, with at least
  **3 real, well-messaged commits** — not one "final" dump. (Design, core
  build, and polish are 3 natural commit points — see `TIMELINE.md`.)

That's the whole bar. Design your class and your standalone functions
before writing the batch-file loop — decide what belongs on the object
(its own data, an `is_low_stock`-style check) versus what belongs in a
function (reading the file, validating a line, printing the summary) so
the two don't blur together. Trace through the first 2-3 lines of your
data file by hand before coding the loop, so your validation logic matches
real edge cases instead of only the happy path.
