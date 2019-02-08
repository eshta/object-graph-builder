__version__ = '1.0.0'

from typing import List
import pinject
from pinject.object_graph import ObjectGraph


class ObjectGraphBuilder(object):
    def __init__(self):
        self.classes: List = []
        self.modules: List = []
        self.binding_specs: List = []
        self.tainted: bool = True
        self.object_graph: ObjectGraph = None

    def get_object_graph(self) -> ObjectGraph:
        if self.tainted:
            self.object_graph = pinject.\
                new_object_graph(classes=self.classes, modules=self.modules, binding_specs=self.binding_specs)
            self.clean()
            return self.object_graph
        else:
            return self.object_graph

    def add_class(self, class_definition):
        self.classes.append(class_definition)
        self.taint()

    def add_classes(self, class_definitions: List):
        self.classes += class_definitions
        self.taint()

    def add_module(self, module):
        self.modules.append(module)
        self.taint()

    def add_modules(self, modules: List):
        self.modules += modules
        self.taint()

    def add_binding_spec(self, binding_spec: pinject.BindingSpec):
        self.binding_specs.append(binding_spec)
        self.taint()

    def add_binding_specs(self, binding_specs: List[pinject.BindingSpec]):
        self.binding_specs += binding_specs
        self.taint()

    def taint(self):
        self.tainted = True

    def clean(self):
        self.tainted = False
