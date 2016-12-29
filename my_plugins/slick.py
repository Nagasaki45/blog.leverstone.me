from collections import namedtuple
import os

from docutils import nodes
from docutils.parsers.rst import directives, Directive
from PIL import Image

THUMBNAIN_HEIGHT = 500
THUMBNAIL_SUFFIX = ".thumb"


Item = namedtuple('Item', ['src', 'alt'])


class Slick(Directive):
    """
    Creates a carousel of thumbnails for images. Note that it doesn't replace
    the necessary js and stylesheets, but only creates the relevant markup.

    Usage:

        .. slick::
            /path/to/img1.png alt text
            /path/to/img2.png 2nd image alt text
            /path/to/img3.png 3rd image alt text
    """
    # To allow varied number of space separated arguments (image paths)
    required_arguments = 1
    final_argument_whitespace = True

    def run(self):
        content = self.arguments[0]
        items = [Item(*line.split(maxsplit=1)) for line in content.splitlines()]

        for item in items:
            self.create_thumbnail(item.src)

        slick_node = nodes.container(format='html')
        slick_node['classes'].append('slick')
        thumbnails = [Item('{}.{}'.format(item.src, THUMBNAIL_SUFFIX), item.alt)
                      for item in items]
        img_nodes = [nodes.image(uri=item.src, alt=item.alt, format='html')
                     for item in thumbnails]
        slick_node.children = img_nodes
        return [slick_node]

    def create_thumbnail(self, src):
        infile = 'content{}'.format(src)
        outfile = 'output{}.{}'.format(src, THUMBNAIL_SUFFIX)
        image = Image.open(infile)
        new_size = self.calculate_thumbnail_size(image.size)
        image.thumbnail(new_size, Image.ANTIALIAS)
        image.save(outfile, 'jpeg')

    def calculate_thumbnail_size(self, size):
        original_height, original_width = size
        new_width = original_height / original_width * THUMBNAIN_HEIGHT
        return (THUMBNAIN_HEIGHT, new_width)


def register():
    directives.register_directive('slick', Slick)
