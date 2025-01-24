#ifndef _SQFUNCTIONS_
#define _SQFUNCTIONS_

#include <Function.h>
#include <CustomTypes.h>

namespace nonut
{
    class ServerFunctions
    {
    protected:
		ServerFunctions();
		static inline ServerFunctions* instance = nullptr;
	public:
		ServerFunctions(ServerFunctions& other) = delete;
		void operator=(const ServerFunctions&) = delete;
		static ServerFunctions* getInstance();

		Function<String> 											getHostname;
        Function<Int> 												getMaxSlots;
		Function<Int>												getPlayersCount;
		
		Function<Float, Float, Float, Float, Float> 				getDistance2d;
		Function<Float, Float, Float, Float, Float, Float, Float> 	getDistance3d;
		Function<Float, Float, Float, Float, Float> 				getVectorAngle;
		
		Function<void, Int, Int, Int, String> 						sendMessageToAll;
		Function<void, Int, Int, Int, Int, String> 					sendMessageToPlayer;
		Function<void, Int, Int, Int, Int, String> 					sendPlayerMessageToAll;
		Function<void, Int, Int, Int, Int, Int, String> 			sendPlayerMessageToPlayer;
		
		Function<void, Int>											exit;
		Function<Float>												getDayLength;
		Function<String> 											getServerDescription;
		Function<String> 											getServerWorld;
		Function<SqDict> 											getTime;
		Function<void, String> 										serverLog;
		Function<void, Float> 										setDayLength;
		Function<Bool, String> 										setServerDescription;
		Function<void, String> 										setServerWorld;
		Function<void, Int, Int, Int> 								setTime;
		
		Function<void, Int>											clearNpcActions;
		Function<Int, String, String>								createNpc;
		Function<Bool, Int>											destroyNpc;
		Function<SqDict, Int, Int>									getNpcAction;
		//Function<???>												getNpcActionType;
		Function<SqList, Int>										getNpcActions;
		Function<Int, Int> 											getNpcActionsCount;
		Function<Int, Int> 											getNpcHostPlayer;
		Function<Int, Int> 											getNpcLastActionId;
		Function<Bool, Int> 										isNpc;
		Function<Bool, Int, Int> 									isNpcActionFinished;
		Function<void, Int, Int, Int, Int> 							npcAttackMelee;
		Function<void, Int, Int> 									npcAttackRanged;
		Function<void, Int, Int> 									npcSpellCast;
		Function<void, Int, String, Int> 							npcUseClosestMob;
		//Function<???>												pushNpcAction;
		Function<Bool, Int, Int>									setNpcHostPlayer;
		
