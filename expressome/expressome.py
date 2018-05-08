dataset_configs = {
	"alex_spirit_journey": {
		"name": "alex_spirit_journey",
		"root": "/host/expressome/videosets/alex_warren_spirit_journey",
		"videos": [
			{
				"name": "VID_20180314_233707.mp4",
				"keywords": ["subaru"],
				"snippet": "Subaru outside Joshua Tree after stuff stolen",
				# "start": 0,
				# "end": 1,
				# "boundary": [0,1,0,1], # x0, x1, y0, y1
			},
			{
				"name": "VID_20180315_003215.mp4",
				"keywords": ["subaru"],
				"snippet": "Subaru outside Joshua, post rant",
			},
			{
				"name": "VID_20180324_172643.mp4",
				"keywords": ["wide"],
				"snippet": "Above chochise during beanfest",
			},
		]
	}
}

def get_dataset(name):
	if name in dataset_configs:
		return Dataset(**dataset_configs[name])
	return None

class Video:
	def __init__(self, name=None, root=None, snippet="", keywords=[], start=None, end=None, boundaries=None):
		if not name or not root:
			raise ValueError('kwargs for Video are missing.')
		self.name = name
		self.root = root
		self.snippet = snippet
		self.keywords = keywords
		self.start = start
		self.end = end
		self.boundaries = boundaries

	def load(self):
		pass

	def __str__(self):
		return "{}: {}".format(self.name, self.snippet)


class Dataset:
	def __init__(self, name=None, root=None, videos=[]):
		if not name or not root or not videos:
			raise ValueError('kwargs for Dataset are missing.')
		self.name = name
		self.root = root
		self.videos = [Video(**v, root=root) for v in videos]

	def load_videos(self):
		for v in self.videos:
			v.load()
		