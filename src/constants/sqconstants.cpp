#include <sqapi.h>
#include <pybind11/embed.h>
#include "events/sqevents.h"
#include <iostream>
#include "sqconstants.h"

namespace py = pybind11;
extern py::module_ g2o;

#define GET_CONST(constName, constType) Sqrat::ConstTable().GetSlot(constName).Cast<constType>()

// Sadly, I have to split definition and declaration of constants, because pybind doesn't allow embeding modules inside functions
// And in the global scope, Squirrel VM and const table is not yet exist

PYBIND11_EMBEDDED_MODULE(sqg2oconst, m) {
    m.attr("DAMAGE_CTX")				        = 0;
    m.attr("EQUIPMENT_CTX")				        = 0;
    
    m.attr("DAMAGE_UNKNOW")				        = 0;
    m.attr("DAMAGE_BARRIER")				    = 0;
    m.attr("DAMAGE_BLUNT")				        = 0;
    m.attr("DAMAGE_EDGE")				        = 0;
    m.attr("DAMAGE_FIRE")				        = 0;
    m.attr("DAMAGE_FLY")				        = 0;
    m.attr("DAMAGE_MAGIC")				        = 0;
    m.attr("DAMAGE_POINT")				        = 0;
    m.attr("DAMAGE_FALL")				        = 0;
    
    m.attr("DEBUG_MODE")				        = false;
    m.attr("SERVER_SIDE")				        = false;
    m.attr("CLIENT_SIDE")				        = false;
    
    m.attr("HAND_LEFT")				            = 0;
    m.attr("HAND_RIGHT")				        = 0;
    
    m.attr("ITEM_CAT_NONE")				        = 0;
    m.attr("ITEM_CAT_NF")				        = 0;
    m.attr("ITEM_CAT_FF")				        = 0;
    m.attr("ITEM_CAT_MUN")				        = 0;
    m.attr("ITEM_CAT_ARMOR")				    = 0;
    m.attr("ITEM_CAT_FOOD")				        = 0;
    m.attr("ITEM_CAT_DOCS")				        = 0;
    m.attr("ITEM_CAT_POTION")				    = 0;
    m.attr("ITEM_CAT_LIGHT")				    = 0;
    m.attr("ITEM_CAT_RUNE")				        = 0;
    m.attr("ITEM_CAT_MAGIC")				    = 0;
    
    m.attr("ITEM_FLAG_DAG")				        = 0;
    m.attr("ITEM_FLAG_SWD")				        = 0;
    m.attr("ITEM_FLAG_AXE")				        = 0;
    m.attr("ITEM_FLAG_2HD_SWD")				    = 0;
    m.attr("ITEM_FLAG_2HD_AXE")				    = 0;
    m.attr("ITEM_FLAG_SHIELD")				    = 0;
    m.attr("ITEM_FLAG_BOW")				        = 0;
    m.attr("ITEM_FLAG_CROSSBOW")				= 0;
    m.attr("ITEM_FLAG_RING")				    = 0;
    m.attr("ITEM_FLAG_AMULET")				    = 0;
    m.attr("ITEM_FLAG_BELT")				    = 0;
    m.attr("ITEM_FLAG_DROPPED")				    = 0;
    m.attr("ITEM_FLAG_MI")				        = 0;
    m.attr("ITEM_FLAG_MULTI")				    = 0;
    m.attr("ITEM_FLAG_NFOCUS")				    = 0;
    m.attr("ITEM_FLAG_CREATEAMMO")				= 0;
    m.attr("ITEM_FLAG_NSPLIT")				    = 0;
    m.attr("ITEM_FLAG_DRINK")				    = 0;
    m.attr("ITEM_FLAG_TORCH")				    = 0;
    m.attr("ITEM_FLAG_THROW")				    = 0;
    m.attr("ITEM_FLAG_ACTIVE")				    = 0;
    
    m.attr("ITEM_WEAR_NO")				        = 0;
    m.attr("ITEM_WEAR_TORSO")				    = 0;
    m.attr("ITEM_WEAR_HEAD")				    = 0;
    m.attr("ITEM_WEAR_LIGHT")				    = 0;
    
    m.attr("ATTACK_RUN")				        = 0;
    m.attr("ATTACK_FORWARD")				    = 0;
    m.attr("ATTACK_LEFT")				        = 0;
    m.attr("ATTACK_RIGHT")				        = 0;
    m.attr("ACTION_CLEAR_QUEUE")				= 0;
    m.attr("ACTION_APPLY_OVERLAY")				= 0;
    m.attr("ACTION_REMOVE_OVERLAY")				= 0;
    m.attr("ACTION_PLAY_ANI")				    = 0;
    m.attr("ACTION_STOP_ANI")				    = 0;
    m.attr("ACTION_EQUIP_ITEM")				    = 0;
    m.attr("ACTION_UNEQUIP_ITEM")				= 0;
    m.attr("ACTION_WEAPON_MODE")				= 0;
    m.attr("ACTION_DRAW_WEAPON")				= 0;
    m.attr("ACTION_REMOVE_WEAPON")				= 0;
    m.attr("ACTION_USE_ITEM")				    = 0;
    m.attr("ACTION_USE_ITEM_TO_STATE")			= 0;
    m.attr("ACTION_READY_SPELL")				= 0;
    m.attr("ACTION_UNREADY_SPELL")				= 0;
    m.attr("ACTION_ATTACK_MELEE_WEAPON")		= 0;
    m.attr("ACTION_ATTACK_RANGED_WEAPON")		= 0;
    m.attr("ACTION_SPELL_CAST")				    = 0;
    m.attr("ACTION_USE_MOB_SCHEME")				= 0;
    m.attr("ACTION_SHOOT_AT")				    = 0;
    m.attr("ACTION_START_AIM_AT")				= 0;
    m.attr("ACTION_STOP_AIM_AT")				= 0;
    m.attr("ACTION_SCRIPT")				        = 0;
    
    m.attr("UNRELIABLE")				        = 0;
    m.attr("UNRELIABLE_SEQUENCED")				= 0;
    m.attr("RELIABLE")				            = 0;
    m.attr("RELIABLE_ORDERED")				    = 0;
    m.attr("RELIABLE_SEQUENCED")				= 0;
    
    m.attr("WEAPON_1H")				            = 0;
    m.attr("WEAPON_2H")				            = 0;
    m.attr("WEAPON_BOW")				        = 0;
    m.attr("WEAPON_CBOW")				        = 0;
    
    m.attr("TALENT_1H")				            = 0;
    m.attr("TALENT_2H")				            = 0;
    m.attr("TALENT_BOW")				        = 0;
    m.attr("TALENT_CROSSBOW")				    = 0;
    m.attr("TALENT_PICK_LOCKS")				    = 0;
    m.attr("TALENT_PICKPOCKET")				    = 0;
    m.attr("TALENT_MAGE")				        = 0;
    m.attr("TALENT_SNEAK")				        = 0;
    m.attr("TALENT_REGENERATE")				    = 0;
    m.attr("TALENT_FIREMASTER")				    = 0;
    m.attr("TALENT_ACROBATIC")				    = 0;
    m.attr("TALENT_PICKPOCKET_UNUSED")			= 0;
    m.attr("TALENT_SMITH")				        = 0;
    m.attr("TALENT_RUNES")				        = 0;
    m.attr("TALENT_ALCHEMY")				    = 0;
    m.attr("TALENT_THROPHY")				    = 0;
    m.attr("TALENT_A")				            = 0;
    m.attr("TALENT_B")				            = 0;
    m.attr("TALENT_C")				            = 0;
    m.attr("TALENT_D")				            = 0;
    m.attr("TALENT_E")				            = 0;
    m.attr("TALENT_MAX")				        = 0;
    
    m.attr("WEAPONMODE_NONE")				    = 0;
    m.attr("WEAPONMODE_FIST")				    = 0;
    m.attr("WEAPONMODE_DAG")				    = 0;
    m.attr("WEAPONMODE_1HS")				    = 0;
    m.attr("WEAPONMODE_2HS")				    = 0;
    m.attr("WEAPONMODE_BOW")				    = 0;
    m.attr("WEAPONMODE_CBOW")				    = 0;
    m.attr("WEAPONMODE_MAG")				    = 0;
    m.attr("WEAPONMODE_MAX")				    = 0;
    
    m.attr("WEATHER_SNOW")				        = 0;
    m.attr("WEATHER_RAIN")				        = 0;
    
    m.attr("AC_SPEED_HACK")				        = 0;
    
    m.attr("DISCONNECTED")				        = 0;
    m.attr("LOST_CONNECTION")				    = 0;
    m.attr("HAS_CRASHED")				        = 0;
}

