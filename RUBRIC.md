# Rubric: Inventory Tracker

**Point scale:** Below Expectations = 1, Approaching = 2, Meets = 4,
Exceeds = 5 (extra credit; most Exceeds levels require Above & Beyond
work). 5 skills × 4 points = **20 points at Meets**.

Your instructor grades your script, `REFLECTION.md`, your own `README.md`,
and your commit history together. Exceeds levels point to the Above &
Beyond section at the bottom of `CHECKLIST_TIMELINE.md`. The Day 5
share-out is practice and isn't graded.

There's no single correct class. You're graded on whether your attributes
fit **your** stakeholder's need and whether you use the class
consistently.

Delete this file before your final push. It stays in the LMS.

---

## Technical Skills

### `control-flow-loops`

*Using loops and conditionals that branch on real conditions in the data,
not just the happy path.*

| Level | Points | Criteria |
|---|---|---|
| **Exceeds** | 5 | Meets, plus handles a **4th** type of edge case beyond the 3 the MVP requires (Above & Beyond). |
| **Meets** | 4 | The loop correctly applies `ADD`, `REMOVE`, and `SEARCH` lines from the student's 430-line data file, **and** handles **at least 3 different types** of edge case from `data/SOURCE.md` without crashing. Each one either skips the line with a specific printed reason or fixes it on purpose. Three lines of the same type count as one. |
| **Approaching** | 2 | Works on well-formed lines but crashes or gives wrong results on 1-2 of the required edge cases, or fewer than 3 different types are handled. |
| **Below Expectations** | 1 | The script crashes on the full data file, or only the happy path was tested. |

### `functions-modular-programming`

*Breaking a script into small, single-purpose functions with clear
parameters and return values.*

| Level | Points | Criteria |
|---|---|---|
| **Exceeds** | 5 | Meets, plus the function-scope explanation in `REFLECTION.md` connects to something concrete from the student's own debugging, not just the definition. |
| **Meets** | 4 | (1) At least 2 standalone functions (not methods) with clear parameters and an explicit `return`; `print_summary` is the only exception. (2) **Every function and method has a docstring the student wrote**; the one given example doesn't count. (3) `REFLECTION.md` explains, in the student's own words, why a local variable doesn't leak out of its function. |
| **Approaching** | 2 | Functions exist but mix jobs (e.g. one function reads the file *and* prints the summary), some docstrings are missing or templated, or the scope explanation is vague or wrong. |
| **Below Expectations** | 1 | All logic in one long block with no real functions, docstrings mostly missing, or the scope explanation is missing or copied. |

### `object-oriented-programming`

*Bundling related data and behavior into a class, and deciding what
belongs on that class for a real need.*

| Level | Points | Criteria |
|---|---|---|
| **Exceeds** | 5 | Meets, plus the class has additional behavior clearly motivated by the stakeholder's stated need, not just extra attributes. |
| **Meets** | 4 | The attributes are a reasonable answer to *this* stakeholder's need, and the README's "Key decisions" section explains why. `__init__` stores them; `is_low_stock` works and uses a stated assumption (`REFLECTION.md`, "Assumptions"); multiple instances hold independent values; the class is used throughout, with no parallel lists or dicts holding the same data. |
| **Approaching** | 2 | The class is mostly used, but the attributes don't clearly connect to the stakeholder's need (e.g. bookstore-style fields in a healthcare scenario), the low-stock rule has no stated assumption, or some item data is kept in a parallel structure. |
| **Below Expectations** | 1 | Item data lives in loose lists or dicts instead of a class, or the core methods are missing or wrong. |

### `algorithmic-complexity-big-o`

*Reasoning about how runtime changes as the input grows.*

| Level | Points | Criteria |
|---|---|---|
| **Exceeds** | 5 | Implemented **both** a linear scan and a dict lookup and timed them on a larger inventory, with real numbers in `REFLECTION.md` (Above & Beyond). |
| **Meets** | 4 | `REFLECTION.md` correctly labels the student's own `find_item` as O(n) (linear scan) or O(1) average (dict lookup) and explains, using their own code, why it matters as the inventory grows. |
| **Approaching** | 2 | The label is wrong for what the code does, or the explanation is a textbook definition not tied to their own `find_item`. |
| **Below Expectations** | 1 | No real Big-O reasoning, or it has nothing to do with the actual search code. |

---

## Professional Skills

### `attention-to-detail`

*Catching subtle mistakes, checking your own work before calling it done,
and using AI to find more problems without trusting it blindly.*

| Level | Points | Criteria |
|---|---|---|
| **Exceeds** | 5 | Completed the `debug_challenge.py` exercise: found and named all 3 bugs at the exact line, fixed them, and confirmed the corrected output (Above & Beyond). |
| **Meets** | 4 | All 3: (1) no leftover debug `print()`s, `TODO`s, or unused variables, school-facing files removed, and `starter/` renamed to `analysis/`; (2) `REFLECTION.md` lists 3 different edge cases with the exact line and what the code does, and the README's "Findings" section reports what the real run printed (e.g. how many lines were skipped and why); (3) the "AI-assisted edge-case discovery" section names a specific prompt **and** a specific check the student would run before trusting the suggestions. "Ask AI for edge cases" with no check doesn't meet this bar. |
| **Approaching** | 2 | 1-2 of the 3 criteria are met. For example, edge cases are handled but the README's findings don't show it, or the AI section names a prompt but no check. |
| **Below Expectations** | 1 | Leftover debug code, fewer than 3 different edge cases, or generic AI answers ("AI would help me find bugs"). |

## Reflection AI line (formative)

*Did you ask the AI well, and check what it gave you?* This covers
`REFLECTION.md`'s "One real AI prompt, checked" section. It's scored and
you get feedback on it, but it doesn't count toward the five skill scores
above. Didn't use AI? You can still earn Meets: write the prompt you would
have used, label it "not sent," and run the same check on your own code.

| Level | Points | Criteria |
|---|---|---|
| **Exceeds** | 5 | Meets, plus you show a second version of the prompt and say what you changed and why (compare and optimize). Or your check caught a real flaw in the AI's answer, and you explain what you fixed. |
| **Meets** | 4 | One real prompt from your sprint, pasted word for word. You name at least one technique it uses and point to where it appears in the prompt. You show what came back, trimmed but not reworded. You checked it one concrete way: a case you worked by hand, a test you wrote, or re-running on your data file. You say what the check showed. |
| **Approaching** | 2 | The prompt is pasted, but the technique is named without pointing to where it shows up. Or the check is vague, such as "it looked right" or "it ran." Or the prompt was clearly rewritten after the fact. |
| **Below Expectations** | 1 | No prompt. Or a prompt with no output and no check. Or the AI's answer is accepted with no verification at all. |

## Common mistakes that cost points

1. One long function that reads, validates, and prints, instead of
   separate functions.
2. One bad line crashes the whole script.
3. Item data kept in separate lists instead of your class.
4. Only testing lines that work. Run the full file.
5. Copying another scenario's attributes, such as a healthcare inventory
   that tracks "genre."
6. Claiming edge cases in `REFLECTION.md` that your README's findings and
   real output don't back up.
