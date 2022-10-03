from sqlite3 import connect
import pandas as pd
from models import Crypto


conn = connect(':memory:')
#conn = sqlite3.connect('Cryptos.db')

c = Crypto.objets.get(all) 
print(c)
# for i in c:
#     print(i)


# c.execute("""CREATE TABLE crypto (

#     symbol text,
#     name text,
#     price integer

#  )""")

# c.execute("INSERT INTO crypto VALUES ('BTC', 'bitcoin', 20000)")

# data = pd.read_sql("SELECT * FROM crypto", conn)
# print(data)



# c.execute("SELECT * FROM BTC WHERE symbol='BTC'")
# print(c.fetchone())

# conn.commit()

# conn.close()