# md-parser

A Markdown parser using Docker and Nginx

## Usage

Move to directory which contains Markdown (.md) file, then execute command below.

```
$ docker run -d -p 80:80 -v $(pwd):/tmp k2morita/md-parser
```

After container starts, access following URLs with browser.

* HTML  
    http://localhost
* PDF  
    http://localhost/?pdf
