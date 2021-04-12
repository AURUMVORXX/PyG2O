#ifndef _SQAPI_H
#define _SQAPI_H

#include <sqmodule.h>

namespace sqModule
{
	extern HSQUIRRELVM vm;
	extern HSQAPI api;

	extern SQPRINTFUNCTION print;
	extern SQPRINTFUNCTION error;
}

/*vm*/
#define sq_open sqModule::api->open
#define sq_newthread sqModule::api->newthread
#define sq_seterrorhandler sqModule::api->seterrorhandler
#define sq_close sqModule::api->close
#define sq_setforeignptr sqModule::api->setforeignptr
#define sq_getforeignptr sqModule::api->getforeignptr
#define sq_setsharedforeignptr sqModule::api->setsharedforeignptr
#define sq_getsharedforeignptr sqModule::api->getsharedforeignptr
#define sq_setvmreleasehook sqModule::api->setvmreleasehook
#define sq_getvmreleasehook sqModule::api->getvmreleasehook
#define sq_setsharedreleasehook sqModule::api->setsharedreleasehook
#define sq_getsharedreleasehook sqModule::api->getsharedreleasehook
#define sq_setprintfunc sqModule::api->setprintfunc
#define sq_getprintfunc sqModule::api->getprintfunc
#define sq_geterrorfunc sqModule::api->geterrorfunc
#define sq_suspendvm sqModule::api->suspendvm
#define sq_wakeupvm sqModule::api->wakeupvm
#define sq_getvmstate sqModule::api->getvmstate
#define sq_getversion sqModule::api->getversion

/*compiler*/
#define sq_compile sqModule::api->compile
#define sq_compilebuffer sqModule::api->compilebuffer
#define sq_enabledebuginfo sqModule::api->enabledebuginfo
#define sq_notifyallexceptions sqModule::api->notifyallexceptions
#define sq_setcompilererrorhandler sqModule::api->setcompilererrorhandler

/*stack operations*/
#define sq_push sqModule::api->push
#define sq_pop sqModule::api->pop
#define sq_poptop sqModule::api->poptop
#define sq_remove sqModule::api->remove
#define sq_gettop sqModule::api->gettop
#define sq_settop sqModule::api->settop
#define sq_reservestack sqModule::api->reservestack
#define sq_cmp sqModule::api->cmp
#define sq_move sqModule::api->move

/*object creation handling*/
#define sq_newuserdata sqModule::api->newuserdata
#define sq_newtable sqModule::api->newtable
#define sq_newtableex sqModule::api->newtableex
#define sq_newarray sqModule::api->newarray
#define sq_newclosure sqModule::api->newclosure
#define sq_setparamscheck sqModule::api->setparamscheck
#define sq_bindenv sqModule::api->bindenv
#define sq_setclosureroot sqModule::api->setclosureroot
#define sq_getclosureroot sqModule::api->getclosureroot
#define sq_pushstring sqModule::api->pushstring
#define sq_pushfloat sqModule::api->pushfloat
#define sq_pushinteger sqModule::api->pushinteger
#define sq_pushbool sqModule::api->pushbool
#define sq_pushuserpointer sqModule::api->pushuserpointer
#define sq_pushnull sqModule::api->pushnull
#define sq_pushthread sqModule::api->pushthread
#define sq_gettype sqModule::api->gettype
#define sq_typeof sqModule::api->typeof
#define sq_getsize sqModule::api->getsize
#define sq_gethash sqModule::api->gethash
#define sq_getbase sqModule::api->getbase
#define sq_instanceof sqModule::api->instanceof
#define sq_tostring sqModule::api->tostring
#define sq_tobool sqModule::api->tobool
#define sq_getstring sqModule::api->getstring
#define sq_getinteger sqModule::api->getinteger
#define sq_getfloat sqModule::api->getfloat
#define sq_getbool sqModule::api->getbool
#define sq_getthread sqModule::api->getthread
#define sq_getuserpointer sqModule::api->getuserpointer
#define sq_getuserdata sqModule::api->getuserdata
#define sq_settypetag sqModule::api->settypetag
#define sq_gettypetag sqModule::api->gettypetag
#define sq_setreleasehook sqModule::api->setreleasehook
#define sq_getreleasehook sqModule::api->getreleasehook
#define sq_getscratchpad sqModule::api->getscratchpad
#define sq_getfunctioninfo sqModule::api->getfunctioninfo
#define sq_getclosureinfo sqModule::api->getclosureinfo
#define sq_getclosurename sqModule::api->getclosurename
#define sq_setnativeclosurename sqModule::api->setnativeclosurename
#define sq_setinstanceup sqModule::api->setinstanceup
#define sq_getinstanceup sqModule::api->getinstanceup
#define sq_setclassudsize sqModule::api->setclassudsize
#define sq_newclass sqModule::api->newclass
#define sq_createinstance sqModule::api->createinstance
#define sq_setattributes sqModule::api->setattributes
#define sq_getattributes sqModule::api->getattributes
#define sq_getclass sqModule::api->getclass
#define sq_weakref sqModule::api->weakref
#define sq_getdefaultdelegate sqModule::api->getdefaultdelegate
#define sq_getmemberhandle sqModule::api->getmemberhandle
#define sq_getbyhandle sqModule::api->getbyhandle
#define sq_setbyhandle sqModule::api->setbyhandle

