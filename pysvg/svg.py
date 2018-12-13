"""
basic svg abstraction
"""
import uuid


def xml_repr(cls):
    xml = getattr(cls, 'xml', None)
    if cls.__repr__ is object.__repr__ and xml is not None:
        cls.__repr__ = xml
    if cls.__str__ is object.__str__ and cls.__repr__ is not object.__repr__:
        cls.__str__ = cls.__repr__
    return cls


@xml_repr
class Filter:
    def __init__(self, name: str=None):
        if name is None:
            name = str(uuid.uuid4())
        self.name = name

    def xml(self) -> str:
        pass

    def __hash__(self):
        return hash(self.name)


@xml_repr
class Defs:
    filters: set

    def __init__(self, *actions):
        self.filters = set(actions)

    def add(self, svg_filter: Filter):
        self.filters.add(svg_filter)

    def xml(self):
        r = "<defs>\n"
        for x in self.filters:
            r += x.xml() + '\n'
        r += '\n</defs>'

        return r

    def copy(self):
        return Defs(*self)

    def __iter__(self):
        return iter(self.filters)

    def __add__(self, other):
        return Defs(*self, *other)

    def __radd__(self, other):
        return Defs(*self, *other)

    def __iadd__(self, other):
        self.filters.union(other.filters)
        return self


class Style(dict):
    """
    how one add a style to a shape
    as well as the <defs>
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.defs = Defs()

    def string(self):
        s = ""
        for k, v in self.items():
            if isinstance(v, Filter):
                v = f"url(#{v.name})"
            s += f"{k}:{v};"
        return s

    def __setitem__(self, key, value):
        if isinstance(value, Filter):
            self.defs.add(value)
        super().__setitem__(key, value)

    def copy(self):
        new_style = Style()
        new_style.update(self)
        new_style.defs = self.defs.copy()
        return new_style


@xml_repr
class Shape(dict):
    style: Style

    def __init__(self, name, svg_filter: Filter=None, style: Style=None, **kwargs):
        super().__init__()
        self.name = name
        self.defs = Defs()
        if style is None:
            style = Style()
        self.style = style.copy()
        self.defs += style.defs
        self.update(kwargs)
        if svg_filter is not None:
            self.style['filter'] = svg_filter

    def xml(self):
        attrs = []
        style_str = self.style.string()
        if self.get('style', '') != '' and style_str != '':
            raise TypeError("You could only specify one style")
        if 'style' not in self and style_str != '':  # we need extra settings
            attrs.append(f'style="{style_str}"')
        for k, v in self.items():
            attrs.append(f'{k}="{v}"')
        attrs = " ".join(attrs)
        return f"""
        <{self.name} {attrs}/>
        """


@xml_repr
class SVG:
    """
    a class used to represent a svg image, which
    is just a plain encapsulation of svg APIs
    """
    def __init__(self, width='100%', height='100%', version='1.1'):
        self.shapes = list()
        self.defs = Defs()
        self.width = width
        self.height = height
        self.version = version

    def xml(self) -> str:
        r = f"""<svg width="{self.width}" height="{self.height}" 
        version="{self.version}" 
        xmlns="http://www.w3.org/2000/svg">\n
        """
        for shape in self.shapes:
            r += shape.xml() + '\n'
        r += "\n</svg>"
        return r

    def add_shape(self, shape: Shape):
        """
        add a shape to svg

        :param shape:
        :return:
        """
        self.defs += shape.defs
        self.shapes.append(shape)
