class QuestionOfflineRouter(object):
    def db_for_read(self, model, **kwrags):
        if model._meta.app_label == 'question_offline':
            return 'question_offline_db'
