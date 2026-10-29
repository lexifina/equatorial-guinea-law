# How this repository was made (Equatorial Guinea)

This file is written by the build on 2026-10-29, the day the source data was retrieved. Everything below is enough to rebuild this repository hash for hash.

## Sources

| Source | Address | Retrieved | Requests | Licence |
| --- | --- | --- | ---: | --- |
| Boletín Oficial del Estado de Guinea Ecuatorial (boe.gob.gq) | <https://boe.gob.gq> | 2026-10-29 | 3 | Official text. The BOE states no licence. |

Every response is cached by the sha256 of its URL, and the table above lists every source with its retrieval date. Lexifina keeps its fetch scripts privately; `tools/parse.py` reads only the cache and writes `corpus.json`, so the same cache always gives the same corpus.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `ley-fundamental` | Ley Fundamental de Guinea Ecuatorial | 1 | 2012-02-16 to 2012-02-16 |

The build made 1 commits:

| Commits | Kind |
| ---: | --- |
| 1 | first version of an act |
| 0 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `futuro`: laws not yet in force on 2026-10-29.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 1 laws in the record.
- 2 tags.

## Dates

Each commit is dated at noon (Africa/Malabo) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Not applied as a general rule. Ley 1/2012, Disposición final: "La presente Ley Fundamental entrará en vigor a partir de su promulgación por el Presidente de la República, después de haber sido aprobada en Referéndum y su publicación en el Boletín Oficial del Estado"; it was promulgated in Bata on 16 February 2012, the date under which the BOE lists it. Its BOE publication date is not given by the source. https://boe.gob.gq/sites/default/files/2026-10/LEY%20FUNDAMENTAL_0.pdf

## Commands, in order

```sh
# fill the cache from the sources listed above (network; Lexifina's fetch scripts are kept privately)
python -X utf8 tools/parse.py                  # cache -> corpus.json (no network)
python -X utf8 tools/build.py <folder> --repo <empty folder> --docs-date 2026-10-29
python -X utf8 tools/check_repo.py <repo> --corpus <folder>/corpus.json --write
python -X utf8 tools/build.py <folder> --repo <another empty folder> --docs-date 2026-10-29 --compare <repo>
```

In the main Lexifina repository these files live as follows:
- `fetch.py`, `parse.py` and `repo/`: in `scripts/equatorial-guinea-law/`.
- `build.py`, `check_repo.py` (`check.py` there) and `on.py`: in `scripts/gitlaw_common/`, with the corpus format in `SCHEMA.md`.

## Exact inputs

- `corpus.json` sha256 `7f91a249711d42bf7d2f9058c0a52414fef35ecd0cda17546475bcb348265c1d` (80887 bytes)
- Script blob hashes (`git hash-object`):

| Script | Blob |
| --- | --- |
| build.py | `42aa8d2a7c12fbca91f57c90d6554960ccca0795` |
| check.py | `cd346c7ff9996d450240e3bab52bcae03b2bc865` |
| on.py | `644a6c0857fbcc72562032b58d57aa113fee0641` |
| fetch.py | `7dff021abb4365d6331bef340707158813f46f71` |
| parse.py | `5562cd6dd20cb85f5d23651b24060f2fb023c063` |

- Tools:
  - Python 3.14.0
  - git version 2.52.0.windows.1
  - curl 8.21.0 (Windows) libcurl/8.21.0 Schannel zlib/1.3.2 WinIDN WinLDAP

## Checks

1 versions of 1 acts read back from git on the day each took effect and on the day before: 0 mismatches. Trailers: 0 commits whose trailers git cannot parse. Health: 0 merge commits on main, 0 commit dates that go backwards, 0 commits dated after the build.

A second build from the same corpus into an empty folder gave identical hashes for all 1 history commits and 2 tags (history tip `8d36af0121129870927e7893a7be36c0436b228b`).

These results are from the check run on the build before this one, from the same corpus.

## Decisions made by hand

- One act, one version: the Ley Fundamental as promulgated by Ley 1/2012 (16 February 2012), credited to Ley 1/2012 as enacted. It replaced the Ley Fundamental of 1991 (reformed in 1995), whose texts were not found online with a text layer (BOE search, Internet Archive CDX of boe.gob.gq); the Common Crawl index did not answer from this machine. So the history before 2012 is missing.
- The version is dated 2012-02-16, the promulgation date (Disposición final: in force on promulgation and BOE publication). The BOE lists the law under that date and gives no separate publication date.
- Not today's text: Ley 1/2025, de 16 de julio, reforms arts. 56.1, 80 and 84.1 and 2. The BOE publishes it only as images (FPDF wrapper, no text layer), and scans are not transcribed (no OCR), so the reform is not applied and its in-force date is not known. The build stays on preview.
- The e-signature line printed on every page ("Documento firmado electrónicamente con código de verificación …"), the title page and the repeated title before the preamble are left out. The introduction (the promulgation formula before the text) and the closing promulgation formula are kept as their own units.
- Paragraphs are rebuilt from the layout: a sentence end followed by a blank line or a short line ends a paragraph; a line without a sentence end runs on, also across a page break; numbered paragraphs ("2.-"), list items ("a)") and articles start new lines.
- Unit layout: one file per article (art-NNN), the preamble, the introduction, each transitional provision, the repealing and final provisions, the closing formula, and one structure file (estructura) naming the article each heading precedes.
- Typesetting is normalised once: NBSP to space, curly apostrophes to straight ones, curly double quotes to « », runs of spaces collapsed. Spelling is kept as printed (for example "DELAS FUERZAS ARMADAS").

## What AI did and did not do

The fetch, parse and check scripts were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above, through code that anyone can rerun.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- Claude Code (Claude Opus 5.5, claude-opus-5-5) wrote fetch.py and parse.py, chose the sources and wrote the decisions. No model wrote, summarised or transformed legal text: parse.py is deterministic code over the cached PDF.
