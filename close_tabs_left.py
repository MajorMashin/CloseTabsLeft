import sublime, sublime_plugin

class CloseTabsLeftCommand(sublime_plugin.WindowCommand):
  def run(self):
    window = self.window
    active_view = window.active_view()
    for view in window.views():
      if view.id() == active_view.id():
        break
      view.set_scratch(True)
      window.focus_view(view)
      window.run_command("close_file")
