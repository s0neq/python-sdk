# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.access import access_pb2 as yandex_dot_cloud_dot_access_dot_access__pb2
from yandex.cloud.containerregistry.v1 import repository_pb2 as yandex_dot_cloud_dot_containerregistry_dot_v1_dot_repository__pb2
from yandex.cloud.containerregistry.v1 import repository_service_pb2 as yandex_dot_cloud_dot_containerregistry_dot_v1_dot_repository__service__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2


class RepositoryServiceStub(object):
    """A set of methods for managing Repository resources.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/yandex.cloud.containerregistry.v1.RepositoryService/Get',
                request_serializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_repository__service__pb2.GetRepositoryRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_repository__pb2.Repository.FromString,
                )
        self.GetByName = channel.unary_unary(
                '/yandex.cloud.containerregistry.v1.RepositoryService/GetByName',
                request_serializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_repository__service__pb2.GetRepositoryByNameRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_repository__pb2.Repository.FromString,
                )
        self.List = channel.unary_unary(
                '/yandex.cloud.containerregistry.v1.RepositoryService/List',
                request_serializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_repository__service__pb2.ListRepositoriesRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_repository__service__pb2.ListRepositoriesResponse.FromString,
                )
        self.ListAccessBindings = channel.unary_unary(
                '/yandex.cloud.containerregistry.v1.RepositoryService/ListAccessBindings',
                request_serializer=yandex_dot_cloud_dot_access_dot_access__pb2.ListAccessBindingsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_access_dot_access__pb2.ListAccessBindingsResponse.FromString,
                )
        self.SetAccessBindings = channel.unary_unary(
                '/yandex.cloud.containerregistry.v1.RepositoryService/SetAccessBindings',
                request_serializer=yandex_dot_cloud_dot_access_dot_access__pb2.SetAccessBindingsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.UpdateAccessBindings = channel.unary_unary(
                '/yandex.cloud.containerregistry.v1.RepositoryService/UpdateAccessBindings',
                request_serializer=yandex_dot_cloud_dot_access_dot_access__pb2.UpdateAccessBindingsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )


class RepositoryServiceServicer(object):
    """A set of methods for managing Repository resources.
    """

    def Get(self, request, context):
        """Returns the specified Repository resource.

        To get the list of available Repository resources, make a [List] request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetByName(self, request, context):
        """Returns the specified Repository resource.

        To get the list of available Repository resources, make a [List] request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Retrieves the list of Repository resources in the specified registry.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListAccessBindings(self, request, context):
        """access

        Lists access bindings for the specified repository.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetAccessBindings(self, request, context):
        """Sets access bindings for the specified repository.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateAccessBindings(self, request, context):
        """Updates access bindings for the specified repository.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RepositoryServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_repository__service__pb2.GetRepositoryRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_repository__pb2.Repository.SerializeToString,
            ),
            'GetByName': grpc.unary_unary_rpc_method_handler(
                    servicer.GetByName,
                    request_deserializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_repository__service__pb2.GetRepositoryByNameRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_repository__pb2.Repository.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_repository__service__pb2.ListRepositoriesRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_repository__service__pb2.ListRepositoriesResponse.SerializeToString,
            ),
            'ListAccessBindings': grpc.unary_unary_rpc_method_handler(
                    servicer.ListAccessBindings,
                    request_deserializer=yandex_dot_cloud_dot_access_dot_access__pb2.ListAccessBindingsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_access_dot_access__pb2.ListAccessBindingsResponse.SerializeToString,
            ),
            'SetAccessBindings': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAccessBindings,
                    request_deserializer=yandex_dot_cloud_dot_access_dot_access__pb2.SetAccessBindingsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'UpdateAccessBindings': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateAccessBindings,
                    request_deserializer=yandex_dot_cloud_dot_access_dot_access__pb2.UpdateAccessBindingsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.containerregistry.v1.RepositoryService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RepositoryService(object):
    """A set of methods for managing Repository resources.
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.containerregistry.v1.RepositoryService/Get',
            yandex_dot_cloud_dot_containerregistry_dot_v1_dot_repository__service__pb2.GetRepositoryRequest.SerializeToString,
            yandex_dot_cloud_dot_containerregistry_dot_v1_dot_repository__pb2.Repository.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetByName(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.containerregistry.v1.RepositoryService/GetByName',
            yandex_dot_cloud_dot_containerregistry_dot_v1_dot_repository__service__pb2.GetRepositoryByNameRequest.SerializeToString,
            yandex_dot_cloud_dot_containerregistry_dot_v1_dot_repository__pb2.Repository.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.containerregistry.v1.RepositoryService/List',
            yandex_dot_cloud_dot_containerregistry_dot_v1_dot_repository__service__pb2.ListRepositoriesRequest.SerializeToString,
            yandex_dot_cloud_dot_containerregistry_dot_v1_dot_repository__service__pb2.ListRepositoriesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListAccessBindings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.containerregistry.v1.RepositoryService/ListAccessBindings',
            yandex_dot_cloud_dot_access_dot_access__pb2.ListAccessBindingsRequest.SerializeToString,
            yandex_dot_cloud_dot_access_dot_access__pb2.ListAccessBindingsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetAccessBindings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.containerregistry.v1.RepositoryService/SetAccessBindings',
            yandex_dot_cloud_dot_access_dot_access__pb2.SetAccessBindingsRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateAccessBindings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.containerregistry.v1.RepositoryService/UpdateAccessBindings',
            yandex_dot_cloud_dot_access_dot_access__pb2.UpdateAccessBindingsRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
