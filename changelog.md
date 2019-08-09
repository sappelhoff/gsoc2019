Week 13
=======

Sunday, 2019-08-25
------------------

Saturday, 2019-08-24
--------------------

Friday, 2019-08-23
------------------

Thursday, 2019-08-22
--------------------

Wednesday, 2019-08-31
---------------------

Tuesday, 2019-08-20
-------------------

Monday, 2019-08-19
------------------

Week 12
=======

Sunday, 2019-08-18
------------------
- enjoyed free time :-)

Saturday, 2019-08-17
--------------------
- enjoyed free time :-)

Friday, 2019-08-16
------------------

Thursday, 2019-08-15
--------------------

Wednesday, 2019-08-14
---------------------

Tuesday, 2019-08-13
-------------------

Monday, 2019-08-12
------------------

Week 11
=======

Sunday, 2019-08-11
------------------
- wrote blog post:

Saturday, 2019-08-10
--------------------
- enjoyed free time :-)

Friday, 2019-08-09
------------------
- conversion of MNE-somato-data into git-annex dataset via OSF: https://osf.io/3qmer/
- figured out the datalad-osf issues and submitted a fix: https://github.com/templateflow/datalad-osf/pull/2
- prepared a PR to make "make source" work: https://github.com/mne-tools/mne-study-template/pull/48

Thursday, 2019-08-08
--------------------
- opened new issue to make `source` and `report` work in study template: https://github.com/mne-tools/mne-study-template/issues/47
- started to work on Mainak's PRs:
  - https://github.com/mne-tools/mne-study-template/pull/43
  - https://github.com/mne-tools/mne-study-template/pull/41
- prepared a PR to comply with WIP BIDS spec on derivatives: https://github.com/mne-tools/mne-study-template/pull/46
- finished removing the pybids dependency in mne-study-template: https://github.com/mne-tools/mne-study-template/pull/42
- added eeg_matchingpennies to test suite of mne-study-template: https://github.com/mne-tools/mne-study-template/pull/45

Wednesday, 2019-08-07
---------------------
- prepared a PR to extract "kinds" (=datatypes) from a BIDS dir: https://github.com/mne-tools/mne-bids/pull/253/files
- worked on PR for giving mne-bids a taste of pybids functionality: https://github.com/mne-tools/mne-bids/pull/252
- improved docs for mne-bids examples and addressed review to MNE-sample-data update: https://github.com/bids-standard/bids-examples/pull/164
- started PR to remove pybids dependency from mne-study-template: https://github.com/mne-tools/mne-study-template/pull/42
- reviewed and merged PR for mne-study-template: https://github.com/mne-tools/mne-study-template/pull/40

Tuesday, 2019-08-06
-------------------
- prepared PR to use mne config in mne-study-template: https://github.com/mne-tools/mne-study-template/pull/39
- opened issue with bids-validator, which is now breaking mne-bids: https://github.com/bids-standard/bids-validator/issues/812
- addressed review to pybids-replacement: https://github.com/mne-tools/mne-bids/pull/252

Monday, 2019-08-05
------------------
- discussed about BIDS anonymization of data in MNE: https://github.com/mne-tools/mne-python/issues/6621
- reviewed a PR on MNE-Python: https://github.com/mne-tools/mne-python/pull/6628
- prepared a PR to replace pybids: https://github.com/mne-tools/mne-bids/pull/252

Week 10
=======

Sunday, 2019-08-04
------------------
- wrote blog post: https://blogs.python-gsoc.org/en/sappelhoffs-blog/tenth-week-of-gsoc-git-annex-and-datalad
- reviewed mne-study-template PR: https://github.com/mne-tools/mne-study-template/pull/35

