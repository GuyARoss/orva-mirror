// Code generated by protoc-gen-go. DO NOT EDIT.
// source: service.proto

package grpcSkill

import (
	context "context"
	fmt "fmt"
	proto "github.com/golang/protobuf/proto"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
	math "math"
)

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.ProtoPackageIsVersion3 // please upgrade the proto package

type ProcessResponse struct {
	ForwardAddress       string   `protobuf:"bytes,1,opt,name=ForwardAddress,proto3" json:"ForwardAddress,omitempty"`
	SubsetID             string   `protobuf:"bytes,2,opt,name=SubsetID,proto3" json:"SubsetID,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *ProcessResponse) Reset()         { *m = ProcessResponse{} }
func (m *ProcessResponse) String() string { return proto.CompactTextString(m) }
func (*ProcessResponse) ProtoMessage()    {}
func (*ProcessResponse) Descriptor() ([]byte, []int) {
	return fileDescriptor_a0b84a42fa06f626, []int{0}
}

func (m *ProcessResponse) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_ProcessResponse.Unmarshal(m, b)
}
func (m *ProcessResponse) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_ProcessResponse.Marshal(b, m, deterministic)
}
func (m *ProcessResponse) XXX_Merge(src proto.Message) {
	xxx_messageInfo_ProcessResponse.Merge(m, src)
}
func (m *ProcessResponse) XXX_Size() int {
	return xxx_messageInfo_ProcessResponse.Size(m)
}
func (m *ProcessResponse) XXX_DiscardUnknown() {
	xxx_messageInfo_ProcessResponse.DiscardUnknown(m)
}

var xxx_messageInfo_ProcessResponse proto.InternalMessageInfo

func (m *ProcessResponse) GetForwardAddress() string {
	if m != nil {
		return m.ForwardAddress
	}
	return ""
}

func (m *ProcessResponse) GetSubsetID() string {
	if m != nil {
		return m.SubsetID
	}
	return ""
}

type ProcessRequest struct {
	Message              string   `protobuf:"bytes,1,opt,name=Message,proto3" json:"Message,omitempty"`
	TransactionID        string   `protobuf:"bytes,2,opt,name=TransactionID,proto3" json:"TransactionID,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *ProcessRequest) Reset()         { *m = ProcessRequest{} }
func (m *ProcessRequest) String() string { return proto.CompactTextString(m) }
func (*ProcessRequest) ProtoMessage()    {}
func (*ProcessRequest) Descriptor() ([]byte, []int) {
	return fileDescriptor_a0b84a42fa06f626, []int{1}
}

func (m *ProcessRequest) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_ProcessRequest.Unmarshal(m, b)
}
func (m *ProcessRequest) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_ProcessRequest.Marshal(b, m, deterministic)
}
func (m *ProcessRequest) XXX_Merge(src proto.Message) {
	xxx_messageInfo_ProcessRequest.Merge(m, src)
}
func (m *ProcessRequest) XXX_Size() int {
	return xxx_messageInfo_ProcessRequest.Size(m)
}
func (m *ProcessRequest) XXX_DiscardUnknown() {
	xxx_messageInfo_ProcessRequest.DiscardUnknown(m)
}

var xxx_messageInfo_ProcessRequest proto.InternalMessageInfo

func (m *ProcessRequest) GetMessage() string {
	if m != nil {
		return m.Message
	}
	return ""
}

func (m *ProcessRequest) GetTransactionID() string {
	if m != nil {
		return m.TransactionID
	}
	return ""
}

func init() {
	proto.RegisterType((*ProcessResponse)(nil), "grpcSkill.ProcessResponse")
	proto.RegisterType((*ProcessRequest)(nil), "grpcSkill.ProcessRequest")
}

func init() { proto.RegisterFile("service.proto", fileDescriptor_a0b84a42fa06f626) }

