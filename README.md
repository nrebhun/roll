# Roll

A digital, d-whatever dice roller.

Accepts "dice shorthand", `QdS`, where `Q` is the quantity of dice, and `S` is
the number of sides.
For example, `2d12` will generate `2` random numbers between 1 and `12`

This utility does not restrict users to standard-sided dice, meaning you can
easily roll percentages (`1d100`) or weird-sided dice (`32d17`, you know... in case you felt
the need to roll `32` `17`-sided dice...)

## Setup
1. Install dependencies with [pip]:
    ```sh
    $ pip install -r requirements.txt
    ```
1. Set the value of `"SLACK_TOKEN"` in `.chalice/config.json` to be some string.
Upon deployment, [Chalice] will set up your slack token as a lambda-accessible environment variable.

## Usage

Roll is currently set up to deploy as an AWS Lambda with API Gateway, using [Chalice].

#### To deploy this project on your own AWS account:
1. Set up your local environment with an [AWS config and corresponding credentials].
###### **Note:** in my opinion, the official docs I've linked above aren't particularly friendly to newer AWS users, but they're comprehensive, updated regularly, and appear to be improving over time.

2. Deploy:
    ```sh
    $ chalice deploy
    ```

#### Alternatively, run locally

1. Serve:
    ```sh
    $ chalice local
    ```
2. POST to the running app using `curl` or [Postman] or whatever, with a `Header` including
`Content-Type: application/x-www-form-urlencoded` and the following `Body` data:

*key* | *value description*
 --- | ---
token | Some token used to poorly validate the source of the request. This value should match what you've set during [Setup] **NOTE:** This will change in the future.
text | some dice shorthand (described above)

[//]: # (External Links)
[pip]: https://pypi.python.org/pypi/pip
[Chalice]: https://github.com/aws/chalice
[Postman]: https://www.getpostman.com
[AWS config and corresponding credentials]: https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html

[//]: # (Internal Links)
[Setup]: #setup
