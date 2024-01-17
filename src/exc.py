class EmptyReposFileError(Exception):
    def __str__(self):
        return "Repos File is Empty"
