#include <pybind11/embed.h>
#include "classes/py/Packet.h"
#include <NoNut/core/Constant.h>

namespace py = pybind11;

PYBIND11_EMBEDDED_MODULE(sqg2o, m) {
    py::class_<PyPacket>(m, "Packet")
        .def(py::init<>())
        .def("reset",           &PyPacket::reset)
        .def("send",            &PyPacket::send)
        .def("sendToAll",       &PyPacket::sendToAll)
        .def("writeInt8",       &PyPacket::writeInt8)
        .def("writeUInt8",      &PyPacket::writeUInt8)
        .def("writeInt16",      &PyPacket::writeInt16)
        .def("writeUInt16",     &PyPacket::writeUInt16)
        .def("writeInt32",      &PyPacket::writeInt32)
        .def("writeUInt32",     &PyPacket::writeUInt32)
        .def("writeFloat",      &PyPacket::writeFloat)
        .def("writeBool",       &PyPacket::writeBool)
        .def("writeString",     &PyPacket::writeString)
        .def("readInt8",        &PyPacket::readInt8)
        .def("readUInt8",       &PyPacket::readUInt8)
        .def("readInt16",       &PyPacket::readInt16)
        .def("readUInt16",      &PyPacket::readUInt16)
        .def("readInt32",       &PyPacket::readInt32)
        .def("readUInt32",      &PyPacket::readUInt32)
        .def("readFloat",       &PyPacket::readFloat)
        .def("readBool",        &PyPacket::readBool)
        .def("readString",      &PyPacket::readString)
        .def("__del__",         &PyPacket::del)
        
        .def_property_readonly("bitsUsed", &PyPacket::getBitsUsed)
        .def_property_readonly("bytesUsed", &PyPacket::getBytesUsed);
}