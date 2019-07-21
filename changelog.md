Week 9
======

Sunday, 2019-07-28
------------------

Saturday, 2019-07-27
--------------------

Friday, 2019-07-26
------------------

Thursday, 2019-07-25
--------------------

Wednesday, 2019-07-24
---------------------


Tuesday, 2019-07-23
-------------------

Monday, 2019-07-22
------------------

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
  - homogenize use of `output_path` and `bids_root`: https://github.com/mne-tools/mne-bids/issues/213
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
