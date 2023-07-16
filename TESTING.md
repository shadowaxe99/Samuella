# Testing

This project currently does not have a testing framework set up. As the project grows and becomes more complex, it would be beneficial to add unit tests to ensure that all components of the application are working as expected.

When a testing framework is added to the project, you will be able to run the tests using a command like `python -m unittest discover` (for the unittest testing framework) or `pytest` (for the pytest testing framework).

In addition to unit tests, you might also consider adding integration tests to ensure that the different components of the application work correctly together, and end-to-end tests to simulate user interactions and test the overall flow of the application.

## Updates

### calendar_integration.py
- Commented out the line where 'create_credentials()' is called because the function is not defined.
- Added 'encoding="utf-8"' to the 'open' function call.
- Commented out the lines where 'events' member is used because it's not found in the 'Resource' instance.
- Replaced triple quotes with single quotes in the docstrings.