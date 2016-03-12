parser
======

Usage:
------
    tail -f /var/log/service.log | parse
    tail -f /var/log/service.log | parse --format template.j2
    tail -f /var/log/service.log | parse --filter @fields.level=ERROR

Options:
--------
    --format    Tels parser to use given file as output template
    --filter    Filters input lines by given fields value

Default output:
---------------
    [@timestamp] @fields.level @message

Example:
--------
    tail -f /var/log/service.log | json-log
    [2015-12-15T05:45:39+00:00] INFO Request processed
