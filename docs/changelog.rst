=========
Changelog
=========

Version 0.6.1
-------------
Released date: December 16, 2017

In this release, we have fixed various bugs and introduced new features:

* Users now can provide all the `BedTools` options by setting `--bedtools-options` argument in `venn`, `upset` and `pairwise` module. Thanks to Issue #3
* Now users can save all the overlapping genomic regions as BED and name lists as text file as by setting `--save-overlaps`. Thanks to those who suggested this feature.
* We added `--bordercolors` to change the Venn border colors.


Version 0.6.0
-------------
Released date: December 11, 2017

* Fixed the pairwise module's `--names` argument. Thanks to @adomingues for reporting the bug.


Version 0.5.9
-------------
Released date: December 08, 2017

* Fixed the bug with two lists, issue #1 reported by @dayanne-castro
* Fixed upset module memory issue for large number of sets