# pdflatex-clean
A python script that creates clean LaTeX-PDFs without active contents.

When you create a PDF with [pdflatex](https://ctan.org/pkg/pdftex), you may have some of these recognized upcoming issues:

- You cannot upload a PDF of e.g. letters or your CV to careers website or other websites due to 'active contents'
- Selecting text and math equations in the output PDF is a horrible mess

## The solution

pdflatex-clean is a solution to both of these problems. It executes the pdf conversion process using `pdflatex` with all arguments given
and then creates a clean `PDF` file using [GhostScript](https://www.ghostscript.com/).

## Prerequisites

You will need the following things to use pdflatex-clean:

- A Linux machine (please report if the code also works on Windows or Mac)
- A working TeX installation (preferably Tex Live) with `pdflatex` binary available in your `$PATH` variable.
- A working GhostScript installation with `gs` binary available in your `$PATH` variable
- A working `Python 3` installation with working `pip` for installation

## Installation

The simplest and currently only way to install `pdflatex-clean` is to use pip:

```sh
pip install https://github.com/JonasBernard/pdflatex-clean/archive/main.zip
```

## Usage

You can use `pdflatex-clean` the same way you use `pdflatex`.
All aguments will be passed to `pdflatex`.
> Exceptions: 
> - `-interaction` flag will always be set to `nonstopmode`
> - `-output-format` flag will always be set to `pdf`

```sh
pdflatex-clean myTexFile.tex
```
will create a `myTexFile.pdf` from `myTexFile.tex`.

## Licensing

A python script that creates clean LaTeX-PDFs without active contents.
Copyright (C) 2020 Jonas Bernard

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
