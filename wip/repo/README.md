# Equatorial Guinea: law history in git

The law of Equatorial Guinea as a git history. Each provision is one file, each law gets one commit on the day it took effect, and the law that made each change is the commit's author. `git blame` names the law behind every paragraph, `git log` lists every change to an article, and `tools/en_vigor_el.py` gives the text in force on any day.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `gq/`.

> **Not today's text.** The Ley Fundamental here is the text of 2012. Ley 1/2025, de 16 de julio, reformed arts. 56.1, 80 and 84.1 and 2, but the Boletín Oficial del Estado publishes that law only as a scan, so the reform is not applied (see below). This build is a preview: it is not on `main`.

**What is in it now**

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `ley-fundamental/` | Ley Fundamental de Guinea Ecuatorial | 1 | Ley Núm. 1/2012, de fecha 16 de febrero, as promulgated in Bata after the referendum of 13 November 2011: the introduction, the preamble, arts. 1 to 134, two transitional provisions, the repealing and final provisions, the closing formula, and the structure of titles and chapters |

**What is missing**

- **Before 2012.** The Ley Fundamental of 1991 and its reform of 1995 replaced by Ley 1/2012 were not found online with a text layer: the BOE's own search lists only Ley 1/2012 and Ley 1/2025 under "Ley Fundamental", and the Internet Archive holds only the same 2012 file. So the history starts in 2012, with the text as enacted.
- **After 2012.** Ley Nº 1/2025, de fecha 16 de julio, "por la que se Reforma los Artículos 56.1, 80 y 84.1 y 2 de la Ley Fundamental de Guinea Ecuatorial", is published by the BOE as page images inside a PDF, with no text layer. Scans are not transcribed, so its wording and its in-force date are unknown here. Arts. 56, 80 and 84 in this repository are the 2012 wording.
- **Other acts.** The BOE lists no Código Penal; it has 110 laws in its "LEYES" category, none of them a consolidated code.

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
- `--before="YYYY-MM-DD"` alone uses your clock's time of day, so a change that took effect that day may be missed before noon. Use `T23:59:59Z` as above, or the tool.

## How it is checked

- Every version is read back from git on the day it took effect and on the day before (`tools/check_repo.py`); both must match `corpus.json`. Results are in `REPRODUCE.md`.
- The repository is rebuilt from the same data a second time and must give identical hashes.
- The text is read from the PDF's own text layer (made with FPDF, not scanned), and every word of it was compared with a second extraction (pdftotext): they differ only in the headings and title page, which are not in the article files.

## What "author" means

The author of a commit is the law that made the change, with an e-mail address that cannot exist, so `git blame` and `git log --author` name laws. The committer is always Lexifina. Here the one commit is credited to Ley 1/2012, the Ley Fundamental as enacted. Blame credits whole lines (one paragraph per line); use `git log -p --word-diff` to see exactly which words a change made.

## What it does not show

- **The Ley Fundamental of 1991 and 1995**, and the reform of 2025 (see above).
- **Headings** (títulos, capítulos) are not in the article files; they are gathered in `estructura.md`, each line naming the article it precedes.
- **The BOE's page furniture**: the title page and the electronic-signature line on every page ("Documento firmado electrónicamente con código de verificación …").
- **No OCR.** Texts published only as scanned images are not included.

## How it is built

`tools/fetch.py` downloads each file once with curl, at no more than one request per second, cached by the sha256 of its URL. `tools/parse.py` reads only the cache: it reads the PDF's text layer with PyMuPDF, drops the signature line, rebuilds paragraphs from the layout, splits the text into one file per article and writes `corpus.json`; the shared builder `tools/build.py` turns it into the commits. `REPRODUCE.md` lists every source, command, tool version and decision, and the result of the hash-for-hash rebuild.

## Sources

| Source | What it gives | Used for |
| --- | --- | --- |
| [Boletín Oficial del Estado](https://boe.gob.gq) (Presidencia del Gobierno) | Each law and decree as enacted, one PDF each; a search form (title, category, text) | The text and dates of the Ley Fundamental; the list of its reforms |

The BOE publishes no consolidation, no past versions and no amendment notes. Research guides that cover every country: [GlobaLex](https://www.nyulawglobal.org/globalex/) and the [Law Library of Congress Guide to Law Online](https://www.loc.gov/research-centers/law-library-of-congress/researcher-resources/guide-to-law-online/).

## Licence

See [LICENSE](LICENSE). Text: Ley Núm. 1/2012 (Ley Fundamental de Guinea Ecuatorial), as published by the Boletín Oficial del Estado de Guinea Ecuatorial; an official text of the Republic of Equatorial Guinea, reproduced with that attribution. Lexifina's arrangement, messages, tables and tools are CC0.

This repository is not legal advice.

## En español

Este repositorio recoge la historia del derecho ecuatoguineano en git: un archivo por artículo, un commit por ley en la fecha de su entrada en vigor, y la ley que modificó el texto como autora del commit. Contiene por ahora la Ley Fundamental de Guinea Ecuatorial promulgada por la Ley Núm. 1/2012, de 16 de febrero, tras el Referéndum de 13 de noviembre de 2011, tomada del Boletín Oficial del Estado. **No es el texto vigente hoy**: la Ley Nº 1/2025, de 16 de julio, que reforma los artículos 56.1, 80 y 84.1 y 2, solo se publica como imagen escaneada y no se aplica; las Leyes Fundamentales de 1991 y 1995 no se encontraron en formato de texto. `python tools/en_vigor_el.py 2020-01-01 ley-fundamental 80` muestra el artículo 80 vigente en esa fecha, y `git blame ley-fundamental/art-080.md` indica la ley de cada párrafo. Este repositorio no constituye asesoramiento jurídico.
