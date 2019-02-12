Usage
=====
You can define the builder in your settings.py and then import it
in each app and add the configurations you need


.. code-block:: python

  from django_pinject import ObjectGraphBuilder
  import pinject

  class MyService(object):
	  def __init__(long_name: SomeReallyLongClassName):
		  self.my_dep = long_name

  # app 1
  class MyBindingSpec(pinject.BindingSpec):
	   def configure(self, bind):
		   bind('long_name', to_class=SomeReallyLongClassName)

  object_graph_builder.addBindingSpec(BindingSpec1)

  # app 2
  class MyBindingSpec2(pinject.BindingSpec):
	   def configure(self, bind):
		   bind('long_name2', to_class=SomeReallyLongClassName2)

  object_graph_builder.addModules([app2.module1, app2.module2]) # which you have imported
  object_graph_builder.addBindingSpec(BindingSpec1)

  # client
  object_graph = object_graph_builder.get_object_graph()

  my_service = object_graph.provide(MyService)


Each time you call *object_graph_builder.get_object_graph()*, it will check if it needs to rebuild the object graph.
