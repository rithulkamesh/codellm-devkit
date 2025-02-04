from pdb import set_trace
from cldk import CLDK
from typing import List, Tuple
from cldk.analysis import AnalysisLevel
from cldk.models.java.models import JMethodDetail


def test_get_symbol_table_is_not_null(test_fixture, codeanalyzer_jar_path):
    # Initialize the CLDK object with the project directory, language, and analysis_backend.
    cldk = CLDK(language="java")
    analysis = cldk.analysis(
        project_path=test_fixture,
        analysis_backend="codeanalyzer",
        analysis_backend_path=codeanalyzer_jar_path,
        eager=True,
        analysis_level=AnalysisLevel.call_graph,
    )
    assert analysis.get_symbol_table() is not None


def test_get_class_call_graph(test_fixture, codeanalyzer_jar_path):
    # Initialize the CLDK object with the project directory, language, and analysis_backend.
    cldk = CLDK(language="java")

    analysis = cldk.analysis(
        project_path=test_fixture,
        analysis_backend="codeanalyzer",
        analysis_backend_path=codeanalyzer_jar_path,
        eager=True,
        analysis_level=AnalysisLevel.call_graph,
    )
    class_call_graph: List[Tuple[JMethodDetail, JMethodDetail]] = analysis.get_class_call_graph(
        qualified_class_name="com.ibm.websphere.samples.daytrader.impl.direct.TradeDirectDBUtils"
    )
    assert class_call_graph is not None
