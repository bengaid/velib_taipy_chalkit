from taipy.gui import Gui
from velib_real_time_page import page as page1

gui = Gui()
gui.add_page("velib", page1)

gui.run(run_browser=True, use_reloader=True)