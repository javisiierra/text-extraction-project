import xml.etree.ElementTree as ET
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter
import sys
from fpdf import FPDF
import shutil
import requests

def process_pdf_with_grobid(pdf_path, output_dir):
    url = "http://localhost:8070/api/processFulltextDocument"
    files = {"input": open(pdf_path, "rb")}
    response = requests.post(url, files=files)
    
    if response.status_code == 200:
        article_dir = os.path.join(output_dir, os.path.basename(pdf_path).replace(".pdf", ""))
        os.makedirs(article_dir, exist_ok=True)
        xml_path = os.path.join(article_dir, os.path.basename(pdf_path).replace(".pdf", ".xml"))
        with open(xml_path, "w", encoding="utf-8") as f:
            f.write(response.text)
        return xml_path, article_dir
    else:
        print(f"Error procesando {pdf_path}: {response.status_code}")
        return None, None

def process_xml(file_path, output_dir, figures_count, global_word_counter):
    ns = {'tei': 'http://www.tei-c.org/ns/1.0'}

    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        
        title_element = root.find('.//tei:titleStmt/tei:title', ns)
        title = title_element.text.strip() if title_element is not None and title_element.text else "Sin título"
        
        abstract_element = root.find('.//tei:abstract//tei:p', ns)
        abstract_text = abstract_element.text.strip() if abstract_element is not None and abstract_element.text else ""
        
        keywords_element = root.findall('.//tei:keywords/tei:term', ns)
        keywords = [kw.text.strip().lower() for kw in keywords_element if kw.text]
        
        if keywords:
            global_word_counter.update(keywords)
        
        body_texts = [p.text.strip() for p in root.findall('.//tei:body//tei:p', ns) if p.text]
        figure_mentions = sum(text.lower().count("fig.") + text.lower().count("figure") for text in body_texts)
        figures_count[file_path] = figure_mentions

        links = [ptr.attrib['target'] for ptr in root.findall('.//tei:ptr', ns) if 'target' in ptr.attrib]
    
        article_dir = os.path.dirname(file_path)
        pdf_path = os.path.join(article_dir, "informe.pdf")
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.add_font("DejaVu", "", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", uni=True)
        pdf.set_font("DejaVu", size=12)
        pdf.cell(200, 10, title, ln=True, align='C')
        
        pdf.ln(10)
        pdf.multi_cell(0, 10, f"Resumen:\n{abstract_text}")
        pdf.ln(5)
        pdf.multi_cell(0, 10, f"Palabras clave: {', '.join(keywords) if keywords else 'No hay palabras clave disponibles'}")
        
        pdf.ln(10)
        pdf.cell(200, 10, "Número de Figuras en el Artículo", ln=True, align='C')
        pdf.ln(5)
        pdf.multi_cell(0, 10, f"Total de figuras mencionadas: {figure_mentions}")

        pdf.ln(10)
        pdf.cell(200, 10, "Enlaces Encontrados", ln=True, align='C')
        pdf.ln(5)
        for link in links:
            pdf.multi_cell(0, 10, link)
        
        pdf.output(pdf_path)
        print(f"Informe guardado en: {pdf_path}")
    
    except ET.ParseError:
        print(f"Error al analizar el archivo XML: {file_path}")
        return

def main():
    if len(sys.argv) < 2:
        print("Uso: python programa.py <carpeta_con_pdfs>")
        exit()

    pdf_dir = sys.argv[1]
    if not os.path.isdir(pdf_dir):
        print(f"No se encontró la carpeta: {pdf_dir}")
        exit()

    output_dir = os.path.join(pdf_dir, "procesados")
    os.makedirs(output_dir, exist_ok=True)

    figures_count = {}
    global_word_counter = Counter()

    for pdf_file in os.listdir(pdf_dir):
        if pdf_file.endswith(".pdf"):
            pdf_path = os.path.join(pdf_dir, pdf_file)
            xml_path, article_dir = process_pdf_with_grobid(pdf_path, output_dir)
            if xml_path:
                process_xml(xml_path, article_dir, figures_count, global_word_counter)
    
    # Crear la nube de palabras con las palabras clave más repetidas en todos los artículos
    font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
    wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='viridis', max_words=100, font_path=font_path)
    wordcloud.generate_from_frequencies(global_word_counter)
    wordcloud_path = os.path.join(output_dir, "wordcloud_global.png")
    wordcloud.to_file(wordcloud_path)
    
    # Crear PDF final con palabras clave más repetidas
    pdf_path = os.path.join(output_dir, "resumen_palabras.pdf")
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.add_font("DejaVu", "", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", uni=True)
    pdf.set_font("DejaVu", size=12)
    pdf.cell(200, 10, "Palabras Clave Más Frecuentes en los Artículos Analizados", ln=True, align='C')
    pdf.ln(10)
    
    for word, count in global_word_counter.most_common(100):
        pdf.cell(0, 10, f"{word}: {count}", ln=True)
    
    if os.path.exists(wordcloud_path):
        pdf.image(wordcloud_path, x=10, w=180)
    
    pdf.output(pdf_path)
    print(f"Resumen de palabras clave guardado en: {pdf_path}")
    
    # Crear la tabla comparativa del número de figuras por artículo
    total_figures_path = os.path.join(output_dir, "comparacion_figuras.png")
    plt.figure(figsize=(10, 5))
    plt.bar(figures_count.keys(), figures_count.values(), color='skyblue')
    plt.xticks(rotation=45, ha='right')
    plt.ylabel("Número de Figuras")
    plt.xlabel("Artículo")
    plt.title("Número Total de Figuras por Artículo")
    plt.savefig(total_figures_path)
    plt.close()
    print(f"Tabla comparativa guardada en: {total_figures_path}")

if __name__ == "__main__":
    main()