Saturday, 2019-08-03
--------------------
- re-uploaded MNE-sample-data to bids-examples repository: https://github.com/bids-standard/bids-examples/pull/164
- worked on PR for eeg_matchingpennies fetcher: https://github.com/mne-tools/mne-bids/pull/249
- worked on making eeg_matchingpennies work via datalad, "the manual road", because osf_datalad is failing: https://github.com/templateflow/datalad-osf/issues/1#issuecomment-517743290
- addressed reviews to several PRs
  - BrainVision testing refactoring: https://github.com/mne-tools/mne-python/pull/6623
  - exposing of bootstrap_ci in MNE-Python: https://github.com/mne-tools/mne-python/pull/6624

Friday, 2019-08-02
------------------
- prepared a PR for a dataset fetcher for eeg_matchingpennies dataset: https://github.com/mne-tools/mne-bids/pull/249
- prepared a PR to expose private function in MNE-Python: https://github.com/mne-tools/mne-python/pull/6624
- worked on mne-study-template
  - identified remaining issues with ds0000117: https://github.com/mne-tools/mne-python/issues/6621
- prepared a PR to MNE-Python to parametrize BV date tests and use fixtures: https://github.com/mne-tools/mne-python/pull/6623
- make import policy im mne-bids PEP8 compliant and consistent: https://github.com/mne-tools/mne-bids/pull/248

Thursday, 2019-08-01
--------------------
- Laptop restored
- worked on test suite for BrainVision

Wednesday, 2019-07-31
---------------------
- Laptop broke down, very unproductive day
- finished bugfix PR to MNE-Python: https://github.com/mne-tools/mne-python/pull/6611

Tuesday, 2019-07-30
-------------------
- continued working on the CI for mne-study-template
  - looked into datalad and OSF integration to get matchingpennies as git annex dataset: https://github.com/templateflow/datalad-osf/issues/1
- tried to reupload the updated MNE-sample-data (ds000248) to OpenNeuro
  - reported problems with installing the CLI: https://github.com/OpenNeuroOrg/openneuro/issues/1220
  - reported problems with the actual upload: https://github.com/OpenNeuroOrg/openneuro/issues/1221

Monday, 2019-07-29
------------------
- found a way to better search OpenNeuro (via Chris M. from Poldracklab): https://docs.google.com/spreadsheets/d/1rsVlKg0vBzkx7XUGK4joky9cM8umtkQRpJ2Y-5d6x7c/
- prepared a PR to MNE-Python to fix BrainVision date string reading: https://github.com/mne-tools/mne-python/pull/6611
- started CI implementation for mne-study-template: https://github.com/sappelhoff/mne-study-template/pull/1
  - involving datalad issues
  - involving OpenNeuro issues: https://github.com/OpenNeuroOrg/datalad-service/issues/81#issuecomment-515992625
- continued discussion in: https://github.com/mne-tools/mne-bids/pull/244
- fixed a typo in mne-scripts: https://github.com/mne-tools/mne-scripts/pull/21
- finished somato PR and uploaded new data to OSF: https://github.com/mne-tools/mne-python/pull/6414
- wrote weekly blog post: https://blogs.python-gsoc.org/en/sappelhoffs-blog/ninth-week-of-gsoc

Week 9
======

Sunday, 2019-07-28
------------------
- enjoyed some free time :-)

Saturday, 2019-07-27
--------------------
- enjoyed some free time :-)

Friday, 2019-07-26
------------------
- reviewed a PR on MNE-Python for ICA: https://github.com/mne-tools/mne-python/pull/6596

Thursday, 2019-07-25
--------------------
- reverted some changes, and incorporated others for the somato conversion script: https://github.com/mne-tools/mne-scripts/pull/20/commits/023c457ed47181443cbf1fd39f223ec6f5098d76
  - final test running now, hopefully finished tomorrow
- finalized update of MNE-sample-data and provided it for Mainak to upload: https://gitter.im/mne-tools/mne-gsoc-2019-BIDS?at=5d3975409114f065e2c6455e
- Skype call with Mainak to dicuss current status and what's up next

