__navigation = {}
__navigation["home"] = "icon-home"
__navigation["squads"] = "icon-squad"
__navigation["transfers"] = "icon-transfer"
__navigation["store"] = "icon-store"
__navigation["club"] = "icon-club"
__navigation["sbc"] = "icon-sbc"
__navigation["leaderboards"] = "icon-leaderboards"
__navigation["settings"] = "icon-settings"

def get_navigation_bar_selector(name, nav):
  return nav.find_element_by_class_name(__navigation[name])
