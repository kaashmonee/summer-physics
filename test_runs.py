import sqlutilpy as sqlutil
# import astrolibpy.utils.sqlutil as sqlutil

def main():
    ra, dec = sqlutil.get(
        """ select ra, dec from des_dr1.main where q3c_radial_query(ra,dec,317.2044,-51.1656,1)""",
        host="wsdb.hpc1.cs.cmu.edu", user="skanda_kaashyap", password="kZ5Wlo.s"
    )

    print("ra:", ra, "dec:", dec)

if __name__ == "__main__":
    main()