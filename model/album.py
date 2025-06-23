from dataclasses import dataclass


@dataclass
class Album:
    AlbumId: int
    title: str
    ncanzoni: int

    def __str__(self):
        return self.title

    def __eq__(self, other):
        return self.AlbumId == other.AlbumId

    def __hash__(self):
        return hash(self.AlbumId)
