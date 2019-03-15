'''
Basic structures to keep track of things that might be found in the zine collection.
Initially: Album, Band, Zine, Interview, (record) Label, (music) Festival

In theory the bare minimum for an entry would be:
Name
Type
Year
Country
Name of referencing zine
Page referenced on
Issue referenced in

but due to the vagaries of prose it may be necessary to allow these to be None initially so the
data can be scraped from web sources and appended once the initial indexed data has been loaded into a database

'''
from enum import Enum

class Ref_entity():

	def __init__(self, type, name, ref_by_name, ref_by_page, ref_by_issue):

		self.type = type
		self.name = name
		self.ref_by_name = ref_by_name
		self.ref_by_page = ref_by_page
		self.ref_by_issue = ref_by_issue

#region classes for referenced items
class Album(Ref_entity):

	def __init__(self, name, ref_by_name, ref_by_page, ref_by_issue,
				 title, band, genre, label=None, year=None):
		super().__init__(Ref_items.album, name, ref_by_name, ref_by_page, ref_by_issue)

		self.title = title
		self.band = band
		self.genre = genre
		self.label = label
		self.year = year

class Band(Ref_entity):

	def __init__(self, name, ref_by_name, ref_by_page, ref_by_issue,
				 country=None, year=None):
		super().__init__(Ref_items.band, name, ref_by_name, ref_by_page, ref_by_issue)

		self.country = country
		self.year = year


class Interview(Ref_entity):

	def __init__(self, name, ref_by_name, ref_by_page, ref_by_issue,
				 interviewer):
		super().__init__(Ref_items.interview, name, ref_by_name, ref_by_page, ref_by_issue)
		#name == interviewee
		self.interviewer = interviewer

class Zine(Ref_entity):

	def __init__(self, name, ref_by_name, ref_by_page, ref_by_issue,
				 pub_date = None, editor=None, country=None, web=None):
		super().__init__(Ref_items.zine, name, ref_by_name, ref_by_page, ref_by_issue)

		self.country = country
		self.editor = editor
		self.web = web
		self.publication_date = pub_date

class Podcast(Ref_entity):
	# Really adding this so I can eventually index Radio Fenriz stuff; might need to add a new
	# Refitem attribute to separate print and audio references
	# TODO: Consider adding an episode field, might be unneeded
	def __init__(self, name, ref_by_name, ref_by_page, ref_by_issue,
				 caster=None, location=None, web=None):
		super().__init__(Ref_items.podcast, name, ref_by_name, ref_by_page, ref_by_issue)

		self.caster = caster
		self.web = web

class Label(Ref_entity):
	def __init__(self, name, ref_by_name, ref_by_page, ref_by_issue,
				 country=None, web=None):
		super().__init__(Ref_items.label, name, ref_by_name, ref_by_page, ref_by_issue)

		self.country = country
		self.web = web

class Festival(Ref_entity):

	def __init__(self, name, ref_by_name, ref_by_page, ref_by_issue,
				 year = None, country=None, web=None):
		super().__init__(Ref_items.festival, name, ref_by_name, ref_by_page, ref_by_issue)

		self.country = country
		self.web = web
		self.year = year
#endregion
#region classes for collection items
# TODO: Figure this out; maybe just inherit from zine and add new collection entities as needed?
#		not sure I want to get into the business of indexing books or anything other than in the
#		most superficial sense

class Collection_entity():
	'''
	Strictly for items held in the collection; i.e., items being indexed
	'''
	def __init__(self,type,name,issue,pub_date):
		self.name = name
		self.type = type
		self.issue = issue
		self.pub_date = pub_date

class Collection_Zine(Collection_entity):
	'''
	Representation for a zine that is a part of the source collection, rather than one referenced /in/ the
	source collection
	'''

	def __init__(self,type,name,issue,pub_date,editor,contributors, cover_artist, print_type, binding):
		super().__init__(Collection_items.zine,name,issue,pub_date)

#endregion

#region data structures
class Ref_items(Enum):
	album 			= 'Album'
	band			= 'Band'
	festival 		= 'Festival'
	interview 		= 'Interview'
	label 			= 'Label'
	podcast 		= 'Podcast'
	zine 			= 'Zine'

class Collection_items(Enum):
	zine 			= 'Zine (Collection)'
	book 			= 'Book'


#endregion
