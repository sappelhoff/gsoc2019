"""Download the eeg_matchingpennies dataset.

The full data is available on the Open Science Framework (OSF) under the
following URL: https://osf.io/cj2dr/

This Python script provides a fetching function that can be used to download
parts or the entire dataset.

Usage
-----
- Call the script from the command line to download the full data to
  ~/mne_data/mne_bids_examples/eeg_matchingpennies
- ... or import the `fetch_matchingpennies` function and make use of the
  input parameters for more specific use.

Dependencies
------------
- Python >= 3.6
- MNE-Python
- MNE-BIDS

Installation
------------
- Simply follow the installation instructions for MNE-BIDS to satisfy all
  software dependencies:
  https://github.com/mne-tools/mne-bids/blob/master/README.rst#installation

Notes
-----
- The data is also available as a git-annex repository under:
  https://github.com/sappelhoff/eeg_matchingpennies
- See this blogpost to learn more about the conversion to a git-annex
  repository:
  https://blogs.python-gsoc.org/en/sappelhoffs-blog/tenth-week-of-gsoc-git-annex-and-datalad/

Citation
--------
- If you use this dataset, please cite the following reference:
  Appelhoff, S., Sauer, D., & Gill, S. S. (2018, July 22). Matching Pennies: A
  Brain Computer Interface Implementation Dataset.
  https://doi.org/10.17605/OSF.IO/CJ2DR

"""
# Authors: Stefan Appelhoff <stefan.appelhoff@mailbox.org>
#
# License: BSD (3-clause)
import os
import os.path as op

from mne.utils import _fetch_file
from mne_bids import make_bids_basename, make_bids_folders


def _download_data(data, overwrite, verbose, dry=False):
    """Iterate over `data`, a dict with fpath, url and download."""
    for fpath, url in data.items():
        if dry:
            print(fpath, url)
            continue
        if op.exists(fpath) and not overwrite:
            continue
        _fetch_file(url=url, file_name=fpath, print_destination=verbose,
                    resume=True, timeout=10., verbose=verbose)


def fetch_matchingpennies(data_path=None, subjects=None, dataset_data=True,
                          sourcedata=False, overwrite=False, verbose=True,
                          dry=False):
    """Fetch the eeg_matchingpennies dataset [1]_.

    Parameters
    ----------
    data_path : str
        Path to a directory into which to place the "eeg_matchingpennies"
        directory. Defaults to "~/mne_data/mne_bids_examples"
    subjects : list of str | None
        The subject identifiers to download data from. Subjects identifiers
        that are invalid will be ignored. Defaults to downloading from all
        subjects. Specify an empty list to not download any subject data.
    dataset_data : bool
        If True, download the dataset metadata. Defaults to True.
    sourcedata : bool
        If True, download the "/sourcedata" directory containing the original
        .xdf files. Defaults to False
    overwrite : bool
        Whether or not to overwrite data. Defaults to False.
    verbose : bool
        Whether or not to print output. Defaults to True.
    dry : bool
        If True, will only print filepaths and urls instead of downloading.

    Returns
    -------
    data_path : str
        The path to the eeg_matchingpennies dataset.

    References
    ----------
    .. [1] Appelhoff, S., Sauer, D., & Gill, S. S. (2018, July 22). Matching
           Pennies: A Brain Computer Interface Implementation Dataset.
           https://doi.org/10.17605/OSF.IO/CJ2DR

    """
    if data_path is None:  # pragma: no cover
        data_path = op.join(op.expanduser('~'), 'mne_data',
                            'mne_bids_examples')
    data_path = op.join(data_path, 'eeg_matchingpennies')
    os.makedirs(data_path, exist_ok=True)

    if not isinstance(subjects, (list, tuple, type(None))):
        raise ValueError('Specify `subjects` as a list of str, or None.')
    if subjects is None:  # pragma: no cover
        subjects = ['{:02}'.format(ii) for ii in range(5, 12)]

    task = 'matchingpennies'
    base_url = 'https://osf.io/{}/download'

    # suffixes of files per subject
    file_suffixes = ('channels.tsv', 'eeg.eeg', 'eeg.vhdr', 'eeg.vmrk',
                     'events.tsv', 'eeg.xdf')
    # Mapping subjects to the identifier url suffixes
    file_key_map = {
        '05': ('wdb42', '3at5h', '3m8et', '7gq4s', '9q8r2', 'agj2q'),
        '06': ('256sk', 'p52dn', 'jk649', 'wdjk9', '5br27', 'rj3nf'),
        '07': ('qvze6', 'z792x', '2an4r', 'u7v2g', 'uyhtd', 'aqesz'),
        '08': ('4safg', 'dg9b4', 'w6kn2', 'mrkag', 'u76fs', '6t5vg'),
        '09': ('nqjfm', '6m5ez', 'btv7d', 'daz4f', 'ue7ah', '59zde'),
        '10': ('5cfmh', 'ya8kr', 'he3c2', 'bw6fp', 'r5ydt', 'gfsnv'),
        '11': ('6p8vr', 'ywnpg', 'p7xk2', '8u5fm', 'rjzhy', '4m3g5'),
                    }

    # Download subject data and optionally sourcedata for subjects
    for subject in subjects:  # pragma: no cover
        file_keys = file_key_map.get(subject, None)

        # If wrong subject, do not attempt to download
        if file_keys is None:
            continue

        bids_sub_dir = make_bids_folders(subject, kind='eeg',
                                         output_path=data_path,
                                         make_dir=True, verbose=verbose,
                                         overwrite=overwrite)

        # Compile download data
        data = dict()
        for suffix, key in zip(file_suffixes, file_keys):
            fname = make_bids_basename(subject=subject, task=task,
                                       suffix=suffix)
            fpath = op.join(bids_sub_dir, fname)

            # If this is the xdf sourcedata, only download if asked for
            # and always place in "/sourcedata" directory
            if suffix.endswith('.xdf'):
                if not sourcedata:
                    continue
                else:
                    fpath = fpath.replace(data_path,
                                          op.join(data_path, 'sourcedata'))

            data[fpath] = base_url.format(key)

        # Download
        _download_data(data, overwrite, verbose, dry)

    # If requested, download general data
    if dataset_data:
        os.makedirs(op.join(data_path, 'stimuli'), exist_ok=True)
        file_key_map = {
            '.bidsignore': '6thgf',
            'CHANGES': 'ckmbf',
            'dataset_description.json': 'tsy4c',
            'LICENSE': 'mkhd4',
            'participants.tsv': '6mceu',
            'participants.json': 'ku2dn',
            'README': 'k8hjf',
            'task-matchingpennies_eeg.json': 'qf5d8',
            'task-matchingpennies_events.json': '3qztv',
            'stimuli{}left_hand.png'.format(os.sep): 'g45de',
            'stimuli{}right_hand.png'.format(os.sep): '2r9zd',
        }
        # Compile data
        data = dict()
        for fname, key in file_key_map.items():
            fpath = op.join(data_path, fname)
            data[fpath] = base_url.format(key)

        # Download
        _download_data(data, overwrite, verbose, dry)

    return data_path


if __name__ == '__main__':
    data_path = fetch_matchingpennies()
    print('Downloaded eeg_matchingpennies to "{}"'.format(data_path))
