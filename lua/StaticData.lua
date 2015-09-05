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
manager.HeroStarStaticVo_Data = require(CURRENT_PACKAGE..".HeroStarStaticVo_Data")
function manager.getHeroStarStaticVo(id,star)
    return manager.HeroStarStaticVo_Data[tostring(id..'_'..star)]
end
manager.HeroQualityStaticVo_Data = require(CURRENT_PACKAGE..".HeroQualityStaticVo_Data")
function manager.getHeroQualityStaticVo(id)
    return manager.HeroQualityStaticVo_Data[tostring(id)]
end
manager.HeroUpgradeQualityStaticVo_Data = require(CURRENT_PACKAGE..".HeroUpgradeQualityStaticVo_Data")
function manager.getHeroUpgradeQualityStaticVo(id,quality)
    return manager.HeroUpgradeQualityStaticVo_Data[tostring(id..'_'..quality)]
end
manager.AtkCircleStaticVo_Data = require(CURRENT_PACKAGE..".AtkCircleStaticVo_Data")
function manager.getAtkCircleStaticVo(id)
    return manager.AtkCircleStaticVo_Data[tostring(id)]
end
manager.MapStaticVo_Data = require(CURRENT_PACKAGE..".MapStaticVo_Data")
function manager.getMapStaticVo(id)
    return manager.MapStaticVo_Data[tostring(id)]
end
manager.SkillStaticVo_Data = require(CURRENT_PACKAGE..".SkillStaticVo_Data")
function manager.getSkillStaticVo(id)
    return manager.SkillStaticVo_Data[tostring(id)]
end
manager.HeroSkillStaticVo_Data = require(CURRENT_PACKAGE..".HeroSkillStaticVo_Data")
function manager.getHeroSkillStaticVo(id)
    return manager.HeroSkillStaticVo_Data[tostring(id)]
end
manager.HeroExpStaticVo_Data = require(CURRENT_PACKAGE..".HeroExpStaticVo_Data")
function manager.getHeroExpStaticVo(level)
    return manager.HeroExpStaticVo_Data[tostring(level)]
end
manager.SkillUpStaticVo_Data = require(CURRENT_PACKAGE..".SkillUpStaticVo_Data")
function manager.getSkillUpStaticVo(level)
    return manager.SkillUpStaticVo_Data[tostring(level)]
end
manager.SectionStaticVo_Data = require(CURRENT_PACKAGE..".SectionStaticVo_Data")
function manager.getSectionStaticVo(id)
    return manager.SectionStaticVo_Data[tostring(id)]
end
manager.ItemConsumablesStaticVo_Data = require(CURRENT_PACKAGE..".ItemConsumablesStaticVo_Data")
function manager.getItemConsumablesStaticVo(id)
    return manager.ItemConsumablesStaticVo_Data[tostring(id)]
end
manager.ItemReelStaticVo_Data = require(CURRENT_PACKAGE..".ItemReelStaticVo_Data")
function manager.getItemReelStaticVo(id)
    return manager.ItemReelStaticVo_Data[tostring(id)]
end
manager.ItemFragStaticVo_Data = require(CURRENT_PACKAGE..".ItemFragStaticVo_Data")
function manager.getItemFragStaticVo(id)
    return manager.ItemFragStaticVo_Data[tostring(id)]
end
manager.VipVo_Data = require(CURRENT_PACKAGE..".VipVo_Data")
function manager.getVipVo(viplevel)
    return manager.VipVo_Data[tostring(viplevel)]
end
manager.BuyPPVo_Data = require(CURRENT_PACKAGE..".BuyPPVo_Data")
function manager.getBuyPPVo(num)
    return manager.BuyPPVo_Data[tostring(num)]
end
manager.ErrStaticVo_Data = require(CURRENT_PACKAGE..".ErrStaticVo_Data")
function manager.getErrStaticVo(id)
    return manager.ErrStaticVo_Data[tostring(id)]
end
manager.EnchantingVo_Data = require(CURRENT_PACKAGE..".EnchantingVo_Data")
function manager.getEnchantingVo(EquipQuality)
    return manager.EnchantingVo_Data[tostring(EquipQuality)]
