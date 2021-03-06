<!--
<p align="center">
  <img src="https://github.com/cthoyt/fairsharing-client/raw/main/docs/source/logo.png" height="150">
</p>
-->

<h1 align="center">
  FAIRsharing Client
</h1>

<p align="center">
    <a href="https://github.com/cthoyt/fairsharing-client/actions?query=workflow%3ATests">
        <img alt="Tests" src="https://github.com/cthoyt/fairsharing-client/workflows/Tests/badge.svg" />
    </a>
    <a href="https://pypi.org/project/fairsharing_client">
        <img alt="PyPI" src="https://img.shields.io/pypi/v/fairsharing_client" />
    </a>
    <a href="https://pypi.org/project/fairsharing_client">
        <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/fairsharing_client" />
    </a>
    <a href="https://github.com/cthoyt/fairsharing-client/blob/main/LICENSE">
        <img alt="PyPI - License" src="https://img.shields.io/pypi/l/fairsharing_client" />
    </a>
    <a href='https://fairsharing-client.readthedocs.io/en/latest/?badge=latest'>
        <img src='https://readthedocs.org/projects/fairsharing-client/badge/?version=latest' alt='Documentation Status' />
    </a>
    <a href="https://codecov.io/gh/cthoyt/fairsharing-client/branch/main">
        <img src="https://codecov.io/gh/cthoyt/fairsharing-client/branch/main/graph/badge.svg" alt="Codecov status" />
    </a>  
    <a href="https://github.com/cthoyt/cookiecutter-python-package">
        <img alt="Cookiecutter template from @cthoyt" src="https://img.shields.io/badge/Cookiecutter-snekpack-blue" /> 
    </a>
    <a href='https://github.com/psf/black'>
        <img src='https://img.shields.io/badge/code%20style-black-000000.svg' alt='Code style: black' />
    </a>
    <a href="https://github.com/cthoyt/fairsharing-client/blob/main/.github/CODE_OF_CONDUCT.md">
        <img src="https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg" alt="Contributor Covenant"/>
    </a>
</p>

A client to the [FAIRsharing API](https://beta.fairsharing.org/API_doc).

## 💪 Getting Started

FAIRsharing is a registry of high-quality metadata about standards, databases,
and policies. However, there are two aspects to FAIRsharing's data that make it
difficult to use:

1. It's licensed under the restrictive [CC-BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license (
   see https://fairsharing.org/licence). This makes it difficult to redistribute
   the data, even in part. Better options for community reuse are [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/) or
   ideally [CC0](https://creativecommons.org/share-your-work/public-domain/cc0/). However, keep in mind that FAIR and Open are emphatically
   [not the same thing](https://www.go-fair.org/resources/faq/ask-question-difference-fair-data-open-data/).
2. Instead of offering a bulk download, there is an API that requires
   authentication using [JWT](https://jwt.io).

While there's nothing wrong with JWT, it requires several steps that make
programmatic access inconvenient for less seasoned programmers.
The `fairsharing_client` package provides a way to automatically bulk download
all contents from the API and store them locally in a reproducible way, so you
can write code that relies on FAIRsharing data without having to worry about how
to interact with its API nor redistribute its data yourself. Further,
this package does some preprocessing on the content to make it more useful.

```python
import fairsharing_client as fc

# Download the data and return the path of the YAML file
# This takes about 4 minutes and gets around 4K records.
path = fc.ensure_fairsharing()

# Download the data and open it for use
data = fc.load_fairsharing() 

# Get data for a given record
chebi_record = data["FAIRsharing.62qk8w"]
```

There are a few ways to do authentication:

1. **Envionment Variables**: set the `FAIRSHARING_LOGIN`
   and `FAIRSHARING_PASSWORD` envionrment variables
2. **Configuration**: in the `~/.config/fairshairing.ini` file, add the
   following configuration:
   ```ini
   [fairsharing]
   login = cthoyt@gmail.com
   password = ...
   ```
3. **Keyword arguments**: pass the `login` and `password` keywords to either of
   the example functions.

A reminder: this repository does NOT redistribute FAIRsharing's data, it only
provides code for you to get it yourself.

## 🚀 Installation

The most recent release can be installed from
[PyPI](https://pypi.org/project/fairsharing_client/) with:

```bash
$ pip install fairsharing_client
```

The most recent code and data can be installed directly from GitHub with:

```bash
$ pip install git+https://github.com/cthoyt/fairsharing-client.git
```

## 👐 Contributing

Contributions, whether filing an issue, making a pull request, or forking, are
appreciated. See
[CONTRIBUTING.md](https://github.com/cthoyt/fairsharing-client/blob/master/.github/CONTRIBUTING.md)
for more information on getting involved.

## 👋 Attribution

### ⚖️ License

The code in this package is licensed under the MIT License.

### 🍪 Cookiecutter

This package was created
with [@audreyfeldroy](https://github.com/audreyfeldroy)'s
[cookiecutter](https://github.com/cookiecutter/cookiecutter) package
using [@cthoyt](https://github.com/cthoyt)'s
[cookiecutter-snekpack](https://github.com/cthoyt/cookiecutter-snekpack)
template.

## 🛠️ For Developers

<details>
  <summary>See developer instructions</summary>


The final section of the README is for if you want to get involved by making a
code contribution.

### Development Installation

To install in development mode, use the following:

```bash
$ git clone git+https://github.com/cthoyt/fairsharing-client.git
$ cd fairsharing-client
$ pip install -e .
```

### 🥼 Testing

After cloning the repository and installing `tox` with `pip install tox`, the
unit tests in the `tests/` folder can be run reproducibly with:

```shell
$ tox
```

Additionally, these tests are automatically re-run with each commit in
a [GitHub Action](https://github.com/cthoyt/fairsharing-client/actions?query=workflow%3ATests)
.

### 📖 Building the Documentation

The documentation can be built locally using the following:

```shell
$ git clone git+https://github.com/cthoyt/fairsharing-client.git
$ cd fairsharing-client
$ tox -e docs
$ open docs/build/html/index.html
``` 

The documentation automatically installs the package as well as the `docs`
extra specified in the [`setup.cfg`](setup.cfg). `sphinx` plugins like `texext`
can be added there. Additionally, they need to be added to the
`extensions` list in [`docs/source/conf.py`](docs/source/conf.py).

### 📦 Making a Release

After installing the package in development mode and installing
`tox` with `pip install tox`, the commands for making a new release are
contained within the `finish` environment in `tox.ini`. Run the following from
the shell:

```shell
$ tox -e finish
```

This script does the following:

1. Uses [Bump2Version](https://github.com/c4urself/bump2version) to switch the
   version number in the `setup.cfg`,
   `src/fairsharing_client/version.py`,
   and [`docs/source/conf.py`](docs/source/conf.py) to not have the `-dev`
   suffix
2. Packages the code in both a tar archive and a wheel
   using [`build`](https://github.com/pypa/build)
3. Uploads to PyPI using [`twine`](https://github.com/pypa/twine). Be sure to
   have a `.pypirc` file configured to avoid the need for manual input at this
   step
4. Push to GitHub. You'll need to make a release going with the commit where the
   version was bumped.
5. Bump the version to the next patch. If you made big changes and want to bump
   the version by minor, you can use `tox -e bumpversion minor` after.

</details>
