from mongoengine import Document, ListField, StringField


class CommitType(Document):
    id = StringField(unique=True, required=True)
    git_hash = StringField(unique=True, required=True)
    changes = ListField(default=None)
    coverage = ListField(default=None)

    def dict(self):
        return {
            "id": self.id,
            "git_hash": self.git_hash,
            "changes": self.changes,
            "coverage": self.coverage,
        }

    meta = {
        "indexes": ["id", "git_hash"]
    }