end
manager.UserShopStaticVo_Data = require(CURRENT_PACKAGE..".UserShopStaticVo_Data")
function manager.getUserShopStaticVo(id)
    return manager.UserShopStaticVo_Data[tostring(id)]
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
manager.NpcTroopStaticVo_Data = require(CURRENT_PACKAGE..".NpcTroopStaticVo_Data")
function manager.getNpcTroopStaticVo(id)
    return manager.NpcTroopStaticVo_Data[tostring(id)]
end
manager.heroMagicStaticVo_Data = require(CURRENT_PACKAGE..".heroMagicStaticVo_Data")
function manager.getheroMagicStaticVo(id)
    return manager.heroMagicStaticVo_Data[tostring(id)]
end
manager.EnchantMagicVo_Data = require(CURRENT_PACKAGE..".EnchantMagicVo_Data")
function manager.getEnchantMagicVo(quality)
    return manager.EnchantMagicVo_Data[tostring(quality)]
end
manager.HeroSoundStaticVo_Data = require(CURRENT_PACKAGE..".HeroSoundStaticVo_Data")
function manager.getHeroSoundStaticVo(id)
    return manager.HeroSoundStaticVo_Data[tostring(id)]
end
manager.BattleSoundPairStaticVo_Data = require(CURRENT_PACKAGE..".BattleSoundPairStaticVo_Data")
function manager.getBattleSoundPairStaticVo(atkType,beAtkType)
    return manager.BattleSoundPairStaticVo_Data[tostring(atkType..'_'..beAtkType)]
end
manager.TaskDayStaticVo_Data = require(CURRENT_PACKAGE..".TaskDayStaticVo_Data")
function manager.getTaskDayStaticVo(id)
    return manager.TaskDayStaticVo_Data[tostring(id)]
end
manager.TaskStaticVo_Data = require(CURRENT_PACKAGE..".TaskStaticVo_Data")
function manager.getTaskStaticVo(id)
    return manager.TaskStaticVo_Data[tostring(id)]
end
manager.UserSkillStaticVo_Data = require(CURRENT_PACKAGE..".UserSkillStaticVo_Data")
function manager.getUserSkillStaticVo(id)
    return manager.UserSkillStaticVo_Data[tostring(id)]
end
manager.UserLevelStaticVo_Data = require(CURRENT_PACKAGE..".UserLevelStaticVo_Data")
function manager.getUserLevelStaticVo(level)
    return manager.UserLevelStaticVo_Data[tostring(level)]
end
manager.BigBossStaticVo_Data = require(CURRENT_PACKAGE..".BigBossStaticVo_Data")
function manager.getBigBossStaticVo(id,level)
    return manager.BigBossStaticVo_Data[tostring(id..'_'..level)]
end
manager.SiegeStaticVo_Data = require(CURRENT_PACKAGE..".SiegeStaticVo_Data")
function manager.getSiegeStaticVo(id,stage)
    return manager.SiegeStaticVo_Data[tostring(id..'_'..stage)]
end
manager.StoryStaticVo_Data = require(CURRENT_PACKAGE..".StoryStaticVo_Data")
function manager.getStoryStaticVo(mapId,timesId)
    return manager.StoryStaticVo_Data[tostring(mapId..'_'..timesId)]
end
manager.ArenaTopRankAwardVo_Data = require(CURRENT_PACKAGE..".ArenaTopRankAwardVo_Data")
function manager.getArenaTopRankAwardVo(topRank)
    return manager.ArenaTopRankAwardVo_Data[tostring(topRank)]
end
manager.ArenaRankAwardVo_Data = require(CURRENT_PACKAGE..".ArenaRankAwardVo_Data")
function manager.getArenaRankAwardVo(Rank)
    return manager.ArenaRankAwardVo_Data[tostring(Rank)]
end
manager.ArenaBuyAttackNumVo_Data = require(CURRENT_PACKAGE..".ArenaBuyAttackNumVo_Data")
function manager.getArenaBuyAttackNumVo(num)
    return manager.ArenaBuyAttackNumVo_Data[tostring(num)]
end
manager.LegionBasicVo_Data = require(CURRENT_PACKAGE..".LegionBasicVo_Data")
function manager.getLegionBasicVo(level)
    return manager.LegionBasicVo_Data[tostring(level)]
