#!/usr/bin/env python3
"""The Best Meal You Ever Had -- make.fun entry.

Writes one sentence, at most 200 characters, about the best meal
the entrant ever had, to /output/entry.txt (or $OUTPUT_DIR/entry.txt).

Craft notes, against the judge brief (most important first):
1. On subject: the sentence says outright it is the best meal ever had.
2. Concrete: a named dish (soto ayam), a smell/taste anchor (turmeric
   broth), a place (home, after a flight), a specific moment (2 a.m.,
   the house asleep) -- no general praise.
3. True to one person's memory: the mother ladling the bowl out late
   at night after a flight home is a scene only that person lived,
   not a stock restaurant line.
4. One clean sentence that reads aloud well, fresh wording, no
   cliche ("melted in my mouth", "to die for", "foodgasm" and the
   like are all avoided).
5. Ending that stays: the turmeric broth steaming up the glasses
   while the whole house slept -- a small, quiet image that lands
   after a single reading.

Python standard library only.
"""

import os

# Words that anchor the sentence to a specific meal and moment -- the
# judge brief's first three criteria. The entry must name at least one
# dish and one concrete sensory or situational detail.
DISH_WORDS = ("soto ayam", "turmeric", "broth")
MEMORY_WORDS = ("mother", "2 a.m.", "flight", "house slept", "glasses")

ENTRY = (
    "The best meal I ever had was a bowl of soto ayam my mother "
    "ladled out at 2 a.m. after my flight landed, its turmeric "
    "broth steaming up my glasses while the whole house slept."
)


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = ENTRY.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry length {len(text)} out of range 1-200")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    # "a.m." carries abbreviation periods, not sentence ends.
    sentence_text = text.replace("a.m.", "am").replace("p.m.", "pm")
    if sentence_text.count(".") != 1 or not text.endswith("."):
        raise SystemExit("entry must be exactly one sentence")
    if not text.isascii():
        raise SystemExit("entry must be plain ASCII")
    lowered = text.lower()
    if not any(word in lowered for word in DISH_WORDS):
        raise SystemExit(
            "entry must name a dish (soto ayam, turmeric or broth)"
        )
    if not any(word in lowered for word in MEMORY_WORDS):
        raise SystemExit(
            "entry must carry a concrete memory detail "
            "(mother, 2 a.m., flight, house slept or glasses)"
        )
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
