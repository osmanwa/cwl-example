# cwl-example

This repo utilizes cwl and python to sort a bam, or list of bams.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install cwltool.
Also make sure you have docker installed.

```bash
pip install cwltool
```

## Usage
from the commandline:
```cwltool bam.cwl bam.inputs.yml```

If you would like to submit a batch of bams, create a list of paths execute the following:

```python
from cwl_submitter import CwlSubmitter

CwlSubmitter('bam.cwl', 'bam.inputs.yml', 'bams_list.txt').loop_and_execute()
```
For bams to test:

https://www.ebi.ac.uk/arrayexpress/experiments/E-GEUV-1/files/processed/

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
