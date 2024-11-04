#include <sqapi.h>
#include <pybind11/embed.h>
#include "sqcontainers.h"

namespace py = pybind11;
using namespace pybind11::literals;

py::dict sqParseTable(Sqrat::Table tab)
{
    py::dict result;
    Sqrat::Object::iterator tabIterator;
    int i = 0;
    
    while (tab.Next(tabIterator))
    {
        HSQOBJECT key   = tabIterator.getKey();
        HSQOBJECT value = tabIterator.getValue();
        
        if (key._type != OT_STRING)
            continue;
        
        switch(value._type)
        {
            case OT_STRING:
                result[sq_objtostring(&key)] = sq_objtostring(&value);
                break;
            case OT_INTEGER:
                result[sq_objtostring(&key)] = sq_objtointeger(&value);
                break;
            case OT_FLOAT:
                result[sq_objtostring(&key)] = sq_objtofloat(&value);
                break;
            case OT_TABLE:
                result[sq_objtostring(&key)] = sqParseTable(Sqrat::Table(value));
                break;
                
            default:
                continue;
        }
    }
    
    return result;
}