import sublime, sublime_plugin
import os
from subprocess import Popen


class CmderCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		if len(self.view.file_name()) > 0:
			cmd_line = ''
			if sublime.platform() == "windows":
				cmd_line = '"${CMDER_ROOT}\\vendor\\conemu-maximus5\\ConEmu.exe" "/here" /dir "%s" /icon ${CMDER_ROOT}\\icons\\cmder.ico /single /cmd cmd /k "${CMDER_ROOT}\\vendor\\init.bat"'
				cmd_line = cmd_line % (os.path.dirname(os.path.realpath(self.view.file_name())))
				cmd_line = os.path.expandvars(cmd_line)
			print "Cmder command: " + cmd_line
			Popen(cmd_line)


	def is_enabled(self):
		return sublime.platform() == "windows" and self.view.file_name() and len(self.view.file_name()) > 0
