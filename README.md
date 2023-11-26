[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
<div align="center">
  <h1>NGS&nbsp;Report&nbsp;Extractor</h1>
  <h2> Parse Genetic Mutation Data From NGS Reports Using OCR&nbsp;</h2>
</div>
 
<br />

![READ ME Image of Project](https://cdn.european-virus-archive.com/sites/default/files/field/image/NGS.jpg)

<br />
The data folder contains input and output folders.

The script iterates over the files  and processes differently.

When it encounters an image file (.jpeg or .png) it is processed by OCR using [Tesseract](https://es.wikipedia.org/wiki/Tesseract_OCR).

The data/input folder when contains .pdf files these are parsed using [Camelot](https://camelot-py.readthedocs.io/en/master/).

The output files are stored in data/output folder in as filename.json 




***




<h6>Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)</h6>
<div style="width:300px; height:200px">
</div>