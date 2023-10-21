from mongoengine import Document, StringField, IntField, ListField, DateTimeField, ObjectIdField
from persiantools.jdatetime import JalaliDate
from bson import ObjectId
class pallet(Document):
    _id = ObjectIdField()
    first_color = StringField(required=True, regex='^#(?:[0-9a-fA-F]{3}){1,2}$', max_length=9, min_length=7)
    secend_color = StringField(required=True, regex='^#(?:[0-9a-fA-F]{3}){1,2}$', max_length=9, min_length=7)
    third_color = StringField(required=True, regex='^#(?:[0-9a-fA-F]{3}){1,2}$', max_length=9, min_length=7)
    type_color = StringField(required=True)
    type_color_name = StringField(required=True)
    type_color_name_vector = ListField(required=True)
    jobs = ListField(required=True)
    jobs_name = ListField(required=True)
    jobs_name_vector = ListField(required=True)
    keywords = ListField(required=True)
    keywords_vectors = ListField(required=True)
    creator = StringField(required=True)
    create_date = DateTimeField(required=True)
    def to_dict(self):
        return {
            '_id': str(self._id),
            'first_color': self.first_color,
            'secend_color': self.secend_color,
            'third_color': self.third_color,
            'type_color': self.third_color,
            'type_color_name': self.type_color_name,
            'type_color_name_vector': self.type_color_name_vector,
            'jobs': self.jobs,
            'jobs_name': self.jobs_name,
            'jobs_name_vector': self.jobs_name_vector,
            'keywords': self.keywords,
            'keywords_vectors': self.keywords_vectors,
            'creator': self.creator,
            'create_date': self.create_date,
        }
    @classmethod
    def get_pallet_tank(cls):
        all_color_types = cls.objects.all()
        result = [color_type.to_dict() for color_type in all_color_types]
        for item in result:
            del item['type_color_name_vector']
            del item['jobs_name_vector']
            del item['keywords_vectors']
            del item['creator']
            item['_id'] = str(item['_id'])
            item['create_date'] = str(JalaliDate.to_jalali(item['create_date'].year,item['create_date'].month,item['create_date'].day))
        return result
    @classmethod
    def delete_pallet(cls, id_pallet):
        pallet_to_delete = cls.objects(_id=ObjectId(id_pallet)).delete()
        if pallet_to_delete:
            return True
        else:
            return False
        
    def __repr__(self):
        return f'Pallet({self.first_color}, {self.secend_color}, {self.third_color})'
