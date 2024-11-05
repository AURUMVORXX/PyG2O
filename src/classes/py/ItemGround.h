#ifndef _PY_ITEMGROUND_H_
#define _PY_ITEMGROUND_H_

#include <pybind11/embed.h>
#include <classes/sq/ItemGround.h>

namespace py = pybind11;

class PyItemGround
{
private:
    nonut::ItemGround *sqobj;
    
public:
    PyItemGround()                              { sqobj = new nonut::ItemGround(); };
    PyItemGround(SQObject obj)                  { sqobj = new nonut::ItemGround(obj); }
    
    py::tuple getPosition()                     { return py::make_tuple(sqobj->getPosition().toTuple()); }
    py::tuple getRotation()                     { return py::make_tuple(sqobj->getRotation().toTuple()); }
    
    nonut::Int getId()                          { return sqobj->id; }
    nonut::String getInstance()                 { return sqobj->instance; }
    nonut::Int getAmount()                      { return sqobj->amount; }
    nonut::String getWorld()                    { return sqobj->world; }
    nonut::Int getVirtualWorld()                { return sqobj->virtualWorld; }
    
    void setVirtualWorld(nonut::Int value)      { sqobj->virtualWorld = value; }
    
    void del()                                  { delete sqobj; }
};

#endif