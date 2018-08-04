local CURRENT_PACKAGE = ...
CURRENT_PACKAGE = string.sub(CURRENT_PACKAGE, 1, -12)
local manager = {}

function manager.getDungeon(id)
    if not manager.Dungeon_Data then
        manager.Dungeon_Data = require(CURRENT_PACKAGE..".Dungeon_Data")
    end
    return manager.Dungeon_Data[id]
end
function manager.getItem(id)
    if not manager.Item_Data then
        manager.Item_Data = require(CURRENT_PACKAGE..".Item_Data")
    end
    return manager.Item_Data[id]
end


function manager.clear()
_G.package[CURRENT_PACKAGE..".Dungeon_Data"]=nil
_G.package[CURRENT_PACKAGE..".Item_Data"]=nil
end

return manager