var fileDescriptor_a0b84a42fa06f626 = []byte{
	// 195 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0xe2, 0xe2, 0x2d, 0x4e, 0x2d, 0x2a,
	0xcb, 0x4c, 0x4e, 0xd5, 0x2b, 0x28, 0xca, 0x2f, 0xc9, 0x17, 0xe2, 0x4c, 0x2f, 0x2a, 0x48, 0x0e,
	0xce, 0xce, 0xcc, 0xc9, 0x51, 0x0a, 0xe5, 0xe2, 0x0f, 0x28, 0xca, 0x4f, 0x4e, 0x2d, 0x2e, 0x0e,
	0x4a, 0x2d, 0x2e, 0xc8, 0xcf, 0x2b, 0x4e, 0x15, 0x52, 0xe3, 0xe2, 0x73, 0xcb, 0x2f, 0x2a, 0x4f,
	0x2c, 0x4a, 0x71, 0x4c, 0x49, 0x29, 0x4a, 0x2d, 0x2e, 0x96, 0x60, 0x54, 0x60, 0xd4, 0xe0, 0x0c,
	0x42, 0x13, 0x15, 0x92, 0xe2, 0xe2, 0x08, 0x2e, 0x4d, 0x2a, 0x4e, 0x2d, 0xf1, 0x74, 0x91, 0x60,
	0x02, 0xab, 0x80, 0xf3, 0x95, 0x02, 0xb8, 0xf8, 0xe0, 0xc6, 0x16, 0x96, 0xa6, 0x16, 0x97, 0x08,
	0x49, 0x70, 0xb1, 0xfb, 0xa6, 0x16, 0x17, 0x27, 0xa6, 0xa7, 0x42, 0x8d, 0x83, 0x71, 0x85, 0x54,
	0xb8, 0x78, 0x43, 0x8a, 0x12, 0xf3, 0x8a, 0x13, 0x93, 0x4b, 0x32, 0xf3, 0xf3, 0xe0, 0x86, 0xa1,
	0x0a, 0x1a, 0x45, 0x73, 0x21, 0x5c, 0x2d, 0xe4, 0xc7, 0x25, 0x0c, 0x35, 0x1e, 0xcc, 0x87, 0xd9,
	0x21, 0xa9, 0x07, 0x57, 0xa2, 0x87, 0x6a, 0xbd, 0x94, 0x14, 0x36, 0x29, 0x88, 0x87, 0x95, 0x18,
	0x92, 0xd8, 0xc0, 0xe1, 0x62, 0x0c, 0x08, 0x00, 0x00, 0xff, 0xff, 0xd8, 0xca, 0x7a, 0x58, 0x28,
	0x01, 0x00, 0x00,
}

// Reference imports to suppress errors if they are not otherwise used.
var _ context.Context
var _ grpc.ClientConn

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
const _ = grpc.SupportPackageIsVersion4

// GrpcSkillClient is the client API for GrpcSkill service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://godoc.org/google.golang.org/grpc#ClientConn.NewStream.
type GrpcSkillClient interface {
	ProcessSkillRequest(ctx context.Context, in *ProcessRequest, opts ...grpc.CallOption) (*ProcessResponse, error)
}

type grpcSkillClient struct {
	cc *grpc.ClientConn
}

func NewGrpcSkillClient(cc *grpc.ClientConn) GrpcSkillClient {
	return &grpcSkillClient{cc}
}

func (c *grpcSkillClient) ProcessSkillRequest(ctx context.Context, in *ProcessRequest, opts ...grpc.CallOption) (*ProcessResponse, error) {
	out := new(ProcessResponse)
	err := c.cc.Invoke(ctx, "/grpcSkill.grpcSkill/ProcessSkillRequest", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// GrpcSkillServer is the server API for GrpcSkill service.
type GrpcSkillServer interface {
	ProcessSkillRequest(context.Context, *ProcessRequest) (*ProcessResponse, error)
}

// UnimplementedGrpcSkillServer can be embedded to have forward compatible implementations.
type UnimplementedGrpcSkillServer struct {
}

func (*UnimplementedGrpcSkillServer) ProcessSkillRequest(ctx context.Context, req *ProcessRequest) (*ProcessResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ProcessSkillRequest not implemented")
}

func RegisterGrpcSkillServer(s *grpc.Server, srv GrpcSkillServer) {
	s.RegisterService(&_GrpcSkill_serviceDesc, srv)
}

func _GrpcSkill_ProcessSkillRequest_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ProcessRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(GrpcSkillServer).ProcessSkillRequest(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/grpcSkill.grpcSkill/ProcessSkillRequest",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(GrpcSkillServer).ProcessSkillRequest(ctx, req.(*ProcessRequest))
	}
	return interceptor(ctx, in, info, handler)
}

var _GrpcSkill_serviceDesc = grpc.ServiceDesc{
	ServiceName: "grpcSkill.grpcSkill",
	HandlerType: (*GrpcSkillServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "ProcessSkillRequest",
			Handler:    _GrpcSkill_ProcessSkillRequest_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "service.proto",
}
