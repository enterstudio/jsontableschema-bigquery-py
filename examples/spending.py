# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

import sys
from pprint import pprint

sys.path.insert(0, '.')
from examples.base import run


# Fixtures
dataset = 'jsontableschema'
prefix = 'test_'
table = 'test_%s_%s' % (sys.version_info.major, sys.version_info.minor)
schema = {
    'fields': [
        {
            'name': 'id',
            'type': 'string',
        },
        {
            'name': 'parent',
            'type': 'string',
        },
        {
            'name': 'name',
            'type': 'string',
        },
        {
            'name': 'current',
            'type': 'boolean',
        },
        {
            'name': 'amount',
            'type': 'number',
        },
    ],
}
data = [
    ('A3001', 'A3001', 'Taxes', True, 10000.5),
    ('A5032', 'A3001', 'Parking Fees', False, 2000.5),
]


# Execution
if __name__ == '__main__':
    pprint(run(dataset, prefix, table, schema, data))
