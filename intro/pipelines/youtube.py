#!/usr/bin/env python
from datetime import timedelta
from itertools import chain

import requests
from bs4 import BeautifulSoup
from datapackage_pipelines.utilities.resources import PROP_STREAMING
from datapackage_pipelines.wrapper import ingest, spew


# in this part we grab the parameters from the metadata, datapackage metadata
# and the results for the datapackage metadata
parameters, datapackage, res_iter = ingest()

DURATION_TEXT_PREFIX = ' - Duration: '


def get_title(item):
    return item.h3.a['title']


def get_duration(item):
    try:
        duration_string = item.h3.span.text[len(DURATION_TEXT_PREFIX):-1]
        return duration_string
    except AttributeError:
        # None signals "no value for this field"
        return None


duration_format = 'HH:MM:SS'


def format_duration(raw_duration):
    if not raw_duration:
        return None
    parts = raw_duration.split(':')
    # pad most significant part (no leading zero in youtube format
    parts[0] = ('0' + parts[0])[-2:]
    result = ':'.join(parts)

    # make sure we have all format parts
    candidate_prefix = '00:00:' + result
    return candidate_prefix[-len(duration_format):]


def parse_item(item):
    return {
        # this is a simple field, it simply forwards a string extracted using bs4
        'title': get_title(item),
        # this is a bit more complex, it requires some formatting
        'duration': format_duration(get_duration(item)),
    }


def scrape_youtube_first_page():
    raw = requests.get('https://youtube.com').content
    html = BeautifulSoup(raw)
    raw_items = html.select('div.yt-lockup-content')
    for item in map(parse_item, raw_items):
        # this is where we actually generate results for the pipeline
        yield item


datapackage['resources'].append(
    {
        PROP_STREAMING: True,
        'name': 'youtube_results',
        'title': 'First page of youtube',
        # output will be written to this file (under `/output`, after `dump.to_path`).
        'path': 'test.csv',
        'schema': {
            'fields': [
                {'name': 'title', 'type': 'string'},
                # time is a parsed field that uses internal parsing (see extended_json.TIME_FORMAT)
                # we can change this format by adding the `format` field
                {'name': 'duration', 'type': 'time'},
            ]
        }
    }
)

# this extends out work so far
# results from previous step are in `res_iter`
# results generated here by `scrape_youtube_first_page`
# it is meaningless here, since we only set metadata in the previous step, but makes the pipeline extensible
# in the sense that if the previous step is generating data this step will "extend" it automagically and
# no changes should be required (because we `chain` whatever we already had)
spew(datapackage, chain(res_iter, [scrape_youtube_first_page()]))