Wednesday, 2019-07-24
---------------------
- solved the coordinates mystery: https://github.com/mne-tools/mne-python/pull/6600
- improved issue for BIDS electrodes and coordsystems: https://github.com/bids-standard/bids-validator/issues/672#issuecomment-514599169
- addressed reviews to previous PR on enhancing read_raw_bids: https://github.com/mne-tools/mne-bids/pull/244
- improved help and usage of CLI in mne-bids: https://github.com/mne-tools/mne-bids/pull/247
- fixed an example on mne-bids: https://github.com/mne-tools/mne-bids/pull/246
- opened an issue on MNE-Python for freesurfer related: https://github.com/mne-tools/mne-python/issues/6597
  - and opened a PR to fix it: https://github.com/mne-tools/mne-python/pull/6598

Tuesday, 2019-07-23
-------------------
- finished conversion script for somato data and made PR to mne-scripts: https://github.com/mne-tools/mne-scripts/pull/20
- made a PR to improve `print_dir_tree` functionality in mne-bids: https://github.com/mne-tools/mne-bids/pull/245
- made a new release of pybv: https://twitter.com/stefanappelhoff/status/1153660293672833025
- made the second GSoC evaluation

Monday, 2019-07-22
------------------
- updated somato PR to comply with new structure: https://github.com/mne-tools/mne-python/pull/6414
  - also started running `recon-all` ... when ready, we can finalize the somato conversion by uploading to OSF
- updated the convert_somato_dataset notebook: https://github.com/sappelhoff/gsoc2019/blob/master/misc_notebooks/convert_somato_data.ipynb
- prepared a PR to enhance mne-bids read_raw_bids functionality: https://github.com/mne-tools/mne-bids/pull/244
- prepared a PR to fix an mne-bids example: https://github.com/mne-tools/mne-bids/pull/243
- reviewed Mainak's NifTI header PR: https://github.com/mne-tools/mne-bids/pull/241

Week 8
======

Sunday, 2019-07-21
------------------
- wrote weekly blog post: https://blogs.python-gsoc.org/en/sappelhoffs-blog/eighth-week-of-gsoc-mixed-tasks-and-progress
- made a PR to pybv, allow writing of meas_date, and fix indexing bug: https://github.com/bids-standard/pybv/pull/29
- tested bids-validator issue in Mainak's PR and opened an issue on bids-validator repo: https://github.com/bids-standard/bids-validator/issues/803
- continues inquiring the mystery of BrainVision coordinates: https://github.com/mne-tools/mne-python/pull/6402#discussion_r305619808

Saturday, 2019-07-20
--------------------
- investigated mystery why BrainVision coordinates are multiplied by a factor of 85. Relevant for MNE-BIDS coordinate handling: https://github.com/mne-tools/mne-python/pull/4109#issuecomment-513444467
- critically went through MNE-Python proposal to improve ICA docs: https://github.com/mne-tools/mne-python/issues/6588
- reviewed PR for improving/fixing MNE-BIDS write_anat: https://github.com/mne-tools/mne-bids/pull/241

Friday, 2019-07-19
------------------
- worked on mne-study-template: https://github.com/mne-tools/mne-study-template/pull/35/commits/6f8502f9ce6980a6c80fc7d126b5f05fe4621fba
- finished PR: https://github.com/mne-tools/mne-bids/pull/234
- user support, reviews, issue comments around MNE-BIDS, BIDS, and BrainVision:
  - https://github.com/mne-tools/mne-bids/issues/240
  - https://github.com/bids-standard/pybv/issues/28
  - https://github.com/bids-standard/bids-specification/issues/276

Thursday, 2019-07-18
--------------------
- fixed pybv issue to make it fit for MNE 0.18+ ... for better integration into MNE-BIDS:
  - also involved sending an Email to BrainProducts to find, if MNE-Python has a buggy
    or valid behavior for reading events from annotations: 3 digits are assumed, but is that OK?: https://github.com/mne-tools/mne-python/blob/a7b39388b3f5225df554cd7cf770a80b0136fe94/mne/io/brainvision/brainvision.py#L828-L829
