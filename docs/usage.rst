Usage
=====

You can define the builder in your settings.py and then import it
in each app and add the configurations you need

**In settings.py**

.. code-block:: python

  from django_pinject import ObjectGraphBuilder

  object_graph_builder = ObjectGraphBuilder()


App 1

in apps.App1Config.ready()
.. code-block:: python

  from config.settings import object_graph_builder
  import pinject


  class MyService(object):
	  def __init__(long_name: SomeReallyLongClassName):
		  self.my_dep = long_name

  class MyBindingSpec(pinject.BindingSpec):
	   def configure(self, bind):
		   bind('long_name', to_class=SomeReallyLongClassName)

  object_graph_builder.addBindingSpec(BindingSpec1)

**App 2**
in apps.App2Config.ready()

.. code-block:: python

  from config.settings import object_graph_builder
  import pinject


  class MyBindingSpec2(pinject.BindingSpec):
	   def configure(self, bind):
		   bind('long_name2', to_class=SomeReallyLongClassName2)

  object_graph_builder.addModules([app2.module1, app2.module2]) # which you have imported
  object_graph_builder.addBindingSpec(BindingSpec1)


**Client**

.. code-block:: python

  object_graph = object_graph_builder.get_object_graph()

  my_service = object_graph.provide(MyService)


Each time you call *object_graph_builder.get_object_graph()*, it will check if it needs to rebuild the object graph.
