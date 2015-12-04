local CURRENT_PACKAGE = ...
CURRENT_PACKAGE = string.sub(CURRENT_PACKAGE, 1, -12)
local manager = {}

manager.UserShopStaticVo_Data = require(CURRENT_PACKAGE..".UserShopStaticVo_Data")
function manager.getUserShopStaticVo(id,frushTime)
    return manager.UserShopStaticVo_Data[tostring(id)..'_'..tostring(frushTime)]
end
manager.ComposeStaticVo_Data = require(CURRENT_PACKAGE..".ComposeStaticVo_Data")
function manager.getComposeStaticVo(id)
    return manager.ComposeStaticVo_Data[tostring(id)]
end
manager.EffectStaticVo_Data = require(CURRENT_PACKAGE..".EffectStaticVo_Data")
function manager.getEffectStaticVo(id)
    return manager.EffectStaticVo_Data[tostring(id)]
end
manager.BuffStaticVo_Data = require(CURRENT_PACKAGE..".BuffStaticVo_Data")
function manager.getBuffStaticVo(id)
    return manager.BuffStaticVo_Data[tostring(id)]
end
manager.RandomNameVo_Data = require(CURRENT_PACKAGE..".RandomNameVo_Data")
function manager.getRandomNameVo(idx)
    return manager.RandomNameVo_Data[idx]
end
manager.EnchantMagicVo_Data = require(CURRENT_PACKAGE..".EnchantMagicVo_Data")
function manager.getEnchantMagicVo(quality)
    return manager.EnchantMagicVo_Data[tostring(quality)]
end
manager.StoryStaticVo_Data = require(CURRENT_PACKAGE..".StoryStaticVo_Data")
function manager.getStoryStaticVo(mapId,timesId)
    return manager.StoryStaticVo_Data[tostring(mapId)..'_'..tostring(timesId)]
end


function manager.clear()
_G.package[CURRENT_PACKAGE..".UserShopStaticVo_Data"]=nil
_G.package[CURRENT_PACKAGE..".ComposeStaticVo_Data"]=nil
_G.package[CURRENT_PACKAGE..".EffectStaticVo_Data"]=nil
_G.package[CURRENT_PACKAGE..".BuffStaticVo_Data"]=nil
_G.package[CURRENT_PACKAGE..".RandomNameVo_Data"]=nil
_G.package[CURRENT_PACKAGE..".EnchantMagicVo_Data"]=nil
_G.package[CURRENT_PACKAGE..".StoryStaticVo_Data"]=nil
end

return manager