- reported new potential pybv issue: https://github.com/bids-standard/pybv/issues/27
- user support and reviewing:
  - https://github.com/mne-tools/mne-bids/pull/236

Wednesday, 2019-07-17
---------------------
- fixed handling of NA data in mne-bids: https://github.com/mne-tools/mne-bids/pull/234
- worked on the mne-study-template
- worked a bit on pybv as related to MNE-BIDS: https://github.com/bids-standard/pybv/pulls/25
- did user support and reviews for MNE-BIDS:
  - https://github.com/mne-tools/mne-bids/issues/229
  - https://github.com/mne-tools/mne-bids/pull/231
  - https://github.com/mne-tools/mne-bids/issues/229
  - https://github.com/mne-tools/mne-bids/issues/232
  - https://github.com/mne-tools/mne-bids/pull/233

Tuesday, 2019-07-16
-------------------
- did only minor maintenance, testing, and integration work

Monday, 2019-07-15
------------------
- Make `write_anat` and `get_head_mri_trans` more robust: https://github.com/mne-tools/mne-bids/pull/227
- did user support for mne-bids: https://github.com/mne-tools/mne-bids/issues/224#issuecomment-511398178
- integrated and tested Alex's work on mne-study-template
- finished PR to enable cli for copyfile functions and automatically generate docs for it: https://github.com/mne-tools/mne-bids/pull/225
- prepared a PR to MNE-Python to make the opt_parser more versatile: https://github.com/mne-tools/mne-python/pull/6572
- fixed a bug in MNE-Python for BrainVision data format: https://github.com/mne-tools/mne-python/pull/6571
  - also contacted Brain Products to find some explanation of whether this is an issue with a software of the recording device
  - also did the user support on the mailing list: https://mail.nmr.mgh.harvard.edu/pipermail//mne_analysis/2019-July/005996.html

Week 7
======

Sunday, 2019-07-14
------------------
- wrote blog post: https://blogs.python-gsoc.org/en/blogs/sappelhoffs-blog/seventh-week-of-gsoc-just-a-status-report/
- did some work on mne-bids docs: https://gitter.im/mne-tools/mne-gsoc-2019-BIDS?at=5d2ae51eeab6cd7763668bdb

Saturday, 2019-07-13
--------------------
- started PR on improving the CLI of mne-bids: https://github.com/mne-tools/mne-bids/pull/225
- finalized PR: https://github.com/mne-tools/mne-bids/pull/219

Friday, 2019-07-12
------------------
- did some user support for mne-bids:
  - https://github.com/mne-tools/mne-bids/issues/224
  - https://github.com/mne-tools/mne-bids/issues/223
- opened an issue, discussing a dedicated example to read_raw_bids: https://github.com/mne-tools/mne-bids/issues/222
- addressed reviews to automatically setting channel types: https://github.com/mne-tools/mne-bids/pull/219

Thursday, 2019-07-11
--------------------
- continued to work on PR setting channel types from channels.tsv in read_raw_bids: https://github.com/mne-tools/mne-bids/pull/219
- reported an MNE-Python issue and proposed a solution: https://github.com/mne-tools/mne-python/issues/6557
- replied to MNE-Python issue: https://github.com/mne-tools/mne-python/issues/6556
- wasted lots of time trying to get rid of warnings in our testing suite such as:
  - `FutureWarning: elementwise comparison failed; returning scalar instead, but in the future will perform elementwise comparison`
  - `numpy.ufunc size changed, may indicate binary incompatibility. Expected 192 from C header, got 216 from PyObject`

Wednesday, 2019-07-10
---------------------
- opened an issue on improving the CLI of mne-bids: https://github.com/mne-tools/mne-bids/issues/220
- prepared an issue and started corresponding PR to improve read_raw_bids: https://github.com/mne-tools/mne-bids/pull/219
- continued work on making mne-study-template BIDS compatible: https://github.com/mne-tools/mne-study-template/pull/35

