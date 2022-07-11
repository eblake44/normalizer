# Normalizer

Python package for normalizing data. Only CSV file normaliztion is supported and usage instructions are below.

For a description of functionality and a description of what normaliztion means, see the [instructions](Instructions.md) documentation

## CSV Normalization Usage Instructions

1. This tool is developed with python v3.10, ensure this version of python is installed. 

2. Dependencies are managed with `pipenv` so this must first be installed.
```
pip install pipenv
```

3. Install dependencies from locked Pipfile
```
pipenv install --deploy
```

4. Enable the virtual environment that pipenv installed the dependencies to:
```
pipenv shell
```

5. Call the CSV normalization file and pass in the input .csv file name:
```
python ./normalizer/CSVnormalizer.py <input_file_name> [output_file_name]
```
- `output_file_name` is an optional input argument. If only an `input_file_name` is supplied, the output file name will be the same as the `input_file_name` except "_norm" will be appended to the filename.