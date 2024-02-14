class EmptyReposFileError(Exception):
    def __str__(self):
        return "Repositories file is empty"
