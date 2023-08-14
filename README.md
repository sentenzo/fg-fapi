# Template adaptation checklist
## Software requirements
- [ ] [**python3.11**](https://www.python.org/downloads/)
- [ ] **make** (to install it on Windows: [Chocolatey](https://github.com/chocolatey/choco) - [GNU make 4.3](https://community.chocolatey.org/packages/make))
- [ ] [**Poetry**](https://python-poetry.org/)


## `Makefile`
- [ ] change the `PROJECT_DIR` value to the name of your app directory

## Files and directories
- [ ] change the `my_app` directory name to the name of your application (exactly the same as the `PROJECT_DIR` parameter)
- [ ] add the `.env` file if you need it
- [ ] (optional) add a `LICENSE` file

## `poetry`
- [ ] init your new virtual environment with one of: 
  - `make init` 
  - `poetry install`
- [ ] add the dependencies required with:
  - `poetry add python-dotenv` 
- [ ] add the development dependencies with one of: 
  - `poetry add -D pylint` 
  - `poetry add -G dev pylint` 

## `./pyproject.toml`
### (optional) `[tool.isort]`
- [ ] add your 2-d level folder names to the `known_local_folder` list
- [ ] change the `line_length` value if you want to omit the [PEP-8 guidelines](https://peps.python.org/pep-0008/#maximum-line-length)

### (optional) `[tool.isort]`
- [ ] change the `line-length` value if, again, you want to omit the official guidelines

### `[tool.poetry]`
- [ ] change `name`, `description` and `authors` according to your credentials
- [ ] change the `license` field if you have any


## The final checkup
- [ ] check the linting functionality with `make lint` (no errors should occure)
- [ ] check tests with `make test-all`
- [ ] finally check the application itself with one of: 
  - `make`  
  - `make run`
