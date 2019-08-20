# Final Report - Google Summer of Code 2019

---

# TL;DR (abstact)

# Description

With the emergence of the Brain Imaging Data Structure (BIDS) in 2016, the
scientific community received a standard to organize and share data in the
broad domain of Neuroscience / Neuroimaging.

BIDS prescribes how the highly complex data that results from experiments should
be structured and which metadata should be encoded next to the raw data. Through
this, there are several benefits that can be reaped:

1. a
1. b
1. c

The objective in my Google Summer of Code (GSoC) 2019 was to harness BIDS to
simplify common workflows in the analysis of neuroimaging data and specifically
in the analysis of electrophysiology data such as EEG, MEG, and iEEG.

Inititally, the idea of Mainak Jas, Alexandra Gramfort (my mentors) was to program
a versatile analysis pipeline drawing on BIDS and several other existing packages
that already make interfaces between BIDS and Python.

However, after a few early discussions, we decided against programming a new
analysis pipeline from scratch and instead determined to focus on revamping the
existing mne-study-template to draw on BIDS.

What is the MNE-study-template?

This involed

- preparing testing datasets
- testing CI setups
- changes to MNE-BIDS and MNE-Python along the way

- What is BIDS
- How can MNE-Python etc. benefit from BIDS?


- initial proposal and how it quickly changed
- state before GSoC
- state after GSoC


# Usable outcomes

which GSoC outcomes are directly usable and how?

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

what work did not get finished up ... and how can somebody pick up the work?


# Complete documentation

... can be found in the changelog. It's ordered by weeks and days: Most recent
on top

# Acknowledgements

- Mainak
- Alex
- Eric
- Juan Massich
- MNE-Python community
- BIDS community
- Google Open Source for funding the Google Summer of Code
