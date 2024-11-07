#include <pybind11/embed.h>
#include "classes/py/Packet.h"
#include "classes/py/DamageDescription.h"
#include "classes/py/ItemGround.h"
#include "classes/py/Daedalus.h"
#include "classes/py/Sky.h"
#include "classes/py/ItemsGround.h"
#include <NoNut/core/Constant.h>

namespace py = pybind11;

PYBIND11_EMBEDDED_MODULE(sqg2o, m) {
    
    py::class_<PyPacket>(m, "Packet")
        .def(py::init<>())
        .def("reset",                               &PyPacket::reset)
        .def("send",                                &PyPacket::send)
        .def("sendToAll",                           &PyPacket::sendToAll)
        .def("writeInt8",                           &PyPacket::writeInt8)
        .def("writeUInt8",                          &PyPacket::writeUInt8)
        .def("writeInt16",                          &PyPacket::writeInt16)
        .def("writeUInt16",                         &PyPacket::writeUInt16)
        .def("writeInt32",                          &PyPacket::writeInt32)
        .def("writeUInt32",                         &PyPacket::writeUInt32)
        .def("writeFloat",                          &PyPacket::writeFloat)
        .def("writeBool",                           &PyPacket::writeBool)
        .def("writeString",                         &PyPacket::writeString)
        .def("readInt8",                            &PyPacket::readInt8)
        .def("readUInt8",                           &PyPacket::readUInt8)
        .def("readInt16",                           &PyPacket::readInt16)
        .def("readUInt16",                          &PyPacket::readUInt16)
        .def("readInt32",                           &PyPacket::readInt32)
        .def("readUInt32",                          &PyPacket::readUInt32)
        .def("readFloat",                           &PyPacket::readFloat)
        .def("readBool",                            &PyPacket::readBool)
        .def("readString",                          &PyPacket::readString)
        .def("__del__",                             &PyPacket::del)
        
        .def_property_readonly("bitsUsed",          &PyPacket::getBitsUsed)
        .def_property_readonly("bytesUsed",         &PyPacket::getBytesUsed);
        
// -------------------------------------------------------------------------
        
    py::class_<PyDamageDescription>(m, "DamageDescription")
        
        .def_property_readonly("item_instance",     &PyDamageDescription::getItemInstance)
        
        .def_property("flags",                      &PyDamageDescription::getFlags,         &PyDamageDescription::setFlags, py::return_value_policy::reference_internal)
        .def_property("damage",                     &PyDamageDescription::getDamage,        &PyDamageDescription::setDamage, py::return_value_policy::reference_internal)
        .def_property("distance",                   &PyDamageDescription::getDistance,      &PyDamageDescription::setDistance, py::return_value_policy::reference_internal)
        .def_property("spell_id",                   &PyDamageDescription::getSpellId,       &PyDamageDescription::setSpellId, py::return_value_policy::reference_internal)
        .def_property("spell_level",                &PyDamageDescription::getSpellLevel,    &PyDamageDescription::setSpellLevel, py::return_value_policy::reference_internal)
        .def_property("node",                       &PyDamageDescription::getNode,          &PyDamageDescription::setNode, py::return_value_policy::reference_internal);
        
// -------------------------------------------------------------------------

    py::class_<PyItemGround>(m, "ItemGround")
        .def("__del__",                             &PyItemGround::del)
        
        .def("getPosition",                         &PyItemGround::getPosition)
        .def("getRotation",                         &PyItemGround::getRotation)
        
        .def_property_readonly("id",                &PyItemGround::getId)
        .def_property_readonly("instance",          &PyItemGround::getInstance)
        .def_property_readonly("amount",            &PyItemGround::getAmount)
        .def_property_readonly("world",             &PyItemGround::getWorld)
        
        .def_property("virtualWorld",               &PyItemGround::getVirtualWorld,         &PyItemGround::setVirtualWorld, py::return_value_policy::reference_internal);
        
// -------------------------------------------------------------------------

    py::class_<PyDaedalus>(m, "Daedalus")
        .def_static("index",                        [](std::string value){ return PyDaedalus::index(value); })
        .def_static("symbol",                       [](std::string value){ return PyDaedalus::symbol(value); })
        .def_static("instance",                     [](std::string value){ return PyDaedalus::instance(value); });
        
// -------------------------------------------------------------------------

    py::class_<PySky>(m, "Sky")
        .def_property_static("weather",             [](py::object){ return PySky::getWeather(); }, [](py::object, int value) { PySky::setWeather(value); })
        .def_property_static("raining",             [](py::object){ return PySky::getRaining(); }, [](py::object, int value) { PySky::setRaining(value); })
        .def_property_static("renderLightning",     [](py::object){ return PySky::getRenderLightning(); }, [](py::object, int value) { PySky::setRenderLightning(value); })
        .def_property_static("windScale",           [](py::object){ return PySky::getWindScale(); }, [](py::object, int value) { PySky::setWindScale(value); })
        .def_property_static("dontRain",            [](py::object){ return PySky::getDontRain(); }, [](py::object, int value) { PySky::setDontRain(value); })
        
        .def_static("setRainStartTime",             [](int hour, int min){ return PySky::setRainStartTime(hour, min); })
        .def_static("setRainStopTime",              [](int hour, int min){ return PySky::setRainStopTime(hour, min); })
        .def_static("getRainStartTime",             [](){ return PySky::getRainStartTime(); })
        .def_static("getRainStopTime",              [](){ return PySky::getRainStopTime(); });
        
// -------------------------------------------------------------------------

    py::class_<PyItemsGround>(m, "ItemsGround")
    
        .def_static("getById",                      [](int value){ return PyItemsGround::getById(value); })
        .def_static("create",                       [](py::dict value){ return PyItemsGround::create(value); })
        .def_static("destroy",                      [](int value){ return PyItemsGround::destroy(value); });
}