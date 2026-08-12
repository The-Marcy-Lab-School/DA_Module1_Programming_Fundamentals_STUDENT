# MVP — Minimum Bar

Full grading detail (what separates each level) lives in `rubric.md`. This
is the bar:

- [ ] **Scenario chosen** (`SCENARIOS.md`), the other 3 data files deleted.
- [ ] **Your own class** — attributes that genuinely fit your stakeholder's
  need, used consistently (no parallel dicts/lists holding the same data).
- [ ] **At least 2 standalone functions**, not methods, with real parameters
  and an explicit `return` (`print_summary` is the one exception).
- [ ] **Batch processing** — a loop + conditional handles ADD/REMOVE/SEARCH
  lines from your data file.
- [ ] **At least 3 distinct edge cases** handled without crashing, each with
  a specific printed message.
- [ ] **At least one real `try`/`except`** for a value that's present but
  the wrong type.
- [ ] **`find_item` implemented** — a linear scan or a dict lookup.
- [ ] **`print_summary` implemented** — a formatted summary plus a separate
  low-stock alert list.
- [ ] **`export_to_json` implemented and called** — writes `inventory.json`,
  used with `tools/search.html` to confirm your edge cases.
- [ ] **Real docstrings you wrote yourself** on every function and method.
- [ ] **`REFLECTION.md` complete** — edge cases, function scope, Big-O
  comparison, AI-assisted edge-case discovery.
- [ ] **A project deck** — 6 slides max, including a live demo of your 3+
  edge cases actually being handled.
- [ ] **Clean submission** — no leftover debug `print()`s or unused code.
- [ ] **GitHub repo** — public, at least 3 real, well-messaged commits.

See `CHECKLIST_TIMELINE.md` for the day-by-day sequence this bar is built in.