Tuesday, 2019-07-09
-------------------
- prepared a bugfix to mne-bids: https://github.com/mne-tools/mne-bids/pull/217
- worked on mne-study-template: https://github.com/mne-tools/mne-study-template/pull/35
- figured out a way to link to dev version of docs in mne-bids: https://github.com/mne-tools/mne-bids/issues/215

Monday, 2019-07-08
------------------
- worked on mne-study-template: https://github.com/mne-tools/mne-study-template/pull/35
- finished PR on pybids: https://github.com/bids-standard/pybids/pull/456
- investigated problems with freesurfer and its MNE bindings

Week 6
======

Sunday, 2019-07-07
------------------
- wrote blog post for Python Software Foundation: https://blogs.python-gsoc.org/en/blogs/sappelhoffs-blog/sixth-week-of-gsoc-on-taking-breaks-and-abstaining-from-rewriting-old-code/

Saturday, 2019-07-06
--------------------
- enjoyed free time :)

Friday, 2019-07-05
------------------
- responded to MNE-Python issue related to BrainVision files: https://github.com/mne-tools/mne-python/pull/6525
- prepared a PR to pybids, fixing pep8 while going through codebase: https://github.com/bids-standard/pybids/pull/456
- prepared a WIP PR to mne-study-template to better discuss whether it makes more sense to start from scratch: https://github.com/mne-tools/mne-study-template/pull/35
- gained access to a cluster, where I now run Freesurfer to finalize the PR on somato data: https://github.com/bids-standard/bids-specification/pull/207

Thursday, 2019-07-04
--------------------
- opened issues for MNE-BIDS
  - allow reading fiducials for write_anat also from a coordsystem.json: https://github.com/mne-tools/mne-bids/issues/214
  - homogenize use of `somato_path_bids` and `bids_root`: https://github.com/mne-tools/mne-bids/issues/213
- improved testing for coordinate system PR and finally got it merged: https://github.com/mne-tools/mne-bids/pull/211

Wednesday, 2019-07-03
---------------------
- finalized coordinate system PR
- addressed reviewer comments for coordinate system PR

Tuesday, 2019-07-02
-------------------
- opened an issue on test refactoring in MNE-BIDS: https://github.com/mne-tools/mne-bids/issues/212
- worked on coordinate system PR
  - improved coverage
  - went over reviews
  - finished the example: https://github.com/mne-tools/mne-bids/pull/211/commits/665570e70afe0c6c987a0c41363eb05a29baa2c5

Monday, 2019-07-01
------------------
- implemented roundtrip testing for coordinate systems PR, ready to focus on an example and a final review
- reviewed slideshow by Mainak for upcoming MNE-BIDS presentation
- opened issue on Neurostars to inquire for getting transformations from NIfTI: https://neurostars.org/t/get-voxel-to-ras-transformation-from-nifti-file/4549
- verified visually that conversion of coords is working: https://gitter.im/mne-tools/mne-gsoc-2019-BIDS?at=5d1a076f2be6a2404d006e33
- continued work on coordinate systems PR: https://github.com/mne-tools/mne-bids/pull/211

Week 5
======

Sunday, 2019-06-30
------------------
- wrote blog post for Python Software Foundation: https://blogs.python-gsoc.org/en/blogs/sappelhoffs-blog/fifth-week-of-gsoc-coordinate-systems-and-transformations/

Saturday, 2019-06-29
--------------------
- enjoyed free time :)

Friday, 2019-06-28
------------------
- prepared a PR in mne-bids to write T1 weighted MRI data and reconstruct `trans`: https://github.com/mne-tools/mne-bids/pull/211

Thursday, 2019-06-27
--------------------
- wrote code to get MRI-landmarks from `trans` and MEG-landmarks: https://github.com/mne-tools/mne-bids/issues/210#issuecomment-506374317
- continued work on docs for source alignment: https://github.com/mne-tools/mne-python/pull/6494

