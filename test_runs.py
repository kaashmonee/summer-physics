import sqlutilpy as sqlutil
import database_config
# import astrolibpy.utils.sqlutil as sqlutil

def main():
    # Whitespace does not matter
    username = database_config.username
    password = database_config.password
    host = database_config.host
    # database_name = database_config.database_name


    ra, dec = sqlutil.get(
        "select ra, dec from des_dr1.main where q3c_radial_query(ra,dec,317.2044,-51.1656,1)",
        host=host, user=username, password=password
    )

    # Getting the entire table 
    # Do not run this...this is too big. this is here for reference
    """
    something = sqlutil.get(
        "select * from des_dr1.main", host="wsdb.hpc1.cs.cmu.edu",
        user=username, password=password
    )
    """

    print("ra:", ra, "dec:", dec)
    print("ra type:", type(ra), "dec type:", type(dec))

if __name__ == "__main__":
    main()