void registerSquirrelConstants()
{
    py::module_ cts = py::module_::import("sqg2oconst");
    
    cts.attr("DAMAGE_CTX")                      = GET_CONST("DAMAGE_CTX", int);
    cts.attr("EQUIPMENT_CTX")                   = GET_CONST("EQUIPMENT_CTX", int);
    
    cts.attr("DAMAGE_UNKNOW")                   = GET_CONST("DAMAGE_UNKNOW", int);
    cts.attr("DAMAGE_BARRIER")                  = GET_CONST("DAMAGE_BARRIER", int);
    cts.attr("DAMAGE_BLUNT")                    = GET_CONST("DAMAGE_BLUNT", int);
    cts.attr("DAMAGE_EDGE")                     = GET_CONST("DAMAGE_EDGE", int);
    cts.attr("DAMAGE_FIRE")                     = GET_CONST("DAMAGE_FIRE", int);
    cts.attr("DAMAGE_FLY")                      = GET_CONST("DAMAGE_FLY", int);
    cts.attr("DAMAGE_MAGIC")                    = GET_CONST("DAMAGE_MAGIC", int);
    cts.attr("DAMAGE_POINT")                    = GET_CONST("DAMAGE_POINT", int);
    cts.attr("DAMAGE_FALL")                     = GET_CONST("DAMAGE_FALL", int);
    
    cts.attr("DEBUG_MODE")                      = GET_CONST("DEBUG_MODE", bool);
    cts.attr("SERVER_SIDE")                     = GET_CONST("SERVER_SIDE", bool);
    cts.attr("CLIENT_SIDE")                     = GET_CONST("CLIENT_SIDE", bool);
    
    cts.attr("HAND_LEFT")                       = GET_CONST("HAND_LEFT", int);
    cts.attr("HAND_RIGHT")                      = GET_CONST("HAND_RIGHT", int);
    
    cts.attr("ITEM_CAT_NONE")		            = GET_CONST("ITEM_CAT_NONE", int);
    cts.attr("ITEM_CAT_NF")		                = GET_CONST("ITEM_CAT_NF", int);
    cts.attr("ITEM_CAT_FF")		                = GET_CONST("ITEM_CAT_FF", int);
    cts.attr("ITEM_CAT_MUN")		            = GET_CONST("ITEM_CAT_MUN", int);
    cts.attr("ITEM_CAT_ARMOR")		            = GET_CONST("ITEM_CAT_ARMOR", int);
    cts.attr("ITEM_CAT_FOOD")		            = GET_CONST("ITEM_CAT_FOOD", int);
    cts.attr("ITEM_CAT_DOCS")		            = GET_CONST("ITEM_CAT_DOCS", int);
    cts.attr("ITEM_CAT_POTION")		            = GET_CONST("ITEM_CAT_POTION", int);
    cts.attr("ITEM_CAT_LIGHT")		            = GET_CONST("ITEM_CAT_LIGHT", int);
    cts.attr("ITEM_CAT_RUNE")		            = GET_CONST("ITEM_CAT_RUNE", int);
    cts.attr("ITEM_CAT_MAGIC")		            = GET_CONST("ITEM_CAT_MAGIC", int);
    
    cts.attr("ITEM_FLAG_DAG")		            = GET_CONST("ITEM_FLAG_DAG", int);
    cts.attr("ITEM_FLAG_SWD")		            = GET_CONST("ITEM_FLAG_SWD", int);
    cts.attr("ITEM_FLAG_AXE")		            = GET_CONST("ITEM_FLAG_AXE", int);
    cts.attr("ITEM_FLAG_2HD_SWD")		        = GET_CONST("ITEM_FLAG_2HD_SWD", int);
    cts.attr("ITEM_FLAG_2HD_AXE")		        = GET_CONST("ITEM_FLAG_2HD_AXE", int);
    cts.attr("ITEM_FLAG_SHIELD")		        = GET_CONST("ITEM_FLAG_SHIELD", int);
    cts.attr("ITEM_FLAG_BOW")		            = GET_CONST("ITEM_FLAG_BOW", int);
    cts.attr("ITEM_FLAG_CROSSBOW")		        = GET_CONST("ITEM_FLAG_CROSSBOW", int);
    cts.attr("ITEM_FLAG_RING")		            = GET_CONST("ITEM_FLAG_RING", int);
    cts.attr("ITEM_FLAG_AMULET")		        = GET_CONST("ITEM_FLAG_AMULET", int);
    cts.attr("ITEM_FLAG_BELT")		            = GET_CONST("ITEM_FLAG_BELT", int);
    cts.attr("ITEM_FLAG_DROPPED")		        = GET_CONST("ITEM_FLAG_DROPPED", int);
    cts.attr("ITEM_FLAG_MI")		            = GET_CONST("ITEM_FLAG_MI", int);
    cts.attr("ITEM_FLAG_MULTI")		            = GET_CONST("ITEM_FLAG_MULTI", int);
    cts.attr("ITEM_FLAG_NFOCUS")		        = GET_CONST("ITEM_FLAG_NFOCUS", int);
    cts.attr("ITEM_FLAG_CREATEAMMO")            = GET_CONST("ITEM_FLAG_CREATEAMMO", int);
    cts.attr("ITEM_FLAG_NSPLIT")		        = GET_CONST("ITEM_FLAG_NSPLIT", int);
    cts.attr("ITEM_FLAG_DRINK")		            = GET_CONST("ITEM_FLAG_DRINK", int);
    cts.attr("ITEM_FLAG_TORCH")		            = GET_CONST("ITEM_FLAG_TORCH", int);
    cts.attr("ITEM_FLAG_THROW")		            = GET_CONST("ITEM_FLAG_THROW", int);
    cts.attr("ITEM_FLAG_ACTIVE")		        = GET_CONST("ITEM_FLAG_ACTIVE", int);
    
    cts.attr("ITEM_WEAR_NO")		            = GET_CONST("ITEM_WEAR_NO", int);
    cts.attr("ITEM_WEAR_TORSO")		            = GET_CONST("ITEM_WEAR_TORSO", int);
    cts.attr("ITEM_WEAR_HEAD")		            = GET_CONST("ITEM_WEAR_HEAD", int);
    cts.attr("ITEM_WEAR_LIGHT")		            = GET_CONST("ITEM_WEAR_LIGHT", int);
    
    cts.attr("ATTACK_RUN")		                = GET_CONST("ATTACK_RUN", int);
    cts.attr("ATTACK_FORWARD")		            = GET_CONST("ATTACK_FORWARD", int);
    cts.attr("ATTACK_LEFT")		                = GET_CONST("ATTACK_LEFT", int);
    cts.attr("ATTACK_RIGHT")		            = GET_CONST("ATTACK_RIGHT", int);
    cts.attr("ACTION_CLEAR_QUEUE")		        = GET_CONST("ACTION_CLEAR_QUEUE", int);
    cts.attr("ACTION_APPLY_OVERLAY")		    = GET_CONST("ACTION_APPLY_OVERLAY", int);
    cts.attr("ACTION_REMOVE_OVERLAY")		    = GET_CONST("ACTION_REMOVE_OVERLAY", int);
    cts.attr("ACTION_PLAY_ANI")		            = GET_CONST("ACTION_PLAY_ANI", int);
    cts.attr("ACTION_STOP_ANI")		            = GET_CONST("ACTION_STOP_ANI", int);
    cts.attr("ACTION_EQUIP_ITEM")		        = GET_CONST("ACTION_EQUIP_ITEM", int);
    cts.attr("ACTION_UNEQUIP_ITEM")		        = GET_CONST("ACTION_UNEQUIP_ITEM", int);
    cts.attr("ACTION_WEAPON_MODE")		        = GET_CONST("ACTION_WEAPON_MODE", int);
    cts.attr("ACTION_DRAW_WEAPON")		        = GET_CONST("ACTION_DRAW_WEAPON", int);
    cts.attr("ACTION_REMOVE_WEAPON")		    = GET_CONST("ACTION_REMOVE_WEAPON", int);
    cts.attr("ACTION_USE_ITEM")		            = GET_CONST("ACTION_USE_ITEM", int);
    cts.attr("ACTION_USE_ITEM_TO_STATE")		= GET_CONST("ACTION_USE_ITEM_TO_STATE", int);
    cts.attr("ACTION_READY_SPELL")		        = GET_CONST("ACTION_READY_SPELL", int);
    cts.attr("ACTION_UNREADY_SPELL")		    = GET_CONST("ACTION_UNREADY_SPELL", int);
    cts.attr("ACTION_ATTACK_MELEE_WEAPON")		= GET_CONST("ACTION_ATTACK_MELEE_WEAPON", int);
    cts.attr("ACTION_ATTACK_RANGED_WEAPON")     = GET_CONST("ACTION_ATTACK_RANGED_WEAPON", int);
    cts.attr("ACTION_SPELL_CAST")		        = GET_CONST("ACTION_SPELL_CAST", int);
    cts.attr("ACTION_USE_MOB_SCHEME")		    = GET_CONST("ACTION_USE_MOB_SCHEME", int);
    cts.attr("ACTION_SHOOT_AT")		            = GET_CONST("ACTION_SHOOT_AT", int);
    cts.attr("ACTION_START_AIM_AT")		        = GET_CONST("ACTION_START_AIM_AT", int);
    cts.attr("ACTION_STOP_AIM_AT")		        = GET_CONST("ACTION_STOP_AIM_AT", int);
    cts.attr("ACTION_SCRIPT")		            = GET_CONST("ACTION_SCRIPT", int);
    
    cts.attr("UNRELIABLE")		                = GET_CONST("UNRELIABLE", int);
    cts.attr("UNRELIABLE_SEQUENCED")		    = GET_CONST("UNRELIABLE_SEQUENCED", int);
    cts.attr("RELIABLE")		                = GET_CONST("RELIABLE", int);
    cts.attr("RELIABLE_ORDERED")		        = GET_CONST("RELIABLE_ORDERED", int);
    cts.attr("RELIABLE_SEQUENCED")		        = GET_CONST("RELIABLE_SEQUENCED", int);
    
    cts.attr("WEAPON_1H")		                = GET_CONST("WEAPON_1H", int);
    cts.attr("WEAPON_2H")		                = GET_CONST("WEAPON_2H", int);
    cts.attr("WEAPON_BOW")		                = GET_CONST("WEAPON_BOW", int);
    cts.attr("WEAPON_CBOW")		                = GET_CONST("WEAPON_CBOW", int);
    
    cts.attr("TALENT_1H")		                = GET_CONST("TALENT_1H", int);
    cts.attr("TALENT_2H")		                = GET_CONST("TALENT_2H", int);
    cts.attr("TALENT_BOW")		                = GET_CONST("TALENT_BOW", int);
    cts.attr("TALENT_CROSSBOW")		            = GET_CONST("TALENT_CROSSBOW", int);
    cts.attr("TALENT_PICK_LOCKS")		        = GET_CONST("TALENT_PICK_LOCKS", int);
    cts.attr("TALENT_PICKPOCKET")		        = GET_CONST("TALENT_PICKPOCKET", int);
    cts.attr("TALENT_MAGE")		                = GET_CONST("TALENT_MAGE", int);
    cts.attr("TALENT_SNEAK")		            = GET_CONST("TALENT_SNEAK", int);
    cts.attr("TALENT_REGENERATE")		        = GET_CONST("TALENT_REGENERATE", int);
    cts.attr("TALENT_FIREMASTER")		        = GET_CONST("TALENT_FIREMASTER", int);
    cts.attr("TALENT_ACROBATIC")		        = GET_CONST("TALENT_ACROBATIC", int);
    cts.attr("TALENT_PICKPOCKET_UNUSED")  		= GET_CONST("TALENT_PICKPOCKET_UNUSED", int);
    cts.attr("TALENT_SMITH")		            = GET_CONST("TALENT_SMITH", int);
    cts.attr("TALENT_RUNES")		            = GET_CONST("TALENT_RUNES", int);
    cts.attr("TALENT_ALCHEMY")		            = GET_CONST("TALENT_ALCHEMY", int);
    cts.attr("TALENT_THROPHY")		            = GET_CONST("TALENT_THROPHY", int);
    cts.attr("TALENT_A")		                = GET_CONST("TALENT_A", int);
    cts.attr("TALENT_B")		                = GET_CONST("TALENT_B", int);
    cts.attr("TALENT_C")		                = GET_CONST("TALENT_C", int);
    cts.attr("TALENT_D")		                = GET_CONST("TALENT_D", int);
    cts.attr("TALENT_E")		                = GET_CONST("TALENT_E", int);
    cts.attr("TALENT_MAX")		                = GET_CONST("TALENT_MAX", int);
    
    cts.attr("WEAPONMODE_NONE")		            = GET_CONST("WEAPONMODE_NONE", int);
    cts.attr("WEAPONMODE_FIST")		            = GET_CONST("WEAPONMODE_FIST", int);
    cts.attr("WEAPONMODE_DAG")		            = GET_CONST("WEAPONMODE_DAG", int);
    cts.attr("WEAPONMODE_1HS")		            = GET_CONST("WEAPONMODE_1HS", int);
    cts.attr("WEAPONMODE_2HS")		            = GET_CONST("WEAPONMODE_2HS", int);
    cts.attr("WEAPONMODE_BOW")		            = GET_CONST("WEAPONMODE_BOW", int);
    cts.attr("WEAPONMODE_CBOW")		            = GET_CONST("WEAPONMODE_CBOW", int);
    cts.attr("WEAPONMODE_MAG")		            = GET_CONST("WEAPONMODE_MAG", int);
    cts.attr("WEAPONMODE_MAX")		            = GET_CONST("WEAPONMODE_MAX", int);
    
    cts.attr("WEATHER_SNOW")		            = GET_CONST("WEATHER_SNOW", int);
    cts.attr("WEATHER_RAIN")		            = GET_CONST("WEATHER_RAIN", int);
    
    cts.attr("AC_SPEED_HACK")		            = GET_CONST("AC_SPEED_HACK", int);
    
    cts.attr("DISCONNECTED")		            = GET_CONST("DISCONNECTED", int);
    cts.attr("LOST_CONNECTION")		            = GET_CONST("LOST_CONNECTION", int);
    cts.attr("HAS_CRASHED")		                = GET_CONST("HAS_CRASHED", int);
}