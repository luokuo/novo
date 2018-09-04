import xadmin
from xadmin import views


class BaseSetting(object):
	enable_themes = True
	use_bootswatch = True


class GlobalSettings(object):
	site_title = "诺禾后台管理系统"
	site_footer = "novogene"
	menu_style = "accordion"






xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(views.BaseAdminView, BaseSetting)
