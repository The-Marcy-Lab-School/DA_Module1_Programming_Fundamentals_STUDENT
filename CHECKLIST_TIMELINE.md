# Checklist & Timeline: 5-Day Sprint

**4 build days, then a share-out day.** Work through the items in order.
Each one is also part of the submission checklist.

## How the sprint works

A sprint is a short, fixed block of time. A team commits to a set of work,
builds it, then stops and shows what they built. Professional software
teams plan their work this way. This project is your first sprint.

- **Sprint planning (Day 1):** understand the goal before you write code.
  The scope is already set (the MVP checklist in the LMS). Your job is to
  understand it.
- **Daily check-in:** at the start of each build day, answer three
  questions in 2 minutes. What did I finish yesterday? What am I doing
  today? Is anything blocking me?
- **Backlog:** useful work that is deliberately left out of this sprint.
  The Above & Beyond section at the bottom of this file is your backlog.
- **Sprint review (Day 5):** you show working code to your classmates. It
  isn't a status update.

## Day 1: Plan and build your class

- [ ] Create your repo from the template with **"Use this template"** (not
  Fork) and clone it. See `README.md`.
- [ ] Confirm `.gitignore`, `LICENSE`, and the git history are there.
  Replace `[YOUR NAME]` in `LICENSE` with your name and commit.
- [ ] Check Python works: `python3 --version`.
- [ ] Read all 4 scenarios in `SCENARIOS.md`. Pick one and delete the
  other 3 data files.
- [ ] Read `starter/REFLECTION.md` so you know what you'll need to explain
  at the end.
- [ ] Write your QAR assumptions in the "Assumptions" section of
  `REFLECTION.md`. Include at least what counts as "low stock."
- [ ] Sketch your class's attributes on paper or in a scratch file, based
  on your stakeholder's words.
  - Common mistake: choosing attributes that don't answer your
    stakeholder's question, or copying them from another scenario.
- [ ] Trace the first 3 lines of your data file by hand. What makes an
  `ADD` line valid or invalid?
- [ ] Write `__init__` to store your attributes, and an `is_low_stock`
  method that uses your assumption.
- [ ] Create 2 objects and change one. Confirm the other one didn't
  change.
- [ ] Write a docstring for the class and each method in your own words.
- [ ] Commit: `git commit -m "add [scenario] item class"`.

## Day 2: Read and validate lines

- [ ] `read_batch_file` reads your data file and returns a list of lines.
- [ ] `validate_line` tells a valid `ADD`, `REMOVE`, or `SEARCH` line from
  an invalid one. Test it on 3 to 5 lines you copy from the data file
  before running the whole file.
- [ ] Use at least one `try`/`except ValueError` for a quantity that isn't
  a number.
- [ ] Write a docstring for each function in your own words.
  - Common mistake: writing one long function that reads, validates, and
    prints. Keep each function to one job.
- [ ] Commit: `git commit -m "add batch file parsing and validation"`.

## Day 3: Process the real file and handle edge cases

- [ ] `process_transactions` loops over every line in your data file and
  updates a collection of your objects. `ADD` creates or restocks an item,
  `REMOVE` lowers its quantity, and `SEARCH` looks one up.
- [ ] `find_item` finds an item by name with either a linear scan or a
  dict lookup. Pick one.
- [ ] Handle at least **3 different types** of edge case from
  `data/SOURCE.md`. Each one either skips the line with a specific printed
  reason or fixes it on purpose. The script must not crash.
  - Common mistake: letting one bad line crash the whole script. Run the
    full file, not just the lines that work.
  - Common mistake: keeping item data in separate lists instead of using
    your class.
- [ ] Commit: `git commit -m "process real batch file, handle edge cases"`.
- [ ] Push. By the end of Day 3 you should have at least 3 commits on
  GitHub.

## Day 4: Finish, reflect, write your README

- [ ] `print_summary` prints every item and then a separate low-stock
  list.
- [ ] `export_to_json` writes `inventory.json`, and your script calls it.
- [ ] Optional: check your results with `tools/search.html`. This is a
  small web page (given code) that reads your `inventory.json` and filters
  your items as you type. To open it, run `python3 -m http.server` in your
  repo's top folder, then go to `http://localhost:8000/tools/search.html`
  in your browser. Press `Control+C` in Terminal to stop the server.
- [ ] Fill in every section of `REFLECTION.md`: assumptions, edge cases,
  function scope, Big-O, AI-assisted edge-case discovery, and one real AI
  prompt, checked.
  - Common mistake: a Big-O answer copied from a textbook that doesn't
    mention your own `find_item`.
  - Common mistake: an AI answer with no specific way to check what the AI
    suggests.