Wednesday, 2019-06-26
---------------------
- prepared a PR to improve MNE-Python docs on coregistration: https://github.com/mne-tools/mne-python/pull/6494
- got stuck on how to extract NAS, LPA, and RPA from NIfTI: https://github.com/mne-tools/mne-bids/issues/210#issuecomment-505853087
- improved `setup.py` of autoreject: https://github.com/autoreject/autoreject/pull/149

Tuesday, 2019-06-25
-------------------
- started to work on a PR that will allow automatic computation of `*.trans` files
- finished PR on auto populating bads in mne-bids: https://github.com/mne-tools/mne-bids/pull/209
- finished work on BIDS-validator MEG update: https://github.com/bids-standard/bids-validator/pull/789
- worked on missing KRISS example: https://github.com/bids-standard/bids-specification/issues/253
- performed the first GSoC evaluation

Monday, 2019-06-24
------------------
- figured out that testing `master` version of `bids-validator` might not be possible under Windows: https://github.com/bids-standard/bids-validator/issues/790#issuecomment-505085605
- overhauled MEG test suite in BIDS-validator: https://github.com/bids-standard/bids-validator/pull/789
- inquired about KRISS MEG data: https://github.com/bids-standard/bids-specification/issues/253
- performed lots of detective work into Unix and Windows flow of the `bids-validator`: https://github.com/bids-standard/bids-validator/issues/790
- repaired and improved Travis CI for mne-bids: Can now easily switch between master and development: https://github.com/mne-tools/mne-bids/pull/209/commits/a7dd5cd5336b70f21c66f50c060c2c937b8f01c2
- learned about `pushd` and `popd`
- Discussion on BIDS-validator with @robertoostenveld and @jasmainak: https://github.com/bids-standard/bids-validator/pull/789#discussion_r296620618
- wrote weekly GSoC blogpost: https://blogs.python-gsoc.org/en/blogs/sappelhoffs-blog/fourth-week-of-gsoc-second-half-of-short-gsoc-pause-due-to-summer-school-and-getting-back-to-work-issues-with-the-bids-validator/


Week 4
======

Sunday, 2019-06-23
------------------
- enjoyed free time :)

Saturday, 2019-06-22
--------------------
- enjoyed free time :)

Friday, 2019-06-21
---------------------
- Opened issue on bids-validator on how to use `master` version with `yarn`: https://github.com/bids-standard/bids-validator/issues/790
- learned about `git bisect`: https://git-scm.com/docs/git-bisect
- Finished up autoreject intuition PR: https://github.com/autoreject/autoreject/pull/147
- Prepared a PR improving the MEG documentation in the BIDS specification: https://github.com/bids-standard/bids-specification/pull/248
- Prepared a PR to allow handling of KIT data with the bids-validator: https://github.com/bids-standard/bids-validator/pull/789
- Continued to work on PR to automatically populate `raw.info['bads']` when reading a raw bids file: https://github.com/mne-tools/mne-bids/pull/209
    - now also fixes an issue with wrong assumptions on `events.tsv` files: https://github.com/mne-tools/mne-bids/issues/202
    - furthermore simplifies `read_raw_bids` by dropping optional event outputs and using `mne.Annotations` instead
- spent some time working on BIDS smaller issues
    - https://github.com/bids-standard/bids-specification/pull/250
    - https://github.com/bids-standard/bids-specification/pull/249

Thursday, 2019-06-20
---------------------
- Prepared an issue on bids-validator to properly check `channels.tsv` files: https://github.com/bids-standard/bids-validator/issues/787
- Prepared a PR to automatically populate `raw.info['bads']` when reading a raw bids file: https://github.com/mne-tools/mne-bids/pull/209

Wednesday, 2019-06-19
---------------------
- concluded summer school: Next day finally back to coding for GSoC!

Tuesday, 2019-06-18
-------------------
- GSoC "sleeps" in favor of organization of summer school, see week 3 in plan: https://blogs.python-gsoc.org/media/proposals/appelhoff_gsoc2019.pdf

