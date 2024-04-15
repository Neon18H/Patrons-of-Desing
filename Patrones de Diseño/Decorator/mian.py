from concrete_component import PlainText
from concrete_decorator import HTMLDecorator

plain_text = PlainText('/̵͇̿̿/’̿’̿ ̿ ̿̿ ̿̿ ̿̿💥')
print("text sin decorar:", plain_text.render())

html_text = HTMLDecorator(plain_text)
print("text decorado:", html_text.render())

