# THE WORLD TODAY — Tuesday, 24 November 2026

Newspaper front page summing up the world news of **Tuesday, 24 November 2026**,
drawn from scratch with Python PIL (`draw.py`, deterministic, no network).
Entry for make.fun competition `news-image-20261124` ($100 shared by the top 50).

## The day's news (all first reported 24 November 2026)

1. **GAZA — Hamas security chief killed** (Reuters): Israeli airstrike kills
   Naeem Abu Nahel, director of Hamas' internal security apparatus, plus six
   others including two police officers, in western Gaza City.
2. **UKRAINE — Zaporizhzhia hit overnight** (Governor Semikin): Russian attack
   kills 2, wounds about 40 including four children, hitting an apartment
   building in Zaporizhzhia.
3. **BUSINESS — Sanofi buys Insmed for $41bn** (Sanofi, Paris): Sanofi agrees
   to buy US biotech Insmed for $41 billion cash ($175/share) — the biggest
   biopharma deal of 2026.
4. **DEFENCE — Germany gets Ukraine's DELTA** (Ukraine Defence Ministry):
   Germany becomes the first foreign country to gain access to Ukraine's DELTA
   battlefield management system; letter of intent signed in Berlin.
5. **CONGO — Ebola teams evacuated** (WHO chief Tedros): WHO staff and Ebola
   responders safely evacuated from Akwe hospital in Ituri after sheltering
   3+ days amid fighting.

In brief: **Iraq** — PM orders the oil ministry to manage oilfields in
Kurdish-controlled areas. **Korea** — Russian warplanes enter South Korea's
air defence zone near Ulleungdo; Seoul scrambles F-15Ks. **UN** — 47,000 women
killed by partners or family in 2025, five every hour (UNODC + UN Women).
**Space** — Euclid finds the most distant quasar J1504+6252 "Dún Aonghasa",
630 million years after the Big Bang (ESA).

## How it runs

`main.ts` (Node 22, standard library only) copies the committed `entry.png`
to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`):

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

To re-draw the image from scratch: `python3 draw.py` (needs Pillow and the
DejaVu fonts in `/usr/share/fonts/truetype/dejavu/`).

## Verification

- `entry.png` is 1024×1024 and under 1 MiB.
- Byte-identical across a direct `draw.py` render, two consecutive
  `node main.ts` runs, and the fallback copy path (see hashes in the build
  report; verified with `sha256sum` / `cmp` before committing).

## License

MIT — see LICENSE.
