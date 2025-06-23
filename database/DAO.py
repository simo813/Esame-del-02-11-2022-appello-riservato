from database.DB_connect import DBConnect
from model.album import Album


class DAO:

    @staticmethod
    def getNodes(canzoniN):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select distinct (a.AlbumId), a.Title , count(t.TrackId) as ncanzoni
                        from itunes.album a , itunes.track t 
                        where a.AlbumId = t.AlbumId 
                        group by a.AlbumId 
                        having count(t.TrackId) > %s
                        """
            cursor.execute(query, (canzoniN, ))

            for row in cursor:
                result.append(Album(row["AlbumId"], row["Title"], row["ncanzoni"]))
            cursor.close()
            cnx.close()
        return result

