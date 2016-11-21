# StubHubScraper
StubhubScraper is a ticket scaper for StubHub events to track ticket pricing trends over time.

## Getting Started
Clone the project to your local machine. 

### Prerequisites

Python dependencies for StubHubScraper

```
import requests
import sqlite3
import time
import json
import base64
import config
```

## Configuration

Create a config.py file in your project root directory with the following information

```
StubHub = dict(
    consumer_key = '**stubhub_consumer_key**',
    consumer_secret = '**stubhub_consumer_secret**',
    stubhub_username = '**stubhub_username**',
    stubhub_password = '**stubhub_password**',
)
```

## Event Tracking

Determine the event that you would like to track ticket price history with and edit the following in StubHubScraper.py

* Event title in handleResponse function
```
event = '**StubHub event title**'
```

* Event ID in main method (can be found in URL of a StubHub event)
```
eventid = '**StubHub event ID**'
```

## Built With

* [StubHub API](https://developer.stubhub.com/store/) - InventorySearchAPIv2 to search ticket listings for events

## Authors

* **Jackson Cheek** - [jacksoncheek](https://github.com/jacksoncheek)

## License

This project is licensed under the MIT License.

MIT License

Copyright (c) 2016 Jackson Cheek

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

