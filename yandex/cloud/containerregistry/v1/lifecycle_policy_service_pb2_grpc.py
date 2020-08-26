# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.containerregistry.v1 import lifecycle_policy_pb2 as yandex_dot_cloud_dot_containerregistry_dot_v1_dot_lifecycle__policy__pb2
from yandex.cloud.containerregistry.v1 import lifecycle_policy_service_pb2 as yandex_dot_cloud_dot_containerregistry_dot_v1_dot_lifecycle__policy__service__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2


class LifecyclePolicyServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/yandex.cloud.containerregistry.v1.LifecyclePolicyService/Get',
                request_serializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_lifecycle__policy__service__pb2.GetLifecyclePolicyRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_lifecycle__policy__pb2.LifecyclePolicy.FromString,
                )
        self.List = channel.unary_unary(
                '/yandex.cloud.containerregistry.v1.LifecyclePolicyService/List',
                request_serializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_lifecycle__policy__service__pb2.ListLifecyclePoliciesRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_lifecycle__policy__service__pb2.ListLifecyclePoliciesResponse.FromString,
                )
        self.Create = channel.unary_unary(
                '/yandex.cloud.containerregistry.v1.LifecyclePolicyService/Create',
                request_serializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_lifecycle__policy__service__pb2.CreateLifecyclePolicyRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Update = channel.unary_unary(
                '/yandex.cloud.containerregistry.v1.LifecyclePolicyService/Update',
                request_serializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_lifecycle__policy__service__pb2.UpdateLifecyclePolicyRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Delete = channel.unary_unary(
                '/yandex.cloud.containerregistry.v1.LifecyclePolicyService/Delete',
                request_serializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_lifecycle__policy__service__pb2.DeleteLifecyclePolicyRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.DryRun = channel.unary_unary(
                '/yandex.cloud.containerregistry.v1.LifecyclePolicyService/DryRun',
                request_serializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_lifecycle__policy__service__pb2.DryRunLifecyclePolicyRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.GetDryRunResult = channel.unary_unary(
                '/yandex.cloud.containerregistry.v1.LifecyclePolicyService/GetDryRunResult',
                request_serializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_lifecycle__policy__service__pb2.GetDryRunLifecyclePolicyResultRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_lifecycle__policy__service__pb2.DryRunLifecyclePolicyResult.FromString,
                )
        self.ListDryRunResults = channel.unary_unary(
                '/yandex.cloud.containerregistry.v1.LifecyclePolicyService/ListDryRunResults',
                request_serializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_lifecycle__policy__service__pb2.ListDryRunLifecyclePolicyResultsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_lifecycle__policy__service__pb2.ListDryRunLifecyclePolicyResultsResponse.FromString,
                )
        self.ListDryRunResultAffectedImages = channel.unary_unary(
                '/yandex.cloud.containerregistry.v1.LifecyclePolicyService/ListDryRunResultAffectedImages',
                request_serializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_lifecycle__policy__service__pb2.ListDryRunLifecyclePolicyResultAffectedImagesRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_lifecycle__policy__service__pb2.ListDryRunLifecyclePolicyResultAffectedImagesResponse.FromString,
                )


class LifecyclePolicyServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DryRun(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDryRunResult(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListDryRunResults(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListDryRunResultAffectedImages(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LifecyclePolicyServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_lifecycle__policy__service__pb2.GetLifecyclePolicyRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_lifecycle__policy__pb2.LifecyclePolicy.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_lifecycle__policy__service__pb2.ListLifecyclePoliciesRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_lifecycle__policy__service__pb2.ListLifecyclePoliciesResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_lifecycle__policy__service__pb2.CreateLifecyclePolicyRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_lifecycle__policy__service__pb2.UpdateLifecyclePolicyRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_lifecycle__policy__service__pb2.DeleteLifecyclePolicyRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'DryRun': grpc.unary_unary_rpc_method_handler(
                    servicer.DryRun,
                    request_deserializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_lifecycle__policy__service__pb2.DryRunLifecyclePolicyRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'GetDryRunResult': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDryRunResult,
                    request_deserializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_lifecycle__policy__service__pb2.GetDryRunLifecyclePolicyResultRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_lifecycle__policy__service__pb2.DryRunLifecyclePolicyResult.SerializeToString,
            ),
            'ListDryRunResults': grpc.unary_unary_rpc_method_handler(
                    servicer.ListDryRunResults,
                    request_deserializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_lifecycle__policy__service__pb2.ListDryRunLifecyclePolicyResultsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_lifecycle__policy__service__pb2.ListDryRunLifecyclePolicyResultsResponse.SerializeToString,
            ),
            'ListDryRunResultAffectedImages': grpc.unary_unary_rpc_method_handler(
                    servicer.ListDryRunResultAffectedImages,
                    request_deserializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_lifecycle__policy__service__pb2.ListDryRunLifecyclePolicyResultAffectedImagesRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_lifecycle__policy__service__pb2.ListDryRunLifecyclePolicyResultAffectedImagesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.containerregistry.v1.LifecyclePolicyService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class LifecyclePolicyService(object):
    """Missing associated documentation comment in .proto file."""

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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.containerregistry.v1.LifecyclePolicyService/Get',
            yandex_dot_cloud_dot_containerregistry_dot_v1_dot_lifecycle__policy__service__pb2.GetLifecyclePolicyRequest.SerializeToString,
            yandex_dot_cloud_dot_containerregistry_dot_v1_dot_lifecycle__policy__pb2.LifecyclePolicy.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.containerregistry.v1.LifecyclePolicyService/List',
            yandex_dot_cloud_dot_containerregistry_dot_v1_dot_lifecycle__policy__service__pb2.ListLifecyclePoliciesRequest.SerializeToString,
            yandex_dot_cloud_dot_containerregistry_dot_v1_dot_lifecycle__policy__service__pb2.ListLifecyclePoliciesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.containerregistry.v1.LifecyclePolicyService/Create',
            yandex_dot_cloud_dot_containerregistry_dot_v1_dot_lifecycle__policy__service__pb2.CreateLifecyclePolicyRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.containerregistry.v1.LifecyclePolicyService/Update',
            yandex_dot_cloud_dot_containerregistry_dot_v1_dot_lifecycle__policy__service__pb2.UpdateLifecyclePolicyRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.containerregistry.v1.LifecyclePolicyService/Delete',
            yandex_dot_cloud_dot_containerregistry_dot_v1_dot_lifecycle__policy__service__pb2.DeleteLifecyclePolicyRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DryRun(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.containerregistry.v1.LifecyclePolicyService/DryRun',
            yandex_dot_cloud_dot_containerregistry_dot_v1_dot_lifecycle__policy__service__pb2.DryRunLifecyclePolicyRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDryRunResult(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.containerregistry.v1.LifecyclePolicyService/GetDryRunResult',
            yandex_dot_cloud_dot_containerregistry_dot_v1_dot_lifecycle__policy__service__pb2.GetDryRunLifecyclePolicyResultRequest.SerializeToString,
            yandex_dot_cloud_dot_containerregistry_dot_v1_dot_lifecycle__policy__service__pb2.DryRunLifecyclePolicyResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListDryRunResults(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.containerregistry.v1.LifecyclePolicyService/ListDryRunResults',
            yandex_dot_cloud_dot_containerregistry_dot_v1_dot_lifecycle__policy__service__pb2.ListDryRunLifecyclePolicyResultsRequest.SerializeToString,
            yandex_dot_cloud_dot_containerregistry_dot_v1_dot_lifecycle__policy__service__pb2.ListDryRunLifecyclePolicyResultsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListDryRunResultAffectedImages(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.containerregistry.v1.LifecyclePolicyService/ListDryRunResultAffectedImages',
            yandex_dot_cloud_dot_containerregistry_dot_v1_dot_lifecycle__policy__service__pb2.ListDryRunLifecyclePolicyResultAffectedImagesRequest.SerializeToString,
            yandex_dot_cloud_dot_containerregistry_dot_v1_dot_lifecycle__policy__service__pb2.ListDryRunLifecyclePolicyResultAffectedImagesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
