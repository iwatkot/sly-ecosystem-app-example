import supervisely as sly

from supervisely.app.widgets import Container

import src.ui.section as section

layout = Container(widgets=[section.card])

app = sly.Application(layout=layout)
