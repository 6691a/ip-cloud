from django.db.models import Manager


class DeleteTimeStampModelManager(Manager):
    """
    A custom manager that provides a method to return all objects,
    including those that are soft-deleted.
    """

    def get_queryset(self):
        return super().get_queryset().filter(deleted__isnull=True)
