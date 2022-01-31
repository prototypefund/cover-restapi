from mongoengine import Document, ListField, StringField


class BranchType(Document):
    id = StringField(unique=True, required=True)
    name = StringField(unique=True, required=True)
    commits = ListField(default=None)
    coverage = ListField(default=None)

    def dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "commits": self.commits,
            "coverage": self.coverage,
        }

    meta = {
        "indexes": ["id", "name"]
    }
