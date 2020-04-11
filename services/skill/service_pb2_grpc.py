# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import service_pb2 as service__pb2


class grpcSkillStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.RegisterCurrentInstance = channel.unary_unary(
        '/grpcSkill.grpcSkill/RegisterCurrentInstance',
        request_serializer=service__pb2.RegisterRequest.SerializeToString,
        response_deserializer=service__pb2.RegisterResponse.FromString,
        )
    self.DetermineSkillFromMessage = channel.unary_unary(
        '/grpcSkill.grpcSkill/DetermineSkillFromMessage',
        request_serializer=service__pb2.SkillDeterminationRequest.SerializeToString,
        response_deserializer=service__pb2.SkillDeterminationResponse.FromString,
        )


class grpcSkillServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def RegisterCurrentInstance(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DetermineSkillFromMessage(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_grpcSkillServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'RegisterCurrentInstance': grpc.unary_unary_rpc_method_handler(
          servicer.RegisterCurrentInstance,
          request_deserializer=service__pb2.RegisterRequest.FromString,
          response_serializer=service__pb2.RegisterResponse.SerializeToString,
      ),
      'DetermineSkillFromMessage': grpc.unary_unary_rpc_method_handler(
          servicer.DetermineSkillFromMessage,
          request_deserializer=service__pb2.SkillDeterminationRequest.FromString,
          response_serializer=service__pb2.SkillDeterminationResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'grpcSkill.grpcSkill', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))