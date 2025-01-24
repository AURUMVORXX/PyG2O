#ifndef _PYWAY_H_
#define _PYWAY_H_

#include "squirrel/Way.h"

class PyWay
{
private:
    nonut::Way *sqway;
    
public:
    PyWay(std::string world, std::string start, std::string end)       { sqway = new nonut::Way(world, start, end); };
    PyWay(SQObject obj)                                                { if (obj._type == OT_NULL) throw py::type_error("Presented Squirrel Object doesn't exist (type: null)"); sqway = new nonut::Way(obj); }
    
    py::list    getWaypoints()                                         { return sqway->getWaypoints().data; }
    int         getCountWaypoints()                                    { return sqway->getCountWaypoints(); }
    
    std::string getStart()                                             { return sqway->start; }
    std::string getEnd()                                               { return sqway->end; }
    
    void del()                                                         { delete sqway; }
};

#endif