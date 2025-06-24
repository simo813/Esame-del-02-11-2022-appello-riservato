from dataclasses import dataclass


@dataclass
class Track:
    TrackId: int
    Name: str
    nPlaylist: int
    duration: int

    def __str__(self):
        return self.Name

    def __eq__(self, other):
        return self.TrackId == other.TrackId

    def __hash__(self):
        return hash(self.TrackId)