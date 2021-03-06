# Final Report - Google Summer of Code 2019

---

# TL;DR (abstract)

In my GSoC, I bridged the data standard "BIDS" and the analyis software
"MNE-Python" to facilitate automatic data analysis in the domain of
neuro-electrophysiology.

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

The mne-study-template is a set of processing files that form a complete
pipeline for automatic processing of MEG and EEG datasets.
So far, the study template had relied on some unspecified data structure, that
was still relatively rigid. Through BIDS, the expected input for the study
template can become much more transparent ... and the code base can be
significantly reduced through reading the data from metadata files that we
know MUST be present in BIDS.

Preparing the mne-study-template to be BIDS compatible involved several key
points, such as:

- preparing testing datasets
- testing CI setups
- working on the study-template itself
- changes to MNE-BIDS and MNE-Python along the way

All of these points have been part of my GSoC, and as an outcome of the overall
project work, the mne-study-template is now usable with BIDS
formatted data, MNE-BIDS version 0.3 is released, and lots of other benefical
outcomes are usable to the community at large.

# Usable outcomes: **Highlights**

Here I list the highlights of my contributions in several projects that are
interrelated. Somewhat ordered by importance (but feel free to disagree!)

- **[mne-study-template](https://github.com/mne-tools/mne-study-template)**
    - make the template BIDS compatible: https://github.com/mne-tools/mne-study-template/pull/35
    - document how to turn any dataset into a git-annex dataset fetchable with datalad: https://blogs.python-gsoc.org/en/sappelhoffs-blog/eleventh-week-of-gsoc-some-more-datalad-complete-and-automatic-flow-now/
    - CI with circleci: https://github.com/mne-tools/mne-study-template/pull/53


- **[mne-bids](https://github.com/mne-tools/mne-bids)**
  - `0.3` release: https://github.com/mne-tools/mne-bids/releases/tag/v0.3
  - `write_anat` to write T1w MRIs to BIDS for coregistration: https://github.com/mne-tools/mne-bids/pull/211
  - `get_head_mri_trans` function to estimate a `trans` matrix from an MRI and a `raw` object: https://mne.tools/mne-bids/auto_examples/convert_mri_and_trans.html#sphx-glr-auto-examples-convert-mri-and-trans-py



- **[mne-python](https://github.com/mne-tools/mne-python)**
  - add a new digitization format: BrainVision CapTrack: https://github.com/mne-tools/mne-python/pull/6663
  - somato data now in BIDS: https://github.com/mne-tools/mne-python/pull/6414
  - refactor BrainVision test suite: https://github.com/mne-tools/mne-python/pull/6623


- **[pybv](https://github.com/bids-standard/pybv)**
  - `0.1` release: https://github.com/bids-standard/pybv/releases/tag/v0.1.0
  - writing of measurement date: https://github.com/bids-standard/pybv/pull/29
  - bring up to date to work with MNE > 0.17: https://github.com/bids-standard/pybv/pull/26


- **[autoreject](https://github.com/autoreject/autoreject)**
  - extend docs on how the algorithm works: https://github.com/autoreject/autoreject/pull/147
  - overhaul CIs (speed up and fixing): https://github.com/autoreject/autoreject/pull/145



- **[bids-validator](https://github.com/bids-validator/bids-validator)**
  - add guide for BIDS extension development: https://github.com/bids-standard/bids-validator/pull/806
  - update regular expressions for MEG data: https://github.com/bids-standard/bids-validator/pull/789

# Unfinished business

A single Google Summer of Code is not enough to fix all problems that appear
along the way.
Right below I list some work that can be picked up by other community members,
or even myself at the next convenient time.
As before, this is not an exhaustive list, it merely highlights the most
pressing issues.

- MNE-Python has the "reports" feature that can provide html reports for
  analysis steps that have been run. This feature should be integrated into
  the mne-study-template, but it's not working so far.
  (issue [#47](https://github.com/mne-tools/mne-study-template/issues/47)
  in mne-study-template)


- MNE-BIDS has a `read_raw_bids` function. Unfortunately, this function does
  currently not read any digitization files such as the headshape, electrode
  positions, or head position coils. (issue
  [#203](https://github.com/mne-tools/mne-bids/issues/203) in mne-bids)


- MNE-BIDS has the function to write anatomical data with its `write_anat`
  function. This function depends on reading fiducial points from an MNE
  `raw` object. In the future, it should be possible for the function to get
  fiducial information from a BIDS `coordsystem.json` file (issue
  [#214](https://github.com/mne-tools/mne-bids/issues/214) in mne-bids)

# Complete documentation

Throughout my GSoC, I have written a changelog with all work I have done each
day.
The changelog is structured by weeks and days with the most recent dates on
top of the document.

The document can be found in this repository:
[changelog.md](https://github.com/sappelhoff/gsoc2019/blob/master/changelog.md)

The blog that I wrote during my GSoC can be found
[here](https://blogs.python-gsoc.org/en/sappelhoffs-blog/).

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
