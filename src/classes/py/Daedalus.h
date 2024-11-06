#ifndef _PYDAEDALUS_H_
#define _PYDAEDALUS_H_

#include <classes/sq/Daedalus.h>
#include <pybind11/embed.h>
#include <iostream>
namespace py = pybind11;

class PyDaedalus
{
    
public:
    
    //static nonut::Int index(nonut::String value)       { return nonut::Daedalus::get()->index(value); }
    static nonut::Int index(nonut::String value)         { std::cout << nonut::Daedalus::get()->index(value) << std::endl;return 5; }
    static py::dict symbol(nonut::String value)          { return nonut::Daedalus::get()->symbol(value).data; }
    static py::dict instance(nonut::String value)        { return nonut::Daedalus::get()->instance(value).data; }
};

#endif