		Function<Bool, SQObject>									addBan;
		Function<Bool, Int, Int>									applyPlayerOverlay;
		Function<void, Int, Int, String>							ban;
		Function<void, Int, Int>									drawWeapon;
		Function<void, Int, String, Int>							equipItem;
		Function<String, Int>										getPlayerAmulet;
		Function<Float, Int>										getPlayerAngle;
		Function<String, Int>										getPlayerAni;
		Function<String, Int>										getPlayerArmor;
		Function<Position3d, Int>									getPlayerAtVector;
		Function<String, Int>										getPlayerBelt;
		Function<Position3d, Int>									getPlayerCameraPosition;
		Function<Bool, Int>											getPlayerCollision;
		Function<Color, Int>										getPlayerColor;
		Function<Int, Int, Int>										getPlayerContext;
		Function<Int, Int>											getPlayerDexterity;
		Function<SqList, Int>										getPlayerFaceAnis;
		Function<Float, Int>										getPlayerFatness;
		Function<Int, Int>											getPlayerFocus;
		Function<Int, Int>											getPlayerHealth;
		Function<String, Int>										getPlayerHelmet;
		Function<String, Int>										getPlayerIP;
		Function<String, Int>										getPlayerInstance;
		Function<String, Int>										getPlayerMacAddr;
		Function<Int, Int>											getPlayerMana;
		Function<Int, Int>											getPlayerMaxHealth;
		Function<Int, Int>											getPlayerMaxMana;
		Function<String, Int>										getPlayerMeleeWeapon;
		Function<String, Int>										getPlayerName;
		Function<Int, Int>											getPlayerPing;
		Function<Position3d, Int>									getPlayerPosition;
		Function<String, Int>										getPlayerRangedWeapon;
		Function<Int, Int>											getPlayerRespawnTime;
		Function<String, Int, Int>									getPlayerRing;
		Function<SqDict, Int>										getPlayerScale;
		Function<String, Int>										getPlayerSerial;
		Function<String, Int>										getPlayerShield;
		Function<Int, Int, Int>										getPlayerSkillWeapon;
		Function<String, Int, Int>									getPlayerSpell;
		Function<Int, Int>											getPlayerStrength;
		Function<Int, Int, Int>										getPlayerTalent;
		Function<String, Int>										getPlayerUID;
		Function<Int, Int>											getPlayerVirtualWorld;
		Function<SqDict, Int>										getPlayerVisual;
		Function<Int, Int>											getPlayerWeaponMode;
		Function<String, Int>										getPlayerWorld;
		Function<void, Int, String, Int>							giveItem;
		Function<Bool, Int, Int>									hitPlayer;
		Function<Bool, Int>											isPlayerConnected;
		Function<Bool, Int>											isPlayerDead;
		Function<Bool, Int>											isPlayerUnconscious;
		Function<void, Int, String>									kick;
		Function<void, Int, String>									playAni;
		Function<void, Int, String>									playFaceAni;
		Function<void, Int, Int, Int>								readySpell;
		Function<void, Int, String, Int>							removeItem;
		Function<Bool, Int, Int>									removePlayerOverlay;
		Function<void, Int>											removeWeapon;
		Function<void, Int>											respawnPlayer;
		Function<void, Int, Float>									setPlayerAngle;
		Function<void, Int, Bool>									setPlayerCollision;
		Function<void, Int, Int, Int, Int>							setPlayerColor;
		Function<void, Int, Int, Int>								setPlayerContext;
		Function<void, Int, Int>									setPlayerDexterity;
		Function<void, Int, Float>									setPlayerFatness;
		Function<void, Int, Int>									setPlayerHealth;
		Function<void, Int, String>									setPlayerInstance;
		Function<void, Int, Bool>									setPlayerInvisible;
		Function<void, Int, Int>									setPlayerMana;
		Function<void, Int, Int>									setPlayerMaxHealth;
		Function<void, Int, Int>									setPlayerMaxMana;
		Function<void, Int, String>									setPlayerName;
		Function<void, Int, Float, Float, Float>					setPlayerPosition;
		Function<void, Int, Int>									setPlayerRespawnTime;
		Function<void, Int, Float, Float, Float>					setPlayerScale;
		Function<void, Int, Int, Int>								setPlayerSkillWeapon;
		Function<void, Int, Int>									setPlayerStrength;
		Function<void, Int, Int, Int>								setPlayerTalent;
		Function<void, Int, Int>									setPlayerVirtualWorld;
		Function<void, Int, String, Int, String, Int>				setPlayerVisual;
		Function<void, Int, Int>									setPlayerWeaponMode;
		Function<void, Int, String, String>							setPlayerWorld;
		Function<void, Int>											spawnPlayer;
		Function<void, Int, String>									stopAni;
		Function<void, Int, String>									stopFaceAni;
		Function<void, Int, String>									unequipItem;
		Function<void, Int>											unreadySpell;
		Function<void, Int>											unspawnPlayer;
		Function<void, Int, String>									useItem;
		Function<void, Int, String, Int>							useItemToState;
		
		Function<SqList, SQObject, Int, String, Int>				findNearbyPlayers;
		Function<SqList, Int>										getSpawnedPlayersForPlayer;
		Function<SqList, Int>										getStreamedPlayersByPlayer;
		
		Function<SqDict, String, Int, Int, Int>						getNearestWaypoint;
		Function<SqDict, String, String>							getWaypoint;
    };
}

#endif