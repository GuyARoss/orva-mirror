# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import service_pb2 as service__pb2


class grpcSpeechStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.HandleSpeechRequest = channel.unary_unary(
        '/grpcSpeech.grpcSpeech/HandleSpeechRequest',
        request_serializer=service__pb2.SpeechRequest.SerializeToString,
        response_deserializer=service__pb2.SpeechResponse.FromString,
        )


class grpcSpeechServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def HandleSpeechRequest(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_grpcSpeechServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'HandleSpeechRequest': grpc.unary_unary_rpc_method_handler(
          servicer.HandleSpeechRequest,
          request_deserializer=service__pb2.SpeechRequest.FromString,
          response_serializer=service__pb2.SpeechResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'grpcSpeech.grpcSpeech', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
