# Equatorial Guinea: law history in git

The law of Equatorial Guinea as a git history. Each provision is one file, each law gets one commit on the day it took effect, and the law that made each change is the commit's author. `git blame` names the law behind every paragraph, `git log` lists every change to an article, and `tools/en_vigor_el.py` gives the text in force on any day.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `gq/`.

> **Not today's text.** The Ley Fundamental here is the text of 2012. Ley 1/2025, de 16 de julio, reformed arts. 56.1, 80 and 84.1 and 2, but the Boletín Oficial del Estado publishes that law only as a scan, so the reform is not applied (see below): this record ends with the text of 2012, and for arts. 56, 80 and 84 it does not show the law in force after the 2025 reform.

**What is in it now**

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `ley-general-de-trabajo/` | Ley Núm. 4/2021, de fecha 3 de Diciembre, General de Trabajo | 1 | The law as enacted, from the BOE's printed edition (Malabo, 31 January 2022): the preamble, arts. 1 to 120, the additional, transitional and repealing provisions; in force 2 March 2022. Ley Núm. 6/2026, which amends it, is not applied |
| `ley-fundamental/` | Ley Fundamental de Guinea Ecuatorial | 1 | Ley Núm. 1/2012, de fecha 16 de febrero, as promulgated in Bata after the referendum of 13 November 2011: the introduction, the preamble, arts. 1 to 134, two transitional provisions, the repealing and final provisions, the closing formula, and the structure of titles and chapters |

**What is missing**

- **Before 2012.** The Ley Fundamental of 1991 and its reform of 1995 replaced by Ley 1/2012 were not found online with a text layer: the BOE's own search lists only Ley 1/2012 and Ley 1/2025 under "Ley Fundamental", and the Internet Archive holds only the same 2012 file. So the history starts in 2012, with the text as enacted.
- **After 2012.** Ley Nº 1/2025, de fecha 16 de julio, "por la que se Reforma los Artículos 56.1, 80 y 84.1 y 2 de la Ley Fundamental de Guinea Ecuatorial", is published by the BOE as page images inside a PDF, with no text layer. Scans are not transcribed, so its wording and its in-force date are unknown here. Arts. 56, 80 and 84 in this repository are the 2012 wording.
- **After 2021 in the labour law.** Ley Núm. 6/2026, de fecha 10 de abril, which amends some articles of the Ley General de Trabajo, is published by the BOE only as page images; it is not applied, so `ley-general-de-trabajo/` is the law as enacted.
- **Other acts.** The BOE's online index lists no Código Penal; the Código Penal of 2022 (Ley Núm. 4/2022) was found only as a scan. The BOE has 110 laws in its "LEYES" category, none of them a consolidated code.

## A lawyer's questions as git commands

| Question | Command |
| --- | --- |
| What did art. 80 say on 1 January 2020? | `python tools/en_vigor_el.py 2020-01-01 ley-fundamental 80` |
| The same, with raw git (bash) | `git show $(git rev-list -1 --before="2020-01-01T23:59:59Z" HEAD -- ley-fundamental/art-080.md):ley-fundamental/art-080.md` |
| The same, in PowerShell | `$r = git rev-list -1 --before="2020-01-01T23:59:59Z" HEAD -- ley-fundamental/art-080.md; git show "$($r):ley-fundamental/art-080.md"` |
| Which law wrote each paragraph of art. 80? | `git blame ley-fundamental/art-080.md` |
| Every change to an article, word by word | `git log -p --word-diff ley-fundamental/art-080.md` |
| Every law in the record, in order | `git log --reverse --format="%ad %an" --date=short` |
| The whole Ley Fundamental on a date | `python tools/en_vigor_el.py 2020-01-01 ley-fundamental` |
| Where an article sits (title, chapter) | `ley-fundamental/estructura.md` |

After a rebuild, refresh tags with `git fetch --force --tags`: a plain fetch keeps stale tags.

## Dates

- Each commit is dated at **noon, Africa/Malabo, on the day the change took effect**. The day is also in the `In-force:` trailer, which the tools read.
- **The day comes from the law's own clause.** Disposición final: "La presente Ley Fundamental entrará en vigor a partir de su promulgación por el Presidente de la República, después de haber sido aprobada en Referéndum y su publicación en el Boletín Oficial del Estado". It was promulgated in Bata on 16 February 2012, the date under which the BOE lists it; the BOE gives no separate publication date.
- **2022-03-02:** the Ley General de Trabajo's final provision puts it in force "a los treinta días de su publicación en el Boletín Oficial del Estado". The BOE's online index does not list the issue; the date used for publication is that of the BOE's printed edition (Malabo, 31 January 2022), and the thirtieth day after it is 2 March 2022.
- `--before="YYYY-MM-DD"` alone uses your clock's time of day, so a change that took effect that day may be missed before noon. Use `T23:59:59Z` as above, or the tool.