end
manager.LegionEmployVo_Data = require(CURRENT_PACKAGE..".LegionEmployVo_Data")
function manager.getLegionEmployVo(force)
    return manager.LegionEmployVo_Data[tostring(force)]
end
manager.LegionSalaryVo_Data = require(CURRENT_PACKAGE..".LegionSalaryVo_Data")
function manager.getLegionSalaryVo(denote)
    return manager.LegionSalaryVo_Data[tostring(denote)]
end
manager.LegionEventVo_Data = require(CURRENT_PACKAGE..".LegionEventVo_Data")
function manager.getLegionEventVo(id)
    return manager.LegionEventVo_Data[tostring(id)]
end
manager.RandomNameVo_Data = require(CURRENT_PACKAGE..".RandomNameVo_Data")
function manager.getRandomNameVo(idx)
    return manager.RandomNameVo_Data[idx]
end
manager.RegistryVo_Data = require(CURRENT_PACKAGE..".RegistryVo_Data")
function manager.getRegistryVo(month,num)
    return manager.RegistryVo_Data[tostring(month..'_'..num)]
end
manager.BuyGoldVo_Data = require(CURRENT_PACKAGE..".BuyGoldVo_Data")
function manager.getBuyGoldVo(times)
    return manager.BuyGoldVo_Data[tostring(times)]
end
manager.BuyEliteVo_Data = require(CURRENT_PACKAGE..".BuyEliteVo_Data")
function manager.getBuyEliteVo(times)
    return manager.BuyEliteVo_Data[tostring(times)]
end
manager.GuideVo_Data = require(CURRENT_PACKAGE..".GuideVo_Data")
function manager.getGuideVo(id)
    return manager.GuideVo_Data[tostring(id)]
end
manager.GuideDialogueVo_Data = require(CURRENT_PACKAGE..".GuideDialogueVo_Data")
function manager.getGuideDialogueVo(id)
    return manager.GuideDialogueVo_Data[tostring(id)]
end
manager.Recharge_Data = require(CURRENT_PACKAGE..".Recharge_Data")
function manager.getRecharge(id)
    return manager.Recharge_Data[tostring(id)]
end
manager.DirtyWord_Data = require(CURRENT_PACKAGE..".DirtyWord_Data")
function manager.getDirtyWord(id)
    return manager.DirtyWord_Data[tostring(id)]
end
manager.Tower_Data = require(CURRENT_PACKAGE..".Tower_Data")
function manager.getTower(id)
    return manager.Tower_Data[tostring(id)]
end
manager.Fund_Data = require(CURRENT_PACKAGE..".Fund_Data")
function manager.getFund(levelLimit)
    return manager.Fund_Data[tostring(levelLimit)]
end
manager.Benefit_Data = require(CURRENT_PACKAGE..".Benefit_Data")
function manager.getBenefit(count)
    return manager.Benefit_Data[tostring(count)]
end
manager.MammonVo_Data = require(CURRENT_PACKAGE..".MammonVo_Data")
function manager.getMammonVo(times)
    return manager.MammonVo_Data[tostring(times)]
end
manager.Activity_Data = require(CURRENT_PACKAGE..".Activity_Data")
function manager.getActivity(id)
    return manager.Activity_Data[tostring(id)]
