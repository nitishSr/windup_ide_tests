# windup_ide_tests

## About the project
This project is for creating automated tests for verifying the functionality of MTA IDE plugin. This is an extension of [windup_integration_test](https://github.com/windup/windup_integration_test) extensively created for coverage of IDEs. Currently below IDEs have been covered:

| IDE           | Version |
| ------------- | ------------- |
| Redhat Code Ready Studio  | 12.18.0.GA  |
| Eclipse IDE for J2EE developers  | 2020-09  |
| VS Code  | 1.54.1 |
| Eclipse CHE  | theia |
| IntelliJ IDEA  | 2021.1.3 |

**Supported OS**

Works on *Linux/RHEL/Fedora* with X11 windowing system enabled (does not work with Wayland scheme)

## Getting Started
To get started with project in development mode or basic usage, follow the below steps:

**Pre-requisites**

- Python 3+ installed
- Respective IDE (to be tested) installed on local machine
- MTA IDE plugin installed in that IDE
- The project to be analysed is imported in IDE
- Selenium webdriver installed locally (chromedriver or geckodriver)

Sample project can be downloaded

- [weblogic-jms-case](https://drive.google.com/file/d/1l4VaWeYbsz7OMFZPT_OBY1ERntxNOUPp/view?usp=sharing_eil&ts=605ab414)

**Eclipse CHE setup**

- The workspace should be created before running test using devfile yaml

    `~/windup_ide_tests/src/conf/eclipse_che_conf.yaml`

- Use JIRA credentials for login, the same must be provided in config.json

    `~/windup_ide_tests/src/conf/config.json`

**Installation**

1. Clone the forked repository and move to repo home
    ```
    git clone https://github.com/<user>/windup-ide-tests.git
    cd windup-ide-tests
    ```
2. Create python3 virtual env

    `python3 -m venv .ide_env`

3. Activate virtual env

    `source .ide_env/bin/activate`

4. Install from setup

    `pip install .`

5. Edit the **config.json** file and provide full path to the executable of respective IDE

    `cd ~/windup_ide_tests/src/conf`

**Contributing to the project**

1. Fork the repository
2. Clone the forked repo `git clone https://github.com/<user>/windup-ide-tests.git`
3. Run the aforementioned installation steps
4. Create new branch `git checkout -b <new_branch_name>`
5. Commit the changes `git commit -m 'Explanatory commit message'`
6. Push your changes to branch `git push origin <new_branch_name>`
7. Open new pull request

## License
Distributed under Eclipse Public License. See [LICENSE](https://github.com/nitishSr/windup-ide-tests/blob/main/LICENSE) for more information.
