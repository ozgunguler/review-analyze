class ReviewAnalyzeRouter(object):

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'comments':
            return 'review'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'comments':
            return 'review'
        return None

    # def allow_relation(self, obj1, obj2, **hints):
    #     if obj1._meta.app_label in self.log_app_labels or obj2._meta.app_label in self.log_app_labels:
    #         return True
    #     return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'comments':
            return db == 'review'
        return None