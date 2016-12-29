from functools import partial
from pelican import signals


def get_index(order, category_and_its_articles):
    """
    Get the index of a category.

    order: list of category names (strings).
    category_and_its_articles: 2 items tuple.
    """
    category, articles = category_and_its_articles
    return order.index(category.name)


def sort_categories(generator):
    """
    Sort the categories by settings.CATEGORIES_ORDER.
    """
    order = generator.settings['CATEGORIES_ORDER']
    partial_get_index = partial(get_index, order)
    categories = generator.context.get('categories')
    categories.sort(key=partial_get_index)
    generator.context['categories'] = categories


def register():
    signals.article_generator_finalized.connect(sort_categories)
