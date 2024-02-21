# Amazon Ion to JSON Converter (v1.0.0b) [WIP]

This project provides python abstractions for converting [Amazon Ion Data Format](https://docs.aws.amazon.com/qldb/latest/developerguide/ion.html) to JSON format and vice-versa, enabling seamless use of Ion-formatted data in systems that prefer JSON.

## Dependencies:

- awscli
- amazon (Verify the library name and required version)
- pyion2json (Specify required version if necessary)

Install dependencies using `pip install awscli amazon pyion2json`.

## Getting Started:

### Command Line:

```bash
python jsion.py -i input.ion -o output.json
```

**Use code with caution.**

This command converts the "input.ion" file to the "output.json" file. Available options include:

- `-i`: Input file path (required)
- `-o`: Output file path (required)
- `-f`: Output format (JSON, default; also supports YAML)

### Docker:

#### Build the image:

```bash
docker build -t ionjsonimg:latest .
```

**Use code with caution.**

#### Run the container:

```bash
docker run --name ion_json ionjsonimg:latest -v /path/to/data:/data
```

**Use code with caution.**

This mounts the local `/path/to/data` directory to the container's `/data` directory, allowing you to process files within the container.

## Troubleshooting:

If you encounter issues, check the project's issue tracker or provide details on the error message and steps taken.

## Additional Notes:

- This project is licensed under the Apache 2.0 License.
- Unit tests are implemented to ensure correctness and reliability.
- We welcome contributions! See the `CONTRIBUTING.md` file for details.
