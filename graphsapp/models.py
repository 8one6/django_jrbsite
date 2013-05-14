from django.db import models

class Graph(models.Model):
	name = models.CharField(max_length=30)
	def __unicode__(self):
		return self.name

class Node(models.Model):
	name = models.CharField(max_length=30)
	owned_by_graph = models.ForeignKey(Graph)
	def __unicode__(self):
		return self.name
		
class Edge(models.Model):
	name = models.CharField(max_length=30)
	from_node = models.ForeignKey(Node, related_name='edge_from_node')
	to_node = models.ForeignKey(Node, related_name='edge_to_node')
	def __unicode__(self):
		return r'%s: %s->%s' % (self.name, self.from_node, self.to_node)
	