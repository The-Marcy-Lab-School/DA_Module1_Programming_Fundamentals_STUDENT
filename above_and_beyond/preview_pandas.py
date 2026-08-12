"""
Above & Beyond: Preview of Module 2 -- code given, you don't need to write
this yourself.

Module 2 introduces pandas for real exploratory data analysis. Here's a
small, real taste of what the SAME transaction data looks like through
pandas instead of the plain functions/loops you just wrote by hand. Run it
(`python3 preview_pandas.py` from the repo root -- you'll need pandas
installed: `pip install pandas`), then in REFLECTION.md write 1-2 sentences
comparing this to your own inventory summary: does it agree? What did
pandas get "for free" that you had to write a loop for yourself?
"""
import pandas as pd

ROWS = []
with open("data/inventory_transactions.txt") as f:
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