- [ ] Clean up: no leftover `TODO` comments, placeholder docstrings, debug
  `print()` lines, or unused variables.
- [ ] Replace the text of `README.md` with your own project README. Write
  it for an employer who has never seen this assignment and will skim it
  in under a minute:
  - **Title and one-line summary:** what you built and for whom.
  - **Business scenario:** your stakeholder, their problem, and why it
    matters to them.
  - **What it does:** what the script does with the transaction file.
  - **Findings:** what your run showed. For example, how many lines were
    skipped and why, and which items are low on stock. Use your real
    output.
  - **Key decisions:** your class attributes and why, your main
    assumption, and your search approach with its Big-O.
  - **How to run it:** the exact command.
  - **Reflection:** 2 or 3 bullets on what you learned and what you'd
    improve next. Link to `starter/REFLECTION.md` for the full version.
- [ ] Delete `CHECKLIST_TIMELINE.md` (this file), `RUBRIC.md`,
  `SCENARIOS.md`, and `PROJECT_OVERVIEW.md`. They describe the assignment,
  not your project, and don't belong in a portfolio repo. The checklist
  and rubric stay available in the LMS.
- [ ] Final push. Open your repo in a private browser window to confirm
  it's public.

## Day 5: Share-out

No slides. You'll do two things in class, in TIP style:

- **Pair repo review.** You and a partner review each other's repo and
  code against a checklist your instructor hands out, then trade one
  strength and one fix.
- **90-second project walkthrough.** Answer "Walk me through your
  project" using PREP (Point, Reason, Example, Point). Your instructor
  times it and stops you at 110 seconds. Classmates score each part of
  PREP and give feedback, then you try again.

To prepare:

- [ ] Your README is finished. Its summary, business scenario, and key
  decisions are your talking points.
- [ ] Practice your walkthrough out loud once with a timer. Aim for 90
  seconds.
- [ ] After the share-out, push any fixes your partner found.

## Above & Beyond (optional)

These go beyond what was taught in class, on purpose. You'll need to
research them yourself. Each one has a starting link. A complete MVP
without any of these is still a full, passing submission. Pick one or two
if you have time.

**Use AI to learn, not to do it for you.** Ask it to explain a concept,
give you a small example on different data, or review code you wrote.
Don't paste in the task and copy the answer. In `REFLECTION.md`, add a
short note on what you looked up and what you learned.

**Some items use given code that isn't in your repo.** It lives in the
`above_and_beyond/` folder on the `project-scope` branch of the original
template repo. Go to the template on GitHub, switch to that branch, and
copy the file you need.

- [ ] **Prove your Big-O answer with timing.** Write a second `find_item`
  that uses the other approach (dict if you used a list, or the reverse).
  Build a much bigger inventory, time both versions, and report the real
  numbers in `REFLECTION.md`. You practiced the pieces in the Lookups
  Matter and Stress-Test labs.
  Start here: [Python docs: `time.perf_counter`](https://docs.python.org/3/library/time.html#time.perf_counter)
  and [Python tutorial: dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries).
- [ ] **Debug `above_and_beyond/debug_challenge.py`.** It's a short
  grade-tracking script with 3 bugs and no hints. Find each bug, name the
  exact line and what's wrong, fix it, and write it up in
  `REFLECTION.md`.
  Start here: [Python Tutor](https://pythontutor.com/) (step through
  the code line by line) and [Python tutorial: errors and exceptions](https://docs.python.org/3/tutorial/errors.html).
- [ ] **Handle a 4th type of edge case** from `data/SOURCE.md`, beyond
  the 3 the MVP requires.
- [ ] **Extend `tools/search.html`.** This means learning some JavaScript.
  Add sorting, a filter by one of your attributes, or a count of low-stock
  items at the top. Note what you changed in `REFLECTION.md`.
  Start here: [MDN: JavaScript first steps](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting)
  and [MDN: `Array.prototype.sort()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort).
- [ ] **Preview Module 2 with pandas.** Copy
  `above_and_beyond/preview_pandas.py` into your repo's top folder and run
  `python3 preview_pandas.py` (install pandas first with
  `pip install pandas`). In `REFLECTION.md`, write 1-2 sentences comparing
  its output to your own summary. What did pandas do with the bad lines
  that your code handled differently?
  Start here: [pandas: 10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html).
