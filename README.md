# nomad-parser-msspec-plugin
Standalone NOMAD plugin for parsing MsSpec calculation files

## Developing the parser

Clone the parser-plugin project and enter the folder
```
git clone https://github.com/nomad-coe/nomad-parser-plugin-msspec.git nomad-parser-plugin-msspec
cd nomad-parser-plugin-msspec
```

Create a virtual environment (preferably using Python 3.9):

```
pip install virtualenv
virtualenv -p `which python3` .pyenv
source .pyenv/bin/activate
```

Install NOMAD's pypi package and the parser-plugin in development mode:

```
pip install nomad-lab
pip install -e .
```

You can debug now the calculations from the parser-plugin.

## Using the parser

You can use NOMAD's parsers and normalizers locally on your computer. You need to install
NOMAD's pypi package (if you didn't do it already)

```
pip install nomad-lab
```

To parse code input/output from the command line, you can use NOMAD's command line
interface (CLI) and print the processing results output to stdout:

```
nomad parse --show-archive <path-to-file>
```

To parse a file in Python, you can program something like this:
```python
import sys
from nomad.cli.parse import parse, normalize_all

# match and run the parser
archive = parse(sys.argv[1])
# run all normalizers
normalize_all(archive)

# get the 'main section' section_run as a metainfo object
section_run = archive.section_run[0]

# get the same data as JSON serializable Python dict
python_dict = section_run.m_to_dict()
```
