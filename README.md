# Datapackages Intro

This is a minimal pipeline implementation for [datapackage-pipelines](https://github.com/frictionlessdata/datapackage-pipelines) as recommended by the tutorial.

## Running

To run the project you need python 3.6 or higher.
You should probably work with [conda](https://conda.io/docs/)/[virtualenv](https://virtualenv.pypa.io/en/stable/) but that is up to you.

Clone the repository

```sh
git clone https://github.com/reutsharabani/datapackages-intro.git
```

Change directory to the project directory and install dependencies
```sh
cd datapackages-intro
pip install -r requirements.txt # or `make install-dependencies`
```

Now that you have datapackacges-piplines installed, run the pipeline using:

```sh
dpp run ./intro/pipelines/youtube-first-page
```

And you should get output similar to this:

> INFO    :RESULTS:
>
> INFO    :SUCCESS: ./intro/pipelines/youtube-first-page {'bytes': 8025, 'count_of_rows': 101, 'dataset_name': 'youtube-first-page', 'hash': '07b6eb584d70905e8a1412c541b56258'}

If you encountered any problems its best to report to the datapackage-pipelines [issue tracking](https://github.com/frictionlessdata/datapackage-pipelines/issues), but if it is a problem with this repository please open an issue/PR [here](https://github.com/reutsharabani/datapackages-intro/issues).
