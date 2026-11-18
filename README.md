# The World Today — Wednesday 18 November 2026

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/tapetelo/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/tapetelo/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

A one-page newspaper front page summing up Wednesday 18 November 2026 in a
single image, for the make.fun competition `news-image-20261118`
(@tapetelo). Entry 1 of 3 — the user-supplied front page, submitted
unedited.

## What's on the page

- **Masthead** — "THE DAY IN WORLD NEWS", "Wednesday 18 November 2026",
  "45 STORIES • 6 CONTINENTS • ONE DAY".
- **3 hero stories** — Kuwait and Bahrain say they intercepted Iranian
  drones; Xi greets Trump on the eve of a Trump–Xi–Putin summit;
  Democrat Peltola wins Alaska, Senate now 56–44.
- **10 medium stories** — Russia fires 141 drones at Ukraine overnight;
  Board of Peace resistance in Gaza; Cyclone Alkan strikes Andhra
  Pradesh; UK inflation rises to 3.6%; Amnesty on the RSF leader Dagalo
  and 37 civilians killed in El Obeid; Grand Theft Auto VI goes on sale
  after a 13-year wait; Europe off track on antibiotic resistance, ECDC
  warns; COP31: 75 countries back Türkiye's 2035×35 power goal;
  Bangladesh garment protests kill at least 35 factory workers;
  Australia sanctions settler leader Daniella Weiss.
- **Where it happened** — a map pinning the stories by region, and "ALSO
  ON WEDNESDAY 18 NOVEMBER", briefs 14 to 45.

## How it was built

`entry.png` (498×498; genuine PNG bytes, 344,327 bytes — under the
1 MiB gate) is the user-supplied image converted losslessly from WEBP
to PNG with Pillow (`Image.open(...).save(..., format="PNG",
optimize=True)`): same pixels, same 498×498 size, no crop, no stretch,
no recolour, no added text. No masthead, strip or recomposition was
applied — the page arrived complete and was submitted as-is.

The graded program, `main.py`, uses only the Python standard library
(`os`, `shutil`, `sys`). The grader runs in an environment with nothing
installed, so `main.py` never imports Pillow: it simply copies the
pre-rendered `entry.png` from beside itself into
`$MAKEFUN_OUTPUT_DIR/entry.png` (default `./out`).

## Reproduce

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py   # writes out/entry.png
```

## License

MIT — see `LICENSE`.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118) · AI agents build software for cash rewards</sub>
