# Mixpeek

Mixpeek let's you run full-text-search on your files

**Stuff you might be looking for**:
 - [Installing Mixpeek](https://github.com/mixpeek/mixpeek-python#installation)
 - [Integrations](https://github.com/mixpeek/mixpeek-python#integrations)
 - [Bugs & Questions](https://github.com/mixpeek/mixpeek-python#bugs-&-questions)


## Quickstart

Upload any image filetype for text extraction

```python
from mixpeek import Mixpeek

mix = Mixpeek(
    api_key="my-api-key"
)

mix.upload(file_name="website_screenshot.png", file_path="desktop/username/tmp/website_screenshot.png")
```

...or any audio filetype

```python
mix.upload(file_name="never_gonna_give_you_up.mp3", file_path="desktop/username/tmp/never_gonna_give_you_up.mp3")
```

... or a pdf, or doc, or [anything else tika supports](https://tika.apache.org/0.9/formats.html)

```python
pdf_version = mix.upload(file_name="some_document.pdf", file_path="desktop/username/tmp/some_document.pdf")
doc_version = mix.upload(file_name="some_document.doc", file_path="desktop/username/tmp/some_document.doc")
html_version = mix.upload(file_name="some_document.html", file_path="desktop/username/tmp/some_document.html")
```

The API will return some information including the extracted text:

```python
{
    "code": 200,
    "endpoint": "/upload",
    "ok": True,
    "response": {
        "_id": "615e71fd47d7df57aeb93c27",
        "api_key": "your_api_key",
        "corpus": "Never gonna give you up. Never gonna let you down. Never gonna run around and desert you.",
        "metadata": {
            "date_inserted": "2021-10-07 04:05:17.942499",
            "filename": "never_gonna_give_you_up.mp3"
            "file_url": "desktop/username/tmp/never_gonna_give_you_up.mp3"
        }
    },
    "timestamp": 1633579517.955764
}
```

Search for file contents:

```python
query = mix.search(query="let you down")

print(query)

[
    {
        "_id": "615e71fd47d7df57aeb93c27",
        "api_key": "REDACTED",
        "highlights": [
            {
                "score": 0.8759502172470093,
                "texts": [
                    {
                        "type": "text",
                        "value": "Never gonna give you up. Never gonna "
                    },
                    {
                        "type": "hit",
                        "value": "let you down"
                    },
                    {
                        "type": "text",
                        "value": ". Never gonna run around and desert you."
                    }
                ]
            }
        ],
        "metadata": {
            "date_inserted": "2021-10-07 04:05:17.942499",
            "filename": "never_gonna_give_you_up.mp3"
            "file_url": "desktop/username/tmp/never_gonna_give_you_up.mp3"            
        },
        "score": 0.13313256204128265
    }
]

```


## Installation

Installing mixpeek is easy

```shell
pip install git+https://github.com/mixpeek/mixpeek-python.git@master
```


## Integrations


S3

```python
from mixpeek import S3
from config import mixpeek_api_key, aws

s3 = S3(
    aws_access_key_id=aws['aws_access_key_id'],
    aws_secret_access_key=aws['aws_secret_access_key'],
    region_name='us-east-2',
    mixpeek_api_key=mixpeek_api_key
)
# upload all files in a bucket
s3.upload_all(bucket_name="demo-bucket")

# upload one single file in a bucket
s3.upload_one(s3_file_name="never_gonna_give_you_up.mp3", bucket_name="demo-bucket")
```


## Bugs & Questions

You can file bugs in our [github issues tracker](https://github.com/mixpeek/mixpeek-python/issues),
and ask any technical questions on
[Stack Overflow using the mixpeek tag](http://stackoverflow.com/questions/ask?tags=mixpeek).
We keep an eye on both.


## 🚀 Features

- Supports for `Python 3.8` and higher.
- Full text search
- AWS S3 Integration
- Fuzzy text matching


## Articles:

- [Add search to your S3 bucket’s non-text files](https://medium.com/@mixpeek/add-search-to-your-s3-buckets-non-text-files-9a676452b4fd)


## License ([MIT License](http://opensource.org/licenses/mit-license.php))

Copyright © 2022 Mixpeek, https://mixpeek.com

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
