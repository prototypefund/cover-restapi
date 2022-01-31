from mongoengine import Document, IntField, StringField, DateTimeField, FloatField


class CoverageType(Document):
    id = StringField(unique=True, required=True)
    timestamp = DateTimeField(default=None)
    lines_valid = IntField(default=0)
    lines_covered = IntField(default=0)
    branches_covered = IntField(default=0)
    branches_valid = IntField(default=0)
    complexity = FloatField(default=0)

    def dict(self):
        return {
            "id": self.id,
        }

    meta = {
        "indexes": ["id"]
    }