## How it is checked

- Every version is read back from git on the day it took effect and on the day before (`tools/check_repo.py`); both must match `corpus.json`. Results are in `REPRODUCE.md`.
- The repository is rebuilt from the same data a second time and must give identical hashes.
- Every paragraph and article heading of the Ley General de Trabajo was found, in order, in a second, independent extraction of its PDF (pdftotext); its arts. 1 to 120 are all present.
- The Ley Fundamental is read from the PDF's own text layer (made with FPDF, not scanned), and every word of it was compared with a second extraction (pdftotext): they differ only in the headings and title page, which are not in the article files.

## What "author" means

The author of a commit is the law that made the change, with an e-mail address that cannot exist, so `git blame` and `git log --author` name laws. The committer is always Lexifina. Here the Ley Fundamental's commit is credited to Ley 1/2012, the Ley Fundamental as enacted, and the Ley General de Trabajo's to Ley Núm. 4/2021, the law as enacted. Blame credits whole lines (one paragraph per line); use `git log -p --word-diff` to see exactly which words a change made.

## What it does not show

- **The Ley Fundamental of 1991 and 1995**, and the reform of 2025 (see above).
- **Headings** (títulos, capítulos) are not in the article files; for the Ley Fundamental they are gathered in `estructura.md`, each line naming the article it precedes. In the Ley General de Trabajo each article's own heading is on its first line.
- **The BOE's page furniture**: the title page and the electronic-signature line on every page ("Documento firmado electrónicamente con código de verificación …").
- **No OCR.** Texts published only as scanned images are not included.

## How it is built

Lexifina reads the sources listed here and records each act's dated versions, and the laws that made each change, in one corpus file. `tools/build.py` writes this repository from that file, and the same corpus always gives the same commit hashes; `REPRODUCE.md` gives the details and the checks. A model (Claude) wrote Lexifina's code; it wrote no legal text, and no model runs when the history is built.

Lexifina's code reads the BOE's PDF through its own text layer with PyMuPDF, drops the signature line, rebuilds paragraphs from the layout, splits the text into one file per article and writes `corpus.json`; the shared builder `tools/build.py` turns it into the commits.

## Sources

| Source | What it gives | Used for |
| --- | --- | --- |
| [Boletín Oficial del Estado](https://boe.gob.gq) (Presidencia del Gobierno) | Each law and decree as enacted, one PDF each; a search form (title, category, text) | The text and dates of the Ley Fundamental; the list of its reforms; the Ley General de Trabajo's amendment of 2026 (a scan, not used) |
| BOE printed edition of Ley Núm. 4/2021, General de Trabajo (Dirección General del B.O.E., Malabo, 31 January 2022), copy held by the [Observatoire des Forêts d'Afrique Centrale (COMIFAC)](https://www.observatoire-comifac.net) | The labour law as enacted, born-digital | `ley-general-de-trabajo/` |

The BOE publishes no consolidation, no past versions and no amendment notes. Research guides that cover every country: [GlobaLex](https://www.nyulawglobal.org/globalex/) and the [Law Library of Congress Guide to Law Online](https://www.loc.gov/research-centers/law-library-of-congress/researcher-resources/guide-to-law-online/).

## Licence

See [LICENSE](LICENSE). Text: Ley Núm. 1/2012 (Ley Fundamental de Guinea Ecuatorial) and Ley Núm. 4/2021 (General de Trabajo), as published by the Boletín Oficial del Estado de Guinea Ecuatorial; an official text of the Republic of Equatorial Guinea, reproduced with that attribution. Lexifina's arrangement, messages, tables and tools are CC0.

This repository is not legal advice.

## En español

Este repositorio recoge la historia del derecho ecuatoguineano en git: un archivo por artículo, un commit por ley en la fecha de su entrada en vigor, y la ley que modificó el texto como autora del commit. Contiene por ahora la Ley Fundamental de Guinea Ecuatorial promulgada por la Ley Núm. 1/2012, de 16 de febrero, tras el Referéndum de 13 de noviembre de 2011, tomada del Boletín Oficial del Estado, y la Ley Núm. 4/2021, General de Trabajo, tal como se promulgó (en vigor desde el 2 de marzo de 2022; la Ley Núm. 6/2026, que la modifica, solo se publica escaneada y no se aplica). **No es el texto vigente hoy**: la Ley Nº 1/2025, de 16 de julio, que reforma los artículos 56.1, 80 y 84.1 y 2, solo se publica como imagen escaneada y no se aplica; las Leyes Fundamentales de 1991 y 1995 no se encontraron en formato de texto. `python tools/en_vigor_el.py 2020-01-01 ley-fundamental 80` muestra el artículo 80 vigente en esa fecha, y `git blame ley-fundamental/art-080.md` indica la ley de cada párrafo. Este repositorio no constituye asesoramiento jurídico.
