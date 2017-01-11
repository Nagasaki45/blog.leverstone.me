from collections import namedtuple
import os

from docutils import nodes
from docutils.parsers.rst import directives, Directive
from PIL import Image

Item = namedtuple('Item', ['src', 'alt'])


class Slick(Directive):
    """
    Creates a carousel of images. Note that it doesn't replace the necessary js
    and stylesheets, but only creates the relevant markup.

    Usage:

        .. slick::
            http://someserver.com/image.png my alt text
            /path/to/img1.png alt text
            /path/to/img2.png another image alt text
            /path/to/img3.png last image alt text
    """
    # To allow varied number of space separated arguments (image paths)
    required_arguments = 1
    final_argument_whitespace = True

    def run(self):
        content = self.arguments[0]
        items = [Item(*line.split(maxsplit=1)) for line in content.splitlines()]
        slick_node = nodes.container(format='html')
        slick_node['classes'].append('slick')
        img_nodes = [nodes.image(uri=item.src, alt=item.alt, format='html')
                     for item in items]
        slick_node.children = img_nodes
        return [slick_node]


def register():
    directives.register_directive('slick', Slick)
