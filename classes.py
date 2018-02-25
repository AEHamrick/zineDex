'''
Basic structures to keep track of things that might be found in the zine collection.
Initially: Album, Band, Zine, Interview, (record) Label, (music) Festival

'''
class RefItem(object):

	def __init__(self, reftype, refname, refby, refbypage, refbyissue):
		self.type = reftype
		self.name = refname
		self.referencedBy = refby
		self.referencedByIssue = refbyissue
		self.referencedOnPage = refbypage


class Album(RefItem):

	def __init__(self, refname, refby, refbypage, refbyissue,
				 title, refband, genre, reflabel=None, year=None):
		super().__init__('Album', refname, refby, refbypage, refbyissue)

		#TODO: this might work better than passing the type in?
		#self.type = self.__class__.__name__

		self.title = title
		self.band = refband
		self.genre = genre
		self.label = reflabel
		self.year = year


class Band(RefItem):

	def __init__(self, refname, refby, refbypage, refbyissue,
				 name, location=None, year=None):
		super().__init__('Band', refname, refby, refbypage, refbyissue)

		self.name = name
		self.location = location
		self.year = year


class Interview(RefItem):

	def __init__(self, refname, refby, refbypage, refbyissue,
				 name, interviewer, type):
		super().__init__('Interview', refname, refby, refbypage, refbyissue)

		self.name = name
		self.interviewer = interviewer
		self.type = type


class Zine(RefItem):

	def __init__(self, refname, refby, refbypage, refbyissue,
				 name, editor=None, location=None, web=None):
		super().__init__('Zine', refname, refby, refbypage, refbyissue)

		self.name = name
		self.location = location
		self.editor = editor
		self.web = web


class Label(RefItem):

	def __init__(self, refname, refby, refbypage, refbyissue,
				 name, location=None, web=None):
		super().__init__('Label', refname, refby, refbypage, refbyissue)

		self.name = name
		self.location = location
		self.web = web

class Festival(RefItem):

	def __init__(self, refname, refby, refbypage, refbyissue,
				 name, year = None, location=None, web=None):
		super().__init__('Festival', refname, refby, refbypage, refbyissue)

		self.name = name
		self.location = location
		self.web = web
		self.year = year