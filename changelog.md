Week 4
======

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
