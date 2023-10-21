
import xml.etree.ElementTree as ET



class vector_service:

    def aspect_ratio(file):
        try:
            root = ET.fromstring(file)
            width = root.attrib.get('width')
            height = root.attrib.get('height')
            return {'width': width, 'height': height}
        except ET.ParseError as e:
            print(f'Error parsing SVG: {e}')
            return None