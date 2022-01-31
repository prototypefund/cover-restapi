from mongoengine import Document, ListField, StringField


class ProjectType(Document):
    id = StringField(unique=True, required=True)
    title = StringField(unique=True, required=True)
    active_branch = StringField(default=None)
    branches = ListField(default=None)
    coverage = ListField(default=None)

    def dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "active_branch": self.active_branch,
            "branches": self.branches,
            "coverage": self.coverage,
        }

    meta = {
        "indexes": ["id", "title"]
    }
