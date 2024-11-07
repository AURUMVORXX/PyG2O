#ifndef _PYITEMSGROUND_H_
#define _PYITEMSGROUND_H_

#include <classes/sq/ItemsGround.h>
#include <classes/py/ItemGround.h>
#include "../Dictionary.h"

class PyItemsGround
{
    
public:
    
    static PyItemGround getById(nonut::Int value)               { return PyItemGround(nonut::ItemsGround::get()->getById(value)); }
    static nonut::Int create(py::dict value)                    
    { 
        Sqrat::Table* pTable    = PyDictionary::toSqObject(value); 
        nonut::Int result       = nonut::ItemsGround::get()->create(pTable->GetObject());
        delete pTable;
        return result;
    }
    static void destroy(nonut::Int value)                       { nonut::ItemsGround::get()->destroy(value); }
};

#endif