# Selenium-Python-Boilerplate (Under development)

This is a boilerplate for running selenium tests with python and includes the bare minimum. It includes unittests for both firefox, phantomjs and examples on how to work with sensitive data using environment variables.

Implementing this in existing project is easy, just create clone this repro into a folder called selenium (or whaterver) and get going.


## Getting started

This boilerplate requires both selenium, nose and python-dotenv, you can install them by doing the following.

1. `virtualenv venv`
2. `source venv/bin/activate`
3. `pip install -r requirements.txt`


### Drivers

This boilerplate includes both PhantomJS and Firefox examples.

- Phantomjs: (OSX) `brew install phantomjs`
- Firefox: Download from https://firefox.com


### Environment values

Create a .env file (this will be kept outside version control): `cp example.env .env`


## Running

You can run the tests by typing: `python runtests.py`

To run a specific case: `python runtests.py tests.test_firefox:TestFirefox`


## Contributing

Want to contribute? Awesome. Just send a pull request.


## License

Selenium-Python-Boilerplate is released under the [MIT License](http://www.opensource.org/licenses/MIT).
