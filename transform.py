#!/usr/bin/env python

import jinja2

with open('index.html.jinja') as f:
    template = jinja2.Template(f.read())

with open('index.html', 'w') as f:
    f.write(template.render())
