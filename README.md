##  jsonparser
Console utility takes data from stdin and prints them line by line to the stdout with formatted form.
You can use [jinja2](http://jinja.pocoo.org/docs/dev/) as template engine to customise output.

###  Usage:
```
$ tail -f /var/log/service.log | jsonparser
$ tail -f /var/log/service.log | jsonparser --format template.j2
$ tail -f /var/log/service.log | jsonparser --filter @fields.level=ERROR
```

###  Default output:
```
[@timestamp] @fields.level @message
```

###  Example:
```
$ tail -f /var/log/service.log | jsonparser
[2015-12-15T05:45:39+00:00] INFO Request processed
```
