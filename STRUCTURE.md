# Estructura / Structure

Una carpeta por norma, un archivo por artículo (`art-NNN.md`), con `preambulo.md`, `firma.md` y un `README.md` por carpeta. Ninguna carpeta tiene más de 1.000 entradas.

One folder per act, one file per article (`art-NNN.md`), with `preambulo.md`, `firma.md` and a `README.md` in each folder. No folder holds more than 1,000 entries.

| Carpeta | Contenido |
| --- | --- |
| `constitucion/` | Ley Fundamental de Guinea Ecuatorial (Ley 1/2012); `estructura.md` lists titles and chapters |
| `codigos/<codigo>/` | Codes: `codigos/codigo-civil/` (the Spanish Código Civil as in force on 12 October 1968, split into `titulo-preliminar/` and `libro-1/` to `libro-4/`) |
| `leyes/<año>/<núm>-<objeto>/` | Leyes and Leyes Orgánicas, by year of the law's number (e.g. `leyes/2021/4-general-de-trabajo/`) |
| `decretos-leyes/<año>/<núm>-<objeto>/` | Decretos-Leyes |
| `decretos/<año>/<núm>-<objeto>/` | Decretos |
| `ordenes/<año>/<núm>-<objeto>/` | Órdenes and Órdenes Ministeriales |
| `resoluciones/<año>/...` | Resoluciones |
| `tratados/<año>/<objeto>/` | Treaties published as national texts |
| `ohada/actos-uniformes/<acto>/` | OHADA Uniform Acts, directly applicable in Equatorial Guinea (Treaty art. 10), in the official OHADA text (French, or OHADA's official English translation where that is the only text layer); one file per article, `visas.md` for the preamble |
| `tools/`, `data/` | Tools (`tools/en_vigor_el.py`) and tables |

Names are Spanish, the language the law is published in; `<objeto>` is a short slug of the act's title. Appointments, decorations and similar individual acts are not included.
