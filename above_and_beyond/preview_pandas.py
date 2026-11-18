"""
Above & Beyond: Preview of Module 2 -- code given, you don't need to write
this yourself.

Module 2 introduces pandas for real exploratory data analysis. Here's a
small, real taste of what the SAME transaction data looks like through
pandas instead of the plain functions/loops you just wrote by hand. Save
this file in your repo's top folder and run `python3 preview_pandas.py`
there (install pandas first: `pip install pandas`). Then in REFLECTION.md
write 1-2 sentences
comparing this to your own inventory summary: does it agree? What did
pandas get "for free" that you had to write a loop for yourself?
"""
import glob

import pandas as pd

# Finds whichever scenario's data file you kept -- see PROJECT_OVERVIEW.md.
data_files = glob.glob("data/*_transactions.txt")
if len(data_files) != 1:
    raise SystemExit(
        f"Expected exactly one data/*_transactions.txt file, found "
        f"{len(data_files)}: {data_files}. Did you delete the other 3 "
        f"scenarios' data files after choosing yours (see PROJECT_OVERVIEW.md)?"
    )

ROWS = []
with open(data_files[0]) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        parts = line.split(",")
        # normalize every row to 4 fields so pandas has a consistent shape --
        # REMOVE/SEARCH rows don't have a category, so pad with None
        parts += [None] * (4 - len(parts))
        ROWS.append(parts[:4])

df = pd.DataFrame(ROWS, columns=["command", "name", "quantity", "category"])
adds = df[df["command"] == "ADD"].copy()
adds["quantity"] = pd.to_numeric(adds["quantity"], errors="coerce")

print("Total quantity added per category:")
print(adds.groupby("category")["quantity"].sum())
print()
print("Quantity column, five-number summary:")
print(adds["quantity"].describe())
