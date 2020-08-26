# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.mdb.clickhouse.v1 import resource_preset_pb2 as yandex_dot_cloud_dot_mdb_dot_clickhouse_dot_v1_dot_resource__preset__pb2
from yandex.cloud.mdb.clickhouse.v1 import resource_preset_service_pb2 as yandex_dot_cloud_dot_mdb_dot_clickhouse_dot_v1_dot_resource__preset__service__pb2


class ResourcePresetServiceStub(object):
    """A set of methods for managing ResourcePreset resources.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/yandex.cloud.mdb.clickhouse.v1.ResourcePresetService/Get',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_clickhouse_dot_v1_dot_resource__preset__service__pb2.GetResourcePresetRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_mdb_dot_clickhouse_dot_v1_dot_resource__preset__pb2.ResourcePreset.FromString,
                )
        self.List = channel.unary_unary(
                '/yandex.cloud.mdb.clickhouse.v1.ResourcePresetService/List',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_clickhouse_dot_v1_dot_resource__preset__service__pb2.ListResourcePresetsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_mdb_dot_clickhouse_dot_v1_dot_resource__preset__service__pb2.ListResourcePresetsResponse.FromString,
                )


class ResourcePresetServiceServicer(object):
    """A set of methods for managing ResourcePreset resources.
    """

    def Get(self, request, context):
        """Returns the specified ResourcePreset resource.

        To get the list of available ResourcePreset resources, make a [List] request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Retrieves the list of available ResourcePreset resources.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ResourcePresetServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_clickhouse_dot_v1_dot_resource__preset__service__pb2.GetResourcePresetRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_mdb_dot_clickhouse_dot_v1_dot_resource__preset__pb2.ResourcePreset.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_clickhouse_dot_v1_dot_resource__preset__service__pb2.ListResourcePresetsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_mdb_dot_clickhouse_dot_v1_dot_resource__preset__service__pb2.ListResourcePresetsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.mdb.clickhouse.v1.ResourcePresetService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ResourcePresetService(object):
    """A set of methods for managing ResourcePreset resources.
    """

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.mdb.clickhouse.v1.ResourcePresetService/Get',
            yandex_dot_cloud_dot_mdb_dot_clickhouse_dot_v1_dot_resource__preset__service__pb2.GetResourcePresetRequest.SerializeToString,
            yandex_dot_cloud_dot_mdb_dot_clickhouse_dot_v1_dot_resource__preset__pb2.ResourcePreset.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.mdb.clickhouse.v1.ResourcePresetService/List',
            yandex_dot_cloud_dot_mdb_dot_clickhouse_dot_v1_dot_resource__preset__service__pb2.ListResourcePresetsRequest.SerializeToString,
            yandex_dot_cloud_dot_mdb_dot_clickhouse_dot_v1_dot_resource__preset__service__pb2.ListResourcePresetsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
