# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.iot.devices.v1 import device_pb2 as yandex_dot_cloud_dot_iot_dot_devices_dot_v1_dot_device__pb2
from yandex.cloud.iot.devices.v1 import device_service_pb2 as yandex_dot_cloud_dot_iot_dot_devices_dot_v1_dot_device__service__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2


class DeviceServiceStub(object):
    """A set of methods for managing devices.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/yandex.cloud.iot.devices.v1.DeviceService/Get',
                request_serializer=yandex_dot_cloud_dot_iot_dot_devices_dot_v1_dot_device__service__pb2.GetDeviceRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_iot_dot_devices_dot_v1_dot_device__pb2.Device.FromString,
                )
        self.List = channel.unary_unary(
                '/yandex.cloud.iot.devices.v1.DeviceService/List',
                request_serializer=yandex_dot_cloud_dot_iot_dot_devices_dot_v1_dot_device__service__pb2.ListDevicesRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_iot_dot_devices_dot_v1_dot_device__service__pb2.ListDevicesResponse.FromString,
                )
        self.Create = channel.unary_unary(
                '/yandex.cloud.iot.devices.v1.DeviceService/Create',
                request_serializer=yandex_dot_cloud_dot_iot_dot_devices_dot_v1_dot_device__service__pb2.CreateDeviceRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Update = channel.unary_unary(
                '/yandex.cloud.iot.devices.v1.DeviceService/Update',
                request_serializer=yandex_dot_cloud_dot_iot_dot_devices_dot_v1_dot_device__service__pb2.UpdateDeviceRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Delete = channel.unary_unary(
                '/yandex.cloud.iot.devices.v1.DeviceService/Delete',
                request_serializer=yandex_dot_cloud_dot_iot_dot_devices_dot_v1_dot_device__service__pb2.DeleteDeviceRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.ListCertificates = channel.unary_unary(
                '/yandex.cloud.iot.devices.v1.DeviceService/ListCertificates',
                request_serializer=yandex_dot_cloud_dot_iot_dot_devices_dot_v1_dot_device__service__pb2.ListDeviceCertificatesRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_iot_dot_devices_dot_v1_dot_device__service__pb2.ListDeviceCertificatesResponse.FromString,
                )
        self.AddCertificate = channel.unary_unary(
                '/yandex.cloud.iot.devices.v1.DeviceService/AddCertificate',
                request_serializer=yandex_dot_cloud_dot_iot_dot_devices_dot_v1_dot_device__service__pb2.AddDeviceCertificateRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.DeleteCertificate = channel.unary_unary(
                '/yandex.cloud.iot.devices.v1.DeviceService/DeleteCertificate',
                request_serializer=yandex_dot_cloud_dot_iot_dot_devices_dot_v1_dot_device__service__pb2.DeleteDeviceCertificateRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.ListPasswords = channel.unary_unary(
                '/yandex.cloud.iot.devices.v1.DeviceService/ListPasswords',
                request_serializer=yandex_dot_cloud_dot_iot_dot_devices_dot_v1_dot_device__service__pb2.ListDevicePasswordsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_iot_dot_devices_dot_v1_dot_device__service__pb2.ListDevicePasswordsResponse.FromString,
                )
        self.AddPassword = channel.unary_unary(
                '/yandex.cloud.iot.devices.v1.DeviceService/AddPassword',
                request_serializer=yandex_dot_cloud_dot_iot_dot_devices_dot_v1_dot_device__service__pb2.AddDevicePasswordRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.DeletePassword = channel.unary_unary(
                '/yandex.cloud.iot.devices.v1.DeviceService/DeletePassword',
                request_serializer=yandex_dot_cloud_dot_iot_dot_devices_dot_v1_dot_device__service__pb2.DeleteDevicePasswordRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.ListOperations = channel.unary_unary(
                '/yandex.cloud.iot.devices.v1.DeviceService/ListOperations',
                request_serializer=yandex_dot_cloud_dot_iot_dot_devices_dot_v1_dot_device__service__pb2.ListDeviceOperationsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_iot_dot_devices_dot_v1_dot_device__service__pb2.ListDeviceOperationsResponse.FromString,
                )


class DeviceServiceServicer(object):
    """A set of methods for managing devices.
    """

    def Get(self, request, context):
        """Returns the specified device.

        To get the list of available devices, make a [List] request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Retrieves the list of devices in the specified registry.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Creates a device in the specified registry.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Updates the specified device.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Deletes the specified device.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListCertificates(self, request, context):
        """Retrieves the list of device certificates for the specified device.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddCertificate(self, request, context):
        """Adds a certificate.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteCertificate(self, request, context):
        """Deletes the specified device certificate.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListPasswords(self, request, context):
        """Retrieves the list of passwords for the specified device.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddPassword(self, request, context):
        """Adds password for the specified device.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeletePassword(self, request, context):
        """Deletes the specified password.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListOperations(self, request, context):
        """Lists operations for the specified device.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DeviceServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_iot_dot_devices_dot_v1_dot_device__service__pb2.GetDeviceRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_iot_dot_devices_dot_v1_dot_device__pb2.Device.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_iot_dot_devices_dot_v1_dot_device__service__pb2.ListDevicesRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_iot_dot_devices_dot_v1_dot_device__service__pb2.ListDevicesResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=yandex_dot_cloud_dot_iot_dot_devices_dot_v1_dot_device__service__pb2.CreateDeviceRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=yandex_dot_cloud_dot_iot_dot_devices_dot_v1_dot_device__service__pb2.UpdateDeviceRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_iot_dot_devices_dot_v1_dot_device__service__pb2.DeleteDeviceRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'ListCertificates': grpc.unary_unary_rpc_method_handler(
                    servicer.ListCertificates,
                    request_deserializer=yandex_dot_cloud_dot_iot_dot_devices_dot_v1_dot_device__service__pb2.ListDeviceCertificatesRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_iot_dot_devices_dot_v1_dot_device__service__pb2.ListDeviceCertificatesResponse.SerializeToString,
            ),
            'AddCertificate': grpc.unary_unary_rpc_method_handler(
                    servicer.AddCertificate,
                    request_deserializer=yandex_dot_cloud_dot_iot_dot_devices_dot_v1_dot_device__service__pb2.AddDeviceCertificateRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'DeleteCertificate': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteCertificate,
                    request_deserializer=yandex_dot_cloud_dot_iot_dot_devices_dot_v1_dot_device__service__pb2.DeleteDeviceCertificateRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'ListPasswords': grpc.unary_unary_rpc_method_handler(
                    servicer.ListPasswords,
                    request_deserializer=yandex_dot_cloud_dot_iot_dot_devices_dot_v1_dot_device__service__pb2.ListDevicePasswordsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_iot_dot_devices_dot_v1_dot_device__service__pb2.ListDevicePasswordsResponse.SerializeToString,
            ),
            'AddPassword': grpc.unary_unary_rpc_method_handler(
                    servicer.AddPassword,
                    request_deserializer=yandex_dot_cloud_dot_iot_dot_devices_dot_v1_dot_device__service__pb2.AddDevicePasswordRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'DeletePassword': grpc.unary_unary_rpc_method_handler(
                    servicer.DeletePassword,
                    request_deserializer=yandex_dot_cloud_dot_iot_dot_devices_dot_v1_dot_device__service__pb2.DeleteDevicePasswordRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'ListOperations': grpc.unary_unary_rpc_method_handler(
                    servicer.ListOperations,
                    request_deserializer=yandex_dot_cloud_dot_iot_dot_devices_dot_v1_dot_device__service__pb2.ListDeviceOperationsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_iot_dot_devices_dot_v1_dot_device__service__pb2.ListDeviceOperationsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.iot.devices.v1.DeviceService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DeviceService(object):
    """A set of methods for managing devices.
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.iot.devices.v1.DeviceService/Get',
            yandex_dot_cloud_dot_iot_dot_devices_dot_v1_dot_device__service__pb2.GetDeviceRequest.SerializeToString,
            yandex_dot_cloud_dot_iot_dot_devices_dot_v1_dot_device__pb2.Device.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.iot.devices.v1.DeviceService/List',
            yandex_dot_cloud_dot_iot_dot_devices_dot_v1_dot_device__service__pb2.ListDevicesRequest.SerializeToString,
            yandex_dot_cloud_dot_iot_dot_devices_dot_v1_dot_device__service__pb2.ListDevicesResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.iot.devices.v1.DeviceService/Create',
            yandex_dot_cloud_dot_iot_dot_devices_dot_v1_dot_device__service__pb2.CreateDeviceRequest.SerializeToString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.iot.devices.v1.DeviceService/Update',
            yandex_dot_cloud_dot_iot_dot_devices_dot_v1_dot_device__service__pb2.UpdateDeviceRequest.SerializeToString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.iot.devices.v1.DeviceService/Delete',
            yandex_dot_cloud_dot_iot_dot_devices_dot_v1_dot_device__service__pb2.DeleteDeviceRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListCertificates(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.iot.devices.v1.DeviceService/ListCertificates',
            yandex_dot_cloud_dot_iot_dot_devices_dot_v1_dot_device__service__pb2.ListDeviceCertificatesRequest.SerializeToString,
            yandex_dot_cloud_dot_iot_dot_devices_dot_v1_dot_device__service__pb2.ListDeviceCertificatesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddCertificate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.iot.devices.v1.DeviceService/AddCertificate',
            yandex_dot_cloud_dot_iot_dot_devices_dot_v1_dot_device__service__pb2.AddDeviceCertificateRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteCertificate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.iot.devices.v1.DeviceService/DeleteCertificate',
            yandex_dot_cloud_dot_iot_dot_devices_dot_v1_dot_device__service__pb2.DeleteDeviceCertificateRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListPasswords(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.iot.devices.v1.DeviceService/ListPasswords',
            yandex_dot_cloud_dot_iot_dot_devices_dot_v1_dot_device__service__pb2.ListDevicePasswordsRequest.SerializeToString,
            yandex_dot_cloud_dot_iot_dot_devices_dot_v1_dot_device__service__pb2.ListDevicePasswordsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddPassword(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.iot.devices.v1.DeviceService/AddPassword',
            yandex_dot_cloud_dot_iot_dot_devices_dot_v1_dot_device__service__pb2.AddDevicePasswordRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeletePassword(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.iot.devices.v1.DeviceService/DeletePassword',
            yandex_dot_cloud_dot_iot_dot_devices_dot_v1_dot_device__service__pb2.DeleteDevicePasswordRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListOperations(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.iot.devices.v1.DeviceService/ListOperations',
            yandex_dot_cloud_dot_iot_dot_devices_dot_v1_dot_device__service__pb2.ListDeviceOperationsRequest.SerializeToString,
            yandex_dot_cloud_dot_iot_dot_devices_dot_v1_dot_device__service__pb2.ListDeviceOperationsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
