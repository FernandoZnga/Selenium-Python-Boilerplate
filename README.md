# Selenium-Python-Boilerplate (Under development)

This is a boilerplate for running selenium tests with python and includes the bare minimum, examples includes unittests for both firefox and phantomjs.

Implementing this in existing project is easy, just create clone this repro into a folder called selenium (or whaterver) and get going.


## Getting started

This boilerplate requires both selenium and nose, you can install them by doing the following.

1. `virtualenv venv`
2. `source venv/bin/activate`
3. `pip install -r requirements.txt`


### Drivers

This boilerplate includes both PhantomJS and Firefox examples.

- Phantomjs: `brew install phantomjs`
- Firefox: https://firefox.com


## Running

You can run the tests by typing: `nosetests`


## Contributing

Want to contribute? Awesome. Just send a pull request.


## License

Selenium-Python-Boilerplate is released under the [MIT License](http://www.opensource.org/licenses/MIT).
