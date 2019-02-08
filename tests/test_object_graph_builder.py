from unittest.mock import patch

import pinject
from pinject.object_graph import ObjectGraph

from django_pinject import ObjectGraphBuilder


class TestObjectGraphBuilder:
    def test_can_build_without_any_configurations(self):
        builder = ObjectGraphBuilder()
        assert isinstance(builder.get_object_graph(), ObjectGraph)

    @patch('django_pinject.pinject.new_object_graph')
    def test_add_class(self, mocked_object_graph_method):
        builder = ObjectGraphBuilder()
        class_to_add = TestObjectGraphBuilder
        builder.add_class(class_to_add)
        builder.get_object_graph()

        mocked_object_graph_method.assert_called_once_with(binding_specs=[], classes=[class_to_add], modules=[])

    @patch('django_pinject.pinject.new_object_graph')
    def test_add_module(self, mocked_object_graph_method):
        builder = ObjectGraphBuilder()
        module_to_add = pinject
        builder.add_module(module_to_add)
        builder.get_object_graph()

        mocked_object_graph_method.assert_called_once_with(binding_specs=[], classes=[], modules=[module_to_add])

    @patch('django_pinject.pinject.new_object_graph')
    def test_add_binding_spec(self, mocked_object_graph_method):
        builder = ObjectGraphBuilder()
        binding_spec_to_add = TestObjectGraphBuilder
        builder.add_binding_spec(binding_spec_to_add)
        builder.get_object_graph()

        mocked_object_graph_method.assert_called_once_with(binding_specs=[binding_spec_to_add], classes=[], modules=[])

    def test_rebuild_when_tainted(self):
        builder = ObjectGraphBuilder()
        object_graph = builder.get_object_graph()
        builder.add_class(TestObjectGraphBuilder)
        new_object_graph = builder.get_object_graph()
        assert id(object_graph) != id(new_object_graph)

    def test_not_building_when_clean(self):
        builder = ObjectGraphBuilder()
        object_graph = builder.get_object_graph()
        new_object_graph = builder.get_object_graph()
        assert id(object_graph) == id(new_object_graph)
