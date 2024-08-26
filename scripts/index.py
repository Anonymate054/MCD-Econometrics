import json

def extract_headings(nb_path):
    """
    Extrae los títulos (headings) de un cuaderno de Jupyter.
    
    Args:
        nb_path (str): La ruta al archivo .ipynb.
        
    Returns:
        List[Tuple[int, str]]: Una lista de tuplas con el nivel del encabezado y el texto.
    """
    with open(nb_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
        
    headings = []
    for cell in notebook['cells']:
        if cell['cell_type'] == 'markdown':
            for line in cell['source']:
                if line.startswith('#'):
                    level = len(line.split(' ')[0])  # Cuenta el número de '#' para determinar el nivel
                    text = line.strip('#').strip()
                    headings.append((level, text))
                    
    return headings

def generate_toc(headings):
    """
    Genera un índice en formato markdown a partir de los encabezados extraídos.
    
    Args:
        headings (List[Tuple[int, str]]): Lista de tuplas con el nivel del encabezado y el texto.
        
    Returns:
        str: El índice en formato markdown.
    """
    toc = []
    for level, text in headings:
        indent = '  ' * (level - 1)  # Indentación basada en el nivel
        toc.append(f'{indent}- [{text}](#{text.lower().replace(" ", "-")})')
    return '\n'.join(toc)