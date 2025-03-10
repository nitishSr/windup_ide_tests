import json
import os

import pytest

from src.lib.application import CodeReadyStudio
from src.lib.application import Eclipse
from src.lib.application import Intellij
from src.lib.application import VisualStudioCode
from src.lib.web import EclipseChe


CONF_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + "/conf/"


@pytest.fixture(scope="session")
def config():
    """
    Fixture to configure IDE path
    """
    with open(CONF_DIR + "config.json") as config:
        config_data = json.load(config)
    return config_data


@pytest.fixture(scope="session")
def setup_codereadystudio(config):
    """
    Fixture to setup codereadystudio application
    """
    codereadystudio = CodeReadyStudio()
    path = config["ide_paths"]["rh_code_ready_studio"]
    codereadystudio.open_application(path)
    codereadystudio.set_default_timeout(timeout=config["timeout_in_seconds"])
    yield codereadystudio
    codereadystudio.close_ide()


@pytest.fixture(scope="session")
def setup_eclipse(config):
    """
    Fixture to setup eclipse application
    """
    eclipse = Eclipse()
    path = config["ide_paths"]["eclipse"]
    eclipse.open_application(path)
    eclipse.set_default_timeout(timeout=config["timeout_in_seconds"])
    yield eclipse
    eclipse.close_ide()


@pytest.fixture(scope="session")
def setup_vscode(config):
    """
    Fixture to setup vs code application
    """
    vscode = VisualStudioCode()
    path = config["ide_paths"]["vs_code"]
    vscode.open_application(path)
    vscode.set_default_timeout(timeout=config["timeout_in_seconds"])
    yield vscode, config
    vscode.close_ide()


@pytest.fixture(scope="function")
def setup_eclipse_che():
    """
    Fixture to setup eclipse che workspace
    """
    eclipse_che = EclipseChe("chrome")
    eclipse_che.open_workspace()
    yield eclipse_che
    eclipse_che.delete_configuration(eclipse_che.configuration_name)
    eclipse_che.close_browser()


@pytest.fixture(scope="session")
def setup_intellij(config):
    """
    Fixture to setup intellij application
    """
    intellij = Intellij()
    path = config["ide_paths"]["intellij"]
    intellij.open_application(path)
    intellij.set_default_timeout(timeout=config["timeout_in_seconds"])
    yield intellij
    intellij.close_ide()
