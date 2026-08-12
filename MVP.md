# MVP — Minimum Bar

This is done when all of the following are true:

- [ ] **`Item` class.** `__init__` correctly stores `name`, `quantity`, and
  `category` as instance attributes; `is_low_stock()` correctly compares
  against `LOW_STOCK_THRESHOLD`. Used consistently everywhere an item's
  data is needed — no parallel raw dicts/lists holding the same data
  outside the class.
- [ ] **At least 2 standalone functions**, not methods, each with real
  parameters and an explicit `return` (not a bare `print`) — e.g. reading
  the batch file, validating a line, updating the collection.
- [ ] **Batch processing.** A loop + conditional logic handles ADD/REMOVE/
  SEARCH lines from `data/inventory_transactions.txt`, updating a running
  collection of `Item` objects.
- [ ] **At least one edge case handled without crashing** — a malformed line
  (missing/non-numeric quantity) or a REMOVE for an item that was never
  added — with a specific, printed message naming what was wrong. Both
  actually appear in the provided batch file; your script needs to survive
  a real run against that exact file end to end, not just handle it in
  theory.
- [ ] **Formatted output.** A printed inventory summary (every item, its
  quantity, its category) and a separate low-stock alert list containing
  only the items where `is_low_stock()` is True.
- [ ] **`REFLECTION.md` filled in** — both the function-scope explanation
  and the Big-O comparison, tied to your actual `find_item` implementation.
- [ ] **Clean submission.** No leftover `print()` debugging statements, no
  unused variables or imports left in the final version.
- [ ] **GitHub repo.** Public, contains `inventory.py`, `REFLECTION.md`, and
  a `README.md`, with at least **2 real, well-messaged commits** — not one
  "final" dump.

That's the whole bar. Design the `Item` class and the standalone functions
before writing the batch-file loop — decide what belongs on the object
(its own data, `is_low_stock`) versus what belongs in a function (reading
the file, validating a line, printing the summary) so the two don't blur
together. Trace through the first 2-3 lines of the batch file by hand
before coding the loop, so your validation logic matches real edge cases
instead of only the happy path.
