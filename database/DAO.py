from database.DB_connect import DBConnect
from model.album import Album
from model.genre import Genre
from model.track import Track


class DAO:

    @staticmethod
    def getGenres():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select g.GenreId , g.Name, (min(t.Milliseconds)/1000) as minD 
                        from itunes.genre g, itunes.track t 
                        where g.GenreId = t.GenreId 
                        group by g.GenreId , g.Name
                        order by g.Name 
                                                    """
            cursor.execute(query,)

            for row in cursor:
                result.append(Genre(row["GenreId"], row["Name"], row["minD"]))
            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def getNodes(genreId, tMin, tMax):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select t.TrackId , t.Name, count(distinct(p.PlaylistId)) as nPlaylist, (t.Milliseconds/1000) as duration 
                        from itunes.genre g, itunes.track t, itunes.playlisttrack p 
                        where g.GenreId = t.GenreId
                                and g.GenreId  = %s
                                and t.Milliseconds >= (%s*1000)
                                and t.Milliseconds <= (%s*1000)
                                and t.TrackId = p.TrackId
                        group by t.TrackId , t.Name
                        """
            cursor.execute(query, (genreId, tMin, tMax))

            for row in cursor:
                result.append(Track(row["TrackId"], row["Name"], row["nPlaylist"], row["duration"]))
            cursor.close()
            cnx.close()
        return result


