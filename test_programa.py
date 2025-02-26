import os
import pytest
import shutil
from collections import Counter
from programa import process_pdf_with_grobid, process_xml

@pytest.fixture
def setup_test_env():
    """Crea un entorno de prueba con archivos de muestra."""
    test_dir = "test_pdfs"
    os.makedirs(test_dir, exist_ok=True)
    
    sample_pdf = os.path.join(test_dir, "sample.pdf")
    with open(sample_pdf, "wb") as f:
        f.write(b"%PDF-1.4\n%Fake PDF content for testing")
    
    yield test_dir
    
    shutil.rmtree(test_dir)

def test_process_pdf_with_grobid(setup_test_env):
    """Verifica que GROBID procesa el PDF y genera un archivo XML."""
    test_dir = setup_test_env
    pdf_path = os.path.join(test_dir, "sample.pdf")
    output_dir = os.path.join(test_dir, "procesados")

    xml_path, article_dir = process_pdf_with_grobid(pdf_path, output_dir)
    
    assert xml_path is not None
    assert os.path.exists(xml_path)
    assert os.path.exists(article_dir)

def test_process_xml():
    """Prueba la extracción de información de un archivo XML de ejemplo."""
    test_dir = "test_xml"
    os.makedirs(test_dir, exist_ok=True)
    
    sample_xml = os.path.join(test_dir, "sample.xml")
    xml_content = """<?xml version="1.0" encoding="UTF-8"?>
    <TEI xmlns=\"http://www.tei-c.org/ns/1.0\">
        <teiHeader>
            <fileDesc>
                <titleStmt>
                    <title>Artículo de Prueba</title>
                </titleStmt>
            </fileDesc>
        </teiHeader>
        <text>
            <body>
                <p>Este artículo menciona una figura (Fig. 1) en su texto.</p>
            </body>
        </text>
    </TEI>"""
    
    with open(sample_xml, "w", encoding="utf-8") as f:
        f.write(xml_content)
    
    figures_count = {}
    global_word_counter = Counter()
    process_xml(sample_xml, test_dir, figures_count, global_word_counter)
    
    assert figures_count[sample_xml] == 1  # Debería contar una figura mencionada
    
    shutil.rmtree(test_dir)

if __name__ == "__main__":
    pytest.main()