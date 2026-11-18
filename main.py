#!/usr/bin/env python3
"""Entry 1 for news-image-20261118: hand over the finished front page.

The picture is the user-supplied front page for Wednesday
18 November 2026, submitted exactly as supplied — no masthead,
strip, text, crop, stretch, recolour or recomposition was applied.
The only handling was a lossless format change of the same pixels
from WEBP to PNG (see README.md), because the kit tells PNG and
JPEG apart by their first bytes and the source arrived as WEBP.
It is baked into entry.png next to this file at 498x498.

The grader's sandbox installs nothing, so this program uses only
the standard library and does one job: place that finished picture
where the grader looks for it.

Note on the file: entry.png carries genuine PNG bytes this time
(the 17 November V3 entry carried JPEG bytes under the same name,
because its PNG ran over the 1 MiB gate; this page's PNG is
344,327 bytes, comfortably under the gate).
"""
import hashlib
import os
import shutil
import sys

BUNDLED = "entry.png"


def bundled_path():
    """Where the bundled picture lives, beside this program."""
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, BUNDLED)


def fingerprint(path):
    """SHA-256 of a file's bytes, read in chunks."""
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def deliver():
    """Copy the bundled picture into the grader's output folder."""
    origin = bundled_path()
    if not os.path.isfile(origin):
        print(f"{BUNDLED} is missing beside {__file__}", file=sys.stderr)
        return 1
    destination_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "./out"
    os.makedirs(destination_dir, exist_ok=True)
    destination = os.path.join(destination_dir, BUNDLED)
    shutil.copyfile(origin, destination)
    # Guard against a short or altered copy: the grader runs this
    # program twice and both runs must write identical bytes, so
    # check the delivered file is exactly the bundled picture —
    # same size and same SHA-256 — before reporting success.
    if os.path.getsize(destination) != os.path.getsize(origin):
        print(f"{destination} is not a complete copy of {origin}",
              file=sys.stderr)
        return 1
    if fingerprint(destination) != fingerprint(origin):
        print(f"{destination} does not match {origin}",
              file=sys.stderr)
        return 1
    print(f"wrote {destination} ({os.path.getsize(destination)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(deliver())
