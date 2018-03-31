local CURRENT_PACKAGE = ...
CURRENT_PACKAGE = string.sub(CURRENT_PACKAGE, 1, -12)
local manager = {}

manager.HeroStaticVo_Data = require(CURRENT_PACKAGE..".HeroStaticVo_Data")
function manager.getHeroStaticVo(id)
    return manager.HeroStaticVo_Data[tostring(id)]
end
manager.EquipStaticVo_Data = require(CURRENT_PACKAGE..".EquipStaticVo_Data")
function manager.getEquipStaticVo(id)
    return manager.EquipStaticVo_Data[tostring(id)]
end


function manager.clear()
_G.package[CURRENT_PACKAGE..".HeroStaticVo_Data"]=nil
_G.package[CURRENT_PACKAGE..".EquipStaticVo_Data"]=nil
end

return manager