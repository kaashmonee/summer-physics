import sqlutilpy as sqlutil
import database-config
# import astrolibpy.utils.sqlutil as sqlutil

def main():
    # Whitespace does not matter
    username = database-config.username
    password = database-config.password

    ra, dec = sqlutil.get(
        """select ra, dec from des_dr1.main where q3c_radial_query(ra,dec,317.2044,-51.1656,1)""",
        host="wsdb.hpc1.cs.cmu.edu", user=username, password=password
    )


    print("ra:", ra, "dec:", dec)
    print("ra type:", type(ra), "dec type:", type(dec))

if __name__ == "__main__":
    main()