
import xml.etree.ElementTree as ET
from svgpathtools import svg2paths



class vector_service:

    def aspect_ratio_file(svg_path):
        # خواندن محتوای فایل SVG
        with open(svg_path, 'r') as file:
            svg_content = file.read()
        # خواندن ابعاد از تگ <svg>
        root = ET.fromstring(svg_content)
        width = root.get('width')
        height = root.get('height')
        return {'width': width, 'height': height}
    
    def aspect_rate_content(path_svg):
        paths, attributes = svg2paths(path_svg)
        mypath = paths[0]
        xmin, xmax, ymin, ymax = mypath.bbox()
        width = xmax - xmin
        height = ymax - ymin
        return {'width': width, 'height': height}

    def svg_file_to_string(svg_path):
        try:
            with open(svg_path, 'r', encoding='utf-8') as file:
                svg_string = file.read()
            return svg_string
        except FileNotFoundError:
            return None

    def svg_file_to_binary(svg_path):
        try:
            with open(svg_path, 'rb') as file:
                svg_binary = file.read()
            return svg_binary
        except FileNotFoundError:
            return None