Monday, 2019-06-17
------------------
- GSoC "sleeps" in favor of organization of summer school, see week 3 in plan: https://blogs.python-gsoc.org/media/proposals/appelhoff_gsoc2019.pdf

Week 3
======

Sunday, 2019-06-16
------------------
- wrote weekly GSoC blogpost: https://blogs.python-gsoc.org/en/blogs/sappelhoffs-blog/third-week-of-gsoc-conference-discussions-and-short-gsoc-pause-due-to-summer-school/

Saturday, 2019-06-15
--------------------
- enjoyed free time :)

Friday, 2019-06-14
------------------
- GSoC "sleeps" in favor of organization of summer school, see week 3 in plan: https://blogs.python-gsoc.org/media/proposals/appelhoff_gsoc2019.pdf

Thursday, 2019-06-13
---------------------
- GSoC "sleeps" in favor of organization of summer school, see week 3 in plan: https://blogs.python-gsoc.org/media/proposals/appelhoff_gsoc2019.pdf

Wednesday, 2019-06-12
---------------------
- GSoC "sleeps" in favor of organization of summer school, see week 3 in plan: https://blogs.python-gsoc.org/media/proposals/appelhoff_gsoc2019.pdf

Tuesday, 2019-06-11
-------------------
- GSoC "sleeps" in favor of organization of summer school, see week 3 in plan: https://blogs.python-gsoc.org/media/proposals/appelhoff_gsoc2019.pdf

Monday, 2019-06-10
------------------
- partially responsible for BIDS talk 1: https://github.com/ohbm/OpenScienceRoom2019/issues/3
- partially responsible for BIDS talk 2: https://github.com/ohbm/OpenScienceRoom2019/issues/4
- Meeting with `@jasmainak`, `@agramfort` to discuss further steps in GSoC

Week 2
======

Sunday, 2019-06-09
------------------
- OHBM opening
- Met MNE-Python contributors: `@wmvanvliet`, `@jasmainak`, `@agramfort`, `@wmvanvliet`, `@dengemann`
- Met BIDS community, preparations for talks on Monday

Saturday, 2019-06-08
--------------------
- Travelled to OHBM conference 2019: https://www.humanbrainmapping.org/i4a/pages/index.cfm?pageID=3882&activateFull=true
- Met with `@franklin-feingold` to discuss BIDS current issues

Friday, 2019-06-07
------------------
- prepared PR to fix several formatting mistakes in the MNE-Python docs: https://github.com/mne-tools/mne-python/pull/6432
- prepared PR to make mne-study-template more transparent with regards to imports: https://github.com/mne-tools/mne-study-template/pull/34
- went through derivatives specification for BIDS, trying to make somato compliant: https://github.com/bids-standard/bids-specification/pull/207/files#r291560175
- went through mne-study-template codebase and prepared PR to improve docs and formatting: https://github.com/mne-tools/mne-study-template/pull/33
- continued work on: https://github.com/mne-tools/mne-python/pull/6414

Thursday, 2019-06-06
--------------------
- checked out docker tutorial: https://docs.docker.com/get-started/
- continued work on: https://github.com/mne-tools/mne-python/pull/6414
- continued work on: https://github.com/autoreject/autoreject/pull/147
- continued work on: https://github.com/mne-tools/mne-python/pull/6416

Wednesday, 2019-06-05
---------------------
- prepared PR to extend autoreject documentation: https://github.com/autoreject/autoreject/pull/147
- prepared PR to allow raw fif files to end on `_meg.fif` to increase BIDS complicance in MNE-Python: https://github.com/mne-tools/mne-python/pull/6416
- prepared PR to run MNE-Python examples with BIDS somato dataset: https://github.com/mne-tools/mne-python/pull/6414
- looked into `osfclient` to conveniently upload BIDS somato directories to OSF: https://github.com/osfclient/osfclient
- put derivatives for somato dataset into an adequate structure: https://osf.io/pqfu5/?view_only=cc572464105e4c07be15b5c6577aa68d

