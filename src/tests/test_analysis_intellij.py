import time

from src.lib.config import config_data


def test_analysis_eap(setup_intellij):
    """
    Test to run analysis for migration path Anything to EAP 7 in IntelliJ IDE
    """
    intellij = setup_intellij
    time.sleep(5)
    intellij.open_mta_perspective()
    # Intellij freezes without this sleep
    time.sleep(3)
    intellij.run_simple_analysis(
        project=config_data["project_paths"]["eap7_generic"], migration_target="eap7",
    )
    assert intellij.is_analysis_complete()
    assert intellij.verify_story_points(target="eap7")


def test_analysis_eapxp(setup_intellij):
    """
    Test to run analysis on ruleset thorntail to eapxp2 in IntelliJ IDE
    """
    intellij = setup_intellij
    time.sleep(5)
    intellij.open_mta_perspective()
    # Intellij freezes without this sleep
    time.sleep(3)
    intellij.run_simple_analysis(
        project=config_data["project_paths"]["eapxp_ruleset"], migration_target="eapxp",
    )
    assert intellij.is_analysis_complete()
    assert intellij.verify_story_points(target="eapxp")


def test_analysis_quarkus(setup_intellij):
    """
    Test to run analysis on ruleset quarkus1 in IntelliJ IDE
    """
    intellij = setup_intellij
    time.sleep(5)
    intellij.open_mta_perspective()
    # Intellij freezes without this sleep
    time.sleep(3)
    intellij.run_simple_analysis(
        project=config_data["project_paths"]["eapxp_ruleset"], migration_target="quarkus1",
    )
    assert intellij.is_analysis_complete()
    assert intellij.verify_story_points(target="quarkus1")
