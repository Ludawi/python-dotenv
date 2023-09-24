# python-dotenv

Python-dotenv is a simple utility class for Python applications to easily access environment variables stored in a .env file.
This library is designed to simplify the process of loading environment variables from a file and accessing them within your Python code.

## Usage

1. Import the `GetEnv` class from `dotenv` module.

```python
from dotenv import GetEnv
```

2. Create an instance of the GetEnv class, providing the environment variable key you want to access as an argument. Note that `GetEnv` only searches for the .env file in the current directory.

```python
env = GetEnv('ENV_VRIABLE_KEY')
```

3. Access the values of ypur .env file using strings if needed.

```python
text = str(env)
```

## Example

```python
from dotenv import GetEnv

host = GetEnv('HOST')
token = GetEnv('TOKEN')
email = GetEnv('EMAIL')

print('host: ', str(host))
```
