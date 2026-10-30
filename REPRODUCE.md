# How this repository was made (Equatorial Guinea)

This file is written by the build on 2026-10-30, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Boletín Oficial del Estado de Guinea Ecuatorial (boe.gob.gq) | <https://boe.gob.gq> | 2026-10-29 | Official text. The BOE states no licence. |
| Boletín Oficial del Estado (Dirección General del B.O.E.): Ley Núm. 4/2021, General de Trabajo (printed edition, Malabo, 31 January 2022) | <https://www.observatoire-comifac.net/file/eyJtb2RlbCI6IkFwcFxcTW9kZWxzXFxOYXRpb25hbEluZGljYXRvcnNcXE1vZHVsZXNcXE4yXFxUZXh0ZVJlZ2xlbWVudGFpcmUiLCJmaWVsZCI6ImRvY3VtZW50IiwiaWQiOjEwNjB9> | 2026-10-30 | Official text of the Boletín Oficial del Estado de Guinea Ecuatorial; copy held by the Observatoire des Forêts d'Afrique Centrale (COMIFAC) |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `ley-fundamental` | Ley Fundamental de Guinea Ecuatorial | 1 | 2012-02-16 to 2012-02-16 |
| `ley-general-de-trabajo` | Ley Núm. 4/2021, de fecha 3 de Diciembre, General de Trabajo en la República de Guinea Ecuatorial | 1 | 2022-03-02 to 2022-03-02 |

The build made 2 commits:

| Commits | Kind |
| ---: | --- |
| 2 | first version of an act |
| 0 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `futuro`: laws not yet in force on 2026-10-30.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 2 laws in the record.
- 4 tags.

## Dates

Each commit is dated at noon (Africa/Malabo) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Not applied as a general rule. Ley 1/2012, Disposición final: "La presente Ley Fundamental entrará en vigor a partir de su promulgación por el Presidente de la República, después de haber sido aprobada en Referéndum y su publicación en el Boletín Oficial del Estado"; it was promulgated in Bata on 16 February 2012, the date under which the BOE lists it. Its BOE publication date is not given by the source. https://boe.gob.gq/sites/default/files/2026-10/LEY%20FUNDAMENTAL_0.pdf

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `d39192ed95a371ab376844eae983f92efd796f70c731657f00255a5942efafb5` (238088 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a4faa25af85facb64b956b372f6b528aafdd7ec1`, `check.py` `3d00541d258745461ab52b1b0cb4e1716a27a95d`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

2 versions of 2 acts read back from git on the day each took effect and on the day before: 0 mismatches. Trailers: 0 commits whose trailers git cannot parse. Health: 0 merge commits on main, 0 commit dates that go backwards, 0 commits dated after the build.

A second build from the same corpus into an empty folder gave identical hashes for all 2 history commits and 4 tags (history tip `79b81357f760c7c32e8c6cb7415100fe0e9646e9`).

## Decisions made by hand

- One act, one version: the Ley Fundamental as promulgated by Ley 1/2012 (16 February 2012), credited to Ley 1/2012 as enacted. It replaced the Ley Fundamental of 1991 (reformed in 1995), whose texts were not found online with a text layer. So the history before 2012 is missing.
- The version is dated 2012-02-16, the promulgation date (Disposición final: in force on promulgation and BOE publication). The BOE lists the law under that date and gives no separate publication date.
- Not today's text: Ley 1/2025, de 16 de julio, reforms arts. 56.1, 80 and 84.1 and 2. The BOE publishes it only as images (FPDF wrapper, no text layer), and scans are not transcribed (no OCR), so the reform is not applied and its in-force date is not known. The record ends with the 2012 text.
- The e-signature line printed on every page ("Documento firmado electrónicamente con código de verificación …"), the title page and the repeated title before the preamble are left out. The introduction (the promulgation formula before the text) and the closing promulgation formula are kept as their own units.
- Paragraphs are rebuilt from the layout: a sentence end followed by a blank line or a short line ends a paragraph; a line without a sentence end runs on, also across a page break; numbered paragraphs ("2.-"), list items ("a)") and articles start new lines.
- Unit layout: one file per article (art-NNN), the preamble, the introduction, each transitional provision, the repealing and final provisions, the closing formula, and one structure file (estructura) naming the article each heading precedes.
- Typesetting is normalised once: NBSP to space, curly apostrophes to straight ones, curly double quotes to « », runs of spaces collapsed. Spelling is kept as printed (for example "DELAS FUERZAS ARMADAS").
- Ley General de Trabajo: one version, Ley Núm. 4/2021 as printed by the Dirección General del Boletín Oficial del Estado, credited to the law and dated 2022-03-02. Its final provision puts it in force "a los treinta días de su publicación en el Boletín Oficial del Estado"; the BOE's online index does not list the issue, so the publication day used is the date of the BOE's printed edition (Malabo, 31 January 2022), and the thirtieth day counted from the day after is 2 March 2022.
- Ley General de Trabajo: Ley Núm. 6/2026 (10 April 2026), which amends some of its articles, is on the BOE only as a scanned image and is not applied: the record holds the text as enacted.
- Ley General de Trabajo: the preamble, one file per article (art-NNN, the number and heading on the first line), and one file per additional, transitional and repealing provision; title and chapter headings, the edition's cover and running footer and the closing formula ("Así lo dispongo ...") are not units. The repealing provision's file also holds the unheaded entry-into-force sentence printed under it.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- Claude Code (Claude Opus 5.5, claude-opus-5-5) wrote Lexifina's code, chose the sources and wrote the decisions. No model wrote, summarised or transformed legal text.
