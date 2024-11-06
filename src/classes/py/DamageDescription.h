#ifndef _PYDAMAGEDESCRIPTION_H
#define _PYDAMAGEDESCRIPTION_H

#include <classes/sq/DamageDescription.h>

class PyDamageDescription
{
private:
    nonut::DamageDescription *sqobj;
    
public:
    PyDamageDescription(SQObject obj)           { sqobj = new nonut::DamageDescription(obj); }
    
    nonut::Int getFlags()                       { return sqobj->flags; }
    nonut::Int getDamage()                      { return sqobj->damage; }
    nonut::String getItemInstance()             { return sqobj->item_instance; }
    nonut::Int getDistance()                    { return sqobj->distance; }
    nonut::Int getSpellId()                     { return sqobj->spell_id; }
    nonut::Int getSpellLevel()                  { return sqobj->spell_level; }
    nonut::String getNode()                     { return sqobj->node; }
    
    void setFlags(nonut::Int value)             { sqobj->flags          = value; }
    void setDamage(nonut::Int value)            { sqobj->damage         = value; }
    void setDistance(nonut::Int value)          { sqobj->distance       = value; }
    void setSpellId(nonut::Int value)           { sqobj->spell_id       = value; }
    void setSpellLevel(nonut::Int value)        { sqobj->spell_level    = value; }
    void setNode(nonut::String value)           { sqobj->node           = value; }
    
    void del()                                  { delete sqobj; }
};

#endif