/*object manipulation*/
#define sq_pushroottable sqModule::api->pushroottable
#define sq_pushregistrytable sqModule::api->pushregistrytable
#define sq_pushconsttable sqModule::api->pushconsttable
#define sq_setroottable sqModule::api->setroottable
#define sq_setconsttable sqModule::api->setconsttable
#define sq_newslot sqModule::api->newslot
#define sq_deleteslot sqModule::api->deleteslot
#define sq_set sqModule::api->set
#define sq_get sqModule::api->get
#define sq_rawset sqModule::api->rawset
#define sq_rawget sqModule::api->rawget
#define sq_rawdeleteslot sqModule::api->rawdeleteslot
#define sq_newmember sqModule::api->newmember
#define sq_rawnewmember sqModule::api->rawnewmember
#define sq_arrayappend sqModule::api->arrayappend
#define sq_arraypop sqModule::api->arraypop
#define sq_arrayresize sqModule::api->arrayresize
#define sq_arrayreverse sqModule::api->arrayreverse
#define sq_arrayremove sqModule::api->arrayremove
#define sq_arrayinsert sqModule::api->arrayinsert
#define sq_setdelegate sqModule::api->setdelegate
#define sq_getdelegate sqModule::api->getdelegate
#define sq_clone sqModule::api->clone
#define sq_setfreevariable sqModule::api->setfreevariable
#define sq_next sqModule::api->next
#define sq_getweakrefval sqModule::api->getweakrefval
#define sq_clear sqModule::api->clear

/*calls*/
#define sq_call sqModule::api->call
#define sq_resume sqModule::api->resume
#define sq_getlocal sqModule::api->getlocal
#define sq_getcallee sqModule::api->getcallee
#define sq_getfreevariable sqModule::api->getfreevariable
#define sq_throwerror sqModule::api->throwerror
#define sq_throwobject sqModule::api->throwobject
#define sq_reseterror sqModule::api->reseterror
#define sq_getlasterror sqModule::api->getlasterror

/*raw object handling*/
#define sq_getstackobj sqModule::api->getstackobj
#define sq_pushobject sqModule::api->pushobject
#define sq_addref sqModule::api->addref
#define sq_release sqModule::api->release
#define sq_getrefcount sqModule::api->getrefcount
#define sq_resetobject sqModule::api->resetobject
#define sq_objtostring sqModule::api->objtostring
#define sq_objtobool sqModule::api->objtobool
#define sq_objtointeger sqModule::api->objtointeger
#define sq_objtofloat sqModule::api->objtofloat
#define sq_objtouserpointer sqModule::api->objtouserpointer
#define sq_getobjtypetag sqModule::api->getobjtypetag
#define sq_getvmrefcount sqModule::api->getvmrefcount

/*GC*/
#define sq_collectgarbage sqModule::api->collectgarbage
#define sq_resurrectunreachable sqModule::api->resurrectunreachable

/*serialization*/
#define sq_writeclosure sqModule::api->writeclosure
#define sq_readclosure sqModule::api->readclosure

/*mem allocation*/
#define sq_malloc sqModule::api->malloc
#define sq_realloc sqModule::api->realloc
#define sq_free sqModule::api->free

/*debug*/
#define sq_stackinfos sqModule::api->stackinfos
#define sq_setdebughook sqModule::api->setdebughook
#define sq_setnativedebughook sqModule::api->setnativedebughook

#endif