Tuesday, 2019-06-04
-------------------
- inquired more about the background of somato data: https://gitter.im/mne-tools/mne-gsoc-2019-BIDS?at=5cf6599ff3a60a79a45051a4

Monday, 2019-06-03
------------------
- converted MNE-somato-data to BIDS format: https://osf.io/pqfu5/?view_only=cc572464105e4c07be15b5c6577aa68d
- prepared PR to fix examples about somato dataset in MNE docs: https://github.com/mne-tools/mne-python/pull/6400
- reviewed sensor plot location PR: https://github.com/mne-tools/mne-python/pull/6394

Week 1
======

Sunday, 2019-06-02
------------------
- wrote blog post for Python Software Foundation: https://blogs.python-gsoc.org/en/blogs/sappelhoffs-blog/first-week-of-gsoc-going-down-several-rabbit-holes/
- made plans for upcoming week, see Gitter chat: https://gitter.im/mne-tools/mne-gsoc-2019-BIDS?at=5cf3da6df3a60a79a43f7364

Saturday, 2019-06-01
--------------------
- enjoyed free time :)

Friday, 2019-05-31
------------------
- prepared a PR to sphinx-gallery to fix a keyword: https://github.com/sphinx-gallery/sphinx-gallery/pull/500
- prepared a PR to sphinx-gallery to add viewing sourcecode link to their docs: https://github.com/sphinx-gallery/sphinx-gallery/pull/499
- made an issue on pybv to deal with deprecation of STIM channel in MNE for BrainVision: https://github.com/bids-standard/pybv/issues/24
- prepared PR to speed up caching in pybv: https://github.com/bids-standard/pybv/pull/23
- prepared PR to include Binder links to mne-bids docs: https://github.com/mne-tools/mne-bids/pull/207
- read up on sphinx_gallery to think about how to include "autoreject" intuition, see: https://github.com/autoreject/autoreject/issues/144
- suggested example pipeline draft: https://github.com/sappelhoff/gsoc2019/issues/2
- suggested JSON pipeline API: https://github.com/sappelhoff/gsoc2019/issues/1

Thursday, 2019-05-30
---------------------
- prepared PR to speed up CI for mne-bids: https://github.com/mne-tools/mne-bids/pull/206

Wednesday, 2019-05-29
---------------------
- made gsoc repository: https://github.com/sappelhoff/gsoc2019
- collected ideas for potential pipeline API: link will follow soon (offline for now)

Tuesday, 2019-05-28
-------------------
- opened issue for Python Software Foundation GSoC blog, editing not possible: https://github.com/python-gsoc/python-blogs/issues/182
- wrote blog post: https://blogs.python-gsoc.org/en/blogs/sappelhoffs-blog/google-summer-of-code-gsoc-2019-analysis-pipelines-and-bids/
- prepared PR to improve CI for mne-study-template: https://github.com/mne-tools/mne-study-template/pull/31
- forked mne-study-template repository to check where BIDS could ease the flow: https://github.com/mne-tools/mne-study-template
- continued work on "intuition" issue: https://github.com/autoreject/autoreject/issues/144
- did some detective work on background of `somato` dataset, found potential origin: http://cobre.mrn.org/megsim/
- addressed comments for PR, now ready to merge: https://github.com/autoreject/autoreject/pull/143
- prepared PR to fix autoreject CIs: https://github.com/autoreject/autoreject/pull/145

Monday, 2019-05-27
------------------
- opened ISSUE to discuss potential "intuition" for autoreject: https://github.com/autoreject/autoreject/issues/144
- prepared PR to improve autoreject docs: https://github.com/autoreject/autoreject/pull/143
- read autoreject publication: https://doi.org/10.1016/j.neuroimage.2017.06.030
- prepared PR to add/fix BIDS links in docs: https://github.com/mne-tools/mne-python/pull/6376
- reviewed PR on docs about annotations/events: https://github.com/mne-tools/mne-python/pull/6358
