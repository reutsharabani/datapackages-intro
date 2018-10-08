# Datapackages Intro

This is a minimal pipeline implementation as recommended here: https://raw.githubusercontent.com/frictionlessdata/datapackage-pipelines/master/README.md

## Running

To run the project you need python 3.6 or higher.
You should probably work with [conda](https://conda.io/docs/)/[virtualenv](https://virtualenv.pypa.io/en/stable/) but that is up to you.

Clone the repository

```sh
git clone https://github.com/reutsharabani/datapackages-intro.git
```

Install dependencies
```sh
pip install -r requirements.txt # or `make install-dependencies`
```

Now that you have datapackacges-piplines installed, run the pipeline using:

```sh
dpp run ./intro/pipelines/youtube-first-page
```
