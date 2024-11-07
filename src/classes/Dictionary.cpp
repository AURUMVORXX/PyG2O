
#include <sqapi.h>
#include <pybind11/embed.h>
#include "Dictionary.h"
#include <NoNut/core/CustomTypes.h>
namespace py = pybind11;


Sqrat::Table* PyDictionary::toSqObject(py::dict value)
{
    Sqrat::Table* result = new Sqrat::Table(Sqrat::DefaultVM::Get());
    HSQUIRRELVM vm = Sqrat::DefaultVM::Get();
    
    for(auto item : value)
    {
        std::string key = item.first.cast<std::string>();
                
         if (py::isinstance<py::str>(item.second))
            result->SetValue(key.c_str(), item.second.cast<std::string>().c_str());
        else if (py::isinstance<py::int_>(item.second))
            result->SetValue(key.c_str(), item.second.cast<int>());
        else if (py::isinstance<py::float_>(item.second))
            result->SetValue(key.c_str(), item.second.cast<float>());
        else if (py::isinstance<py::bool_>(item.second))
            result->SetValue(key.c_str(), item.second.cast<bool>());
        else if (py::isinstance<py::dict>(item.second))
        {
            Sqrat::Table *pTable = PyDictionary::toSqObject(item.second.cast<py::dict>());
            
            sq_pushobject(vm, result->GetObject());
            sq_pushstring(vm, key.c_str(), -1);
            sq_pushobject(vm, pTable->GetObject());
            sq_newslot(vm, -3, false);
            sq_pop(vm,1);
            
            delete pTable;
        }
    }
    
    return result;
};