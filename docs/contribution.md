# Contribute code

---
## Create PR
We welcome anyone to contribute code to VeighNa.  

If wishing to contribute code please use Github's PR (Pull Request) process.

The PR process is roughly as follows:

---
1. [Create Issue][CreateIssue] - For larger changes (e.g. new features, major refactoring, etc.) it is recommended to open an issue to discuss them first, and for smaller improvements (e.g. documentation improvements, bugfixes, etc.) it is sufficient to send a PR.

2. Fork [VeighNa][#GithubVnpy] - Click the **Fork** button in the upper right corner.

3. Clone your own fork: ```git clone https://github.com/$userid/vnpy.git```
	
	> If your fork is outdated, you need to manually [sync][GithubDocForSync].
	
4. Create your own branch from **dev**: ```git checkout -b $my_feature_branch dev``` > If your fork is out of date, you need to [sync][GithubDocForSync] it manually.

5. Make changes to $my_feature_branch and push them to your forked repository.

6. Create a [Pull Request] from your forked $my_feature_branch branch to the main project's **dev** branch.  
 [Click here][CreatePR], then click **compare across forks** and select the required fork and branch to create the PR.

---

Please be patient after creating the PR: we will check the PR as soon as we have time, and once your code is useful and [meets the requirements](#code style), it will be merged!


---
## Code style
There are some basic rules that need to be followed when writing code for VeighNa, otherwise your code may not be merged.
These rules include:
- [Contribute code](# Contribute code)
  - [create pr](#create pr)
  - [Code style](#code style)
    - [Naming Rules](#Naming Rules)
    - [Code Format](#Code Format)
    - [Code quality check](#Code quality check)


### Naming rules
The naming rules for our code are as follows:

* Class properties, class methods, parameters and variables use lowercase with underscores
* Class names use camel case
* Constants use uppercase plus underscore form

Example:
```python 3
DEFAULT_PATH = "/tmp/VeighNa/"
class ClassA.
    def __init__(self, arg_one: int, arg_two: str):
        if arg_two is None.
            arg_two = DEFAULT_PATH
        self.property_one = arg_one
        variable_one = "some string"
```


### Code formatting
We don't have particularly strict requirements for code formatting, but at least it should be pep8 compliant, and additionally take a docstring (that's a paragraph of """""") underneath classes and functions.

To make the code pep8 compliant, format your code with [autopep8](https://github.com/hhatto/autopep8) after writing it:

```bash
autopep8 --in-place --recursive . 
```

### Code quality checking
Check your code with [flake8](https://pypi.org/project/flake8/) to make sure there are no errors and warnings.
Running ```flake8`` in the project root directory will check for poorly written code. If it checks for errors or warnings, it means that your code needs some changes to improve the quality.

[GithubVnpy]:https://github.com/vnpy/vnpy
[GithubDocForSync]:https://help.github.com/articles/syncing-a-fork/
[CreateIssue]:https://github.com/vnpy/vnpy/issues/new
[CreatePR]:https://github.com/vnpy/vnpy/compare?expand=1

