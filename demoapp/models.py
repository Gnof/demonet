from django.db import models as m

''' demo model for demonet '''
class DemoModel(m.Model):
	name = m.CharField(max_length=100, unique=True)
	
	desc = m.TextField()

	date = m.DateTimeField()

	def __unicode__(self):
		return self.name

''' demo model relational model '''
class SubModel(m.Model):
	name = m.CharField(max_length=100)

	relation = m.ForeignKey(DemoModel)

	def __unicode__(self):
		return self.name + " -- " + self.relation.name