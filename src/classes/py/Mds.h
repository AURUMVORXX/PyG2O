#ifndef _PYMDS_H
#define _PYMDS_H

#include <classes/sq/Mds.h>
#include <pybind11/embed.h>
namespace py = pybind11;

class PyMds
{
    
public:
    
    static int id(std::string mdsName)      { return nonut::Mds::get()->id(mdsName); }
    static std::string name(int mdsId)      { return nonut::Mds::get()->name(mdsId); }
};

#endif