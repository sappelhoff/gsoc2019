# Final Report - Google Summer of Code 2019

---

# TL;DR (abstract)



# Description

With the emergence of the Brain Imaging Data Structure (BIDS) in 2016, the
scientific community received a standard to organize and share data in the
broad domain of Neuroscience / Neuroimaging.

BIDS prescribes how the highly complex data that results from experiments should
be structured and which metadata should be encoded next to the raw data. Through
this, there are several benefits that can be reaped:

1. **sharing data within a lab and between labs:** Through the structured
   specification, everybody who has read the basics can understand any BIDS
   dataset without requiring specialist knowledge.
1. **data validation:** Use software to check whether everything is documented or
   whether there are missing data (see
   [bids-validator](https://github.com/bids-standard/bids-validator))
1. **automatic data analysis pipelines:** Through the use of REQUIRED,
   RECOMMENDED, and OPTIONAL flags for data in BIDS, analysis software can
   perfectly know which data to expect and where to search for it. Data reading
   and processing are facilitated and can be automated to a much higher degree
   than with non-standard data structures.

... and many more benefits - I recommend reading the
[original publication on BIDS](https://www.nature.com/articles/sdata201644).

The objective in my Google Summer of Code (GSoC) 2019 was to harness BIDS to
simplify common workflows in the analysis of neuroimaging data and specifically
in the analysis of electrophysiology data such as EEG, MEG, and iEEG.

Inititally, the idea of Mainak Jas, Alexandra Gramfort (my mentors) was to program
a versatile analysis pipeline drawing on BIDS and several other existing packages
that already make interfaces between BIDS and Python.

However, after a few
[early discussions](https://github.com/sappelhoff/gsoc2019/issues?utf8=%E2%9C%93&q=is%3Aissue+is%3Aclosed+pipeline),
we decided against programming a new analysis pipeline from scratch and instead
determined to focus on revamping the existing
[mne-study-template](https://github.com/mne-tools/mne-study-template)
to draw on BIDS.

What is the MNE-study-template?

This involed

- preparing testing datasets
- testing CI setups
- changes to MNE-BIDS and MNE-Python along the way

As an outcome, the mne-study-template is now usable ... mne-bids 0.3 is released
and lots of other benefical outcomes are usable to the community at large.

# Usable outcomes: **Highlights**

Here I list
- MNE-BIDS

- mne-study-template
    - datasets (datalad + git-annex)
    - CI with circleci

- mne-python

- Pybv
  - release

- autoreject

- bids-validator

# Unfinished business

A single Google Summer of Code is not enough to fix all problems that appear
along the way.
Right below I list some work that can be picked up by other community members,
or even myself at the next convenient time.
As before, this is not an exhaustive list, it merely highlights the most
pressing issues.

1. a
1. b
1. c

# Complete documentation

Throughout my GSoC, I have written a changelog with all work I have done each
day.
The changelog is structured by weeks and days with the most recent dates on
top of the document.

The document can be found in this repository:
[changelog.md](https://github.com/sappelhoff/gsoc2019/blob/master/changelog.md)

# Acknowledgements

I have received a lot of support by my mentors @jasmainak and @agramfort, both
of which helped me to write clean code and to stay practical.

I am furthermore grateful to @larsoner and @massich for providing guidance and
advise in topics surrounding MNE-Python, code testing, and Python in general.

Both the MNE-Python community and BIDS community made my time during the GSoC
very enjoyable and productive.

Lastly, I think that Google Open Source is doing a great job with their
Google Summer of Code program and I consider myself lucky to have been a part
of this.
