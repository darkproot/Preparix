from flet import Page, app, Row
from assets.widgets import InfoBar, Topic, Code

def main(page: Page):
    page.title = "Preparix (v1.0)"
    page.window.height = 750
    page.window.width = 1000
    page.window.icon = "book.ico"
    page.fonts = {
        'code': 'polices\\JetBrainsMono-Light.ttf',
        'title': 'polices\\Silver Christmas.otf',
        'text': 'polices\\ERASMD.TTF',
        'fantasy': 'polices\\Nasalization Rg.otf',
        'title1': 'polices\\Pumpkin Bites Solid.ttf'
    }
    page.window.resizable = False
    page.theme_mode = 'dark'
    page.add(InfoBar(), Row([Topic(), Code()]))
    page.update()

if __name__ == "__main__":
    app(main)