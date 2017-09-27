# Roll

A digital, d-whatever dice roller.

Accepts "dice shorthand", `QdS`, where `Q` is the quantity of dice, and `S` is
the number of sides.
For example, `2d12` will generate `2` random numbers between 1 and `12`

This utility does not restrict users to standard-sided dice, meaning you can
easily roll percentages (`1d100`) or weird-sided dice (`32d17`, in case you felt
the need to roll `32` `17`-sided dice...)

## Setup
1. Install dependencies with [pip]:
    ```sh
    $ pip install -r requirements.txt
    ```
1. Set the value of `SLACK_TOKEN` in `app.py` to be some string. Currently used
as a terrible form of validation.

## Usage

Roll is currently set up to deploy as an AWS Lambda with API Gateway, using
[Chalice]
1. Run locally:
    ```sh
    $ chalice local
    ```
1. POST to the running app, with a `Header` including
`Content-Type: application/x-www-form-urlencoded` and the following data:

*key* | *value description*
 --- | ---
token | Some token used to poorly validate the source of the request. This value should match what you've set during [Setup] **NOTE:** This will change in the future.
text | some dice shorthand (described above)

[//]: # (External Links)
[pip]: https://pypi.python.org/pypi/pip
[Chalice]: https://github.com/aws/chalice

[//]: # (Internal Links)
[Setup]: #setup