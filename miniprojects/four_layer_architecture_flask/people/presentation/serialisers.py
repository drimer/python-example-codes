from flask.json import jsonify
from injector import inject

from people.presentation.schemas import PersonSchema


class PersonSerialiser(object):
    @inject
    def __init__(self, schema: PersonSchema):
        self.schema = schema

    def serialise(self, person):
        return jsonify(self.schema.dump(person).data)