end
function manager.clear()
_G.package[CURRENT_PACKAGE..".HeroStaticVo_Data"]=nil
_G.package[CURRENT_PACKAGE..".EquipStaticVo_Data"]=nil
_G.package[CURRENT_PACKAGE..".HeroStarStaticVo_Data"]=nil
_G.package[CURRENT_PACKAGE..".HeroQualityStaticVo_Data"]=nil
_G.package[CURRENT_PACKAGE..".HeroUpgradeQualityStaticVo_Data"]=nil
_G.package[CURRENT_PACKAGE..".AtkCircleStaticVo_Data"]=nil
_G.package[CURRENT_PACKAGE..".MapStaticVo_Data"]=nil
_G.package[CURRENT_PACKAGE..".SkillStaticVo_Data"]=nil
_G.package[CURRENT_PACKAGE..".HeroSkillStaticVo_Data"]=nil
_G.package[CURRENT_PACKAGE..".HeroExpStaticVo_Data"]=nil
_G.package[CURRENT_PACKAGE..".SkillUpStaticVo_Data"]=nil
_G.package[CURRENT_PACKAGE..".SectionStaticVo_Data"]=nil
_G.package[CURRENT_PACKAGE..".ItemConsumablesStaticVo_Data"]=nil
_G.package[CURRENT_PACKAGE..".ItemReelStaticVo_Data"]=nil
_G.package[CURRENT_PACKAGE..".ItemFragStaticVo_Data"]=nil
_G.package[CURRENT_PACKAGE..".VipVo_Data"]=nil
_G.package[CURRENT_PACKAGE..".BuyPPVo_Data"]=nil
_G.package[CURRENT_PACKAGE..".ErrStaticVo_Data"]=nil
_G.package[CURRENT_PACKAGE..".EnchantingVo_Data"]=nil
_G.package[CURRENT_PACKAGE..".UserShopStaticVo_Data"]=nil
_G.package[CURRENT_PACKAGE..".ComposeStaticVo_Data"]=nil
_G.package[CURRENT_PACKAGE..".EffectStaticVo_Data"]=nil
_G.package[CURRENT_PACKAGE..".BuffStaticVo_Data"]=nil
_G.package[CURRENT_PACKAGE..".NpcTroopStaticVo_Data"]=nil
_G.package[CURRENT_PACKAGE..".heroMagicStaticVo_Data"]=nil
_G.package[CURRENT_PACKAGE..".EnchantMagicVo_Data"]=nil
_G.package[CURRENT_PACKAGE..".HeroSoundStaticVo_Data"]=nil
_G.package[CURRENT_PACKAGE..".BattleSoundPairStaticVo_Data"]=nil
_G.package[CURRENT_PACKAGE..".TaskDayStaticVo_Data"]=nil
_G.package[CURRENT_PACKAGE..".TaskStaticVo_Data"]=nil
_G.package[CURRENT_PACKAGE..".UserSkillStaticVo_Data"]=nil
_G.package[CURRENT_PACKAGE..".UserLevelStaticVo_Data"]=nil
_G.package[CURRENT_PACKAGE..".BigBossStaticVo_Data"]=nil
_G.package[CURRENT_PACKAGE..".SiegeStaticVo_Data"]=nil
_G.package[CURRENT_PACKAGE..".StoryStaticVo_Data"]=nil
_G.package[CURRENT_PACKAGE..".ArenaTopRankAwardVo_Data"]=nil
_G.package[CURRENT_PACKAGE..".ArenaRankAwardVo_Data"]=nil
_G.package[CURRENT_PACKAGE..".ArenaBuyAttackNumVo_Data"]=nil
_G.package[CURRENT_PACKAGE..".LegionBasicVo_Data"]=nil
_G.package[CURRENT_PACKAGE..".LegionEmployVo_Data"]=nil
_G.package[CURRENT_PACKAGE..".LegionSalaryVo_Data"]=nil
_G.package[CURRENT_PACKAGE..".LegionEventVo_Data"]=nil
_G.package[CURRENT_PACKAGE..".RandomNameVo_Data"]=nil
_G.package[CURRENT_PACKAGE..".RegistryVo_Data"]=nil
_G.package[CURRENT_PACKAGE..".BuyGoldVo_Data"]=nil
_G.package[CURRENT_PACKAGE..".BuyEliteVo_Data"]=nil
_G.package[CURRENT_PACKAGE..".GuideVo_Data"]=nil
_G.package[CURRENT_PACKAGE..".GuideDialogueVo_Data"]=nil
_G.package[CURRENT_PACKAGE..".Recharge_Data"]=nil
_G.package[CURRENT_PACKAGE..".DirtyWord_Data"]=nil
_G.package[CURRENT_PACKAGE..".Tower_Data"]=nil
_G.package[CURRENT_PACKAGE..".Fund_Data"]=nil
_G.package[CURRENT_PACKAGE..".Benefit_Data"]=nil
_G.package[CURRENT_PACKAGE..".MammonVo_Data"]=nil
_G.package[CURRENT_PACKAGE..".Activity_Data"]=nil
end
return manager
