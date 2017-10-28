class QuestionOfflineRouter(object):

    def db_for_read(self, model, **kwrags):
        if model._meta.app_label == 'mysql':
            return 'html_archive'
        return None


    def db_for_write(self, model, **kwrags):
        if model._meta.app_label == 'mysql':
            return 'html_archive'
        return None


    # def allow_migrate(self, db, model):
    #     if db == 'html_archive':
    #         return model._meta.app_label == 'appname'
    #     elif model._meta.app_label == 'appname':
    #         return False


    def allow_syncdb(self, db, model):  # 决定 model 是否可以和 db 为别名的数据库同步
        if db == 'html_archive' or model._meta.app_label == "mysql":
            return False  # we're not using syncdb on our hvdb database
        else:  # but all other models/databases are fine
            return True
        return None
