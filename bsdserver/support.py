from configparser import ConfigParser

class Config(ConfigParser):
	def __init__(self, PATH="./config.ini"):
		ConfigParser.__init__(self)
		self.path = PATH
		self.read(PATH)

	def getval(self, section, option, raw=False):
		val = super().get(section, option)
		if not raw:
			val = self._convert(val)
		return val

	def _convert(self, val):

		def tryfunc(func):
			try:
				_val = func(val)
			except:
				return None
			else:
				return _val

		for func in [float, int, str]:
			ret = tryfunc(func)
			if ret != None:
				break
		return ret

	def __del__(self):
		pass