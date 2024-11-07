#ifndef _PYDICTIONARY_H_
#define _PYDICTIONARY_H_

#include <pybind11/embed.h>
#include <string>
namespace py = pybind11;

class PyDictionary
{
public:
    
    static Sqrat::Table* toSqObject(py::dict value);
};

#endif