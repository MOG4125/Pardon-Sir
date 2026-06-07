# pardon_sir

[![PyPI version](https://shields.io)](https://pypi.org)
[![Python versions](https://shields.io)](https://pypi.org)
[![License: MIT](https://shields.io)](https://opensource.org)

A lightweight CLI tool to write natural multi-line or single-line comments in YAML using the `£` symbol. It scans your directory and instantly outputs valid, production-ready standard `#` YAML configurations.

## How it Works

Standard YAML parsers reject block comments. `pardon_sir` allows you to write natural line-by-line comments using `£`, then automatically converts them to valid `#` comments while carefully protecting actual financial numbers (like `"£10.99"`).

### Custom Input File
```yaml
£ PRODUCTION ENVIRONMENT CONFIG
£ Maintained by the DevOps team.
server:
  host: 127.0.0.1
  port: 8080 £ inline reminder
  price_tag: "£50.00" £ Currency symbol is perfectly safe inside text!
```

### Processed Valid Output
```yaml
# PRODUCTION ENVIRONMENT CONFIG
# Maintained by the DevOps team.
server:
  host: 127.0.0.1
  port: 8080 # inline reminder
  price_tag: "£50.00" # Currency symbol is perfectly safe inside text!
```

## Installation

Install `pardon_sir` via your preferred package manager:

```bash
# Using pip
pip install pardon_sir

# Using uv
uv tool install pardon_sir

# Using poetry
poetry add pardon_sir
```

## Usage

Run the tool from your terminal inside any project folder to automatically scan and update all `.yaml` and `.yml` files in place:

```bash
pardon_sir
```

To target a specific folder directory elsewhere on your computer, pass the pathway as an argument:

```bash
pardon_sir /path/to/your/yaml/files
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
