from decor import TextDecorator

class HTMLDecorator(TextDecorator):
    def render(self):
        return f'▄︻{self._text_component.render()}━一'
    

