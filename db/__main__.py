import sqlite3

def save_author(c, author):
  pass

def delete_quotes(c, filters={}):
  query = 'delete from quotes'

  if filters:
    query += 'where '
    for k in filters.keys():
      query += f'{k}=:{k} '

  res = c.execute(query, filters).fetchall()
  return res

def update_quote(c, new_data, filters):
  query = 'update quotes set '
  where = {}

  for k in new_data.keys():
    query += f'{k}=:{k} '

  query += 'where '
  for k, v in filters.items():
    new_k = 'old_' + k
    query += f'{k}=:{new_k} '
    where[new_k] = v

  arguments = new_data | where

  res = c.execute(query, arguments)
  return res

def get_quotes(c, filters={}, order_by=[]):
  quotes = []
  query = "select * from quotes "

  if filters:
    query += "where "

    for k in filters.keys():
      query += f'{k}=:{k} '

  if len(order_by) > 0:
    query += "order by "
    for o in order_by:
      query += o + " "
    
  print(query)
  quotes = c.execute(query, filters).fetchall()
  return quotes  



def save_quote(c, quote):
  c.execute("insert into quotes values (?, ?, ?, ?)", quote)

def exists_table(cur, name):
  res = cur.execute('select name from sqlite_master where type="table" and name=:name', { "name": name }).fetchall()
  return len(res) > 0  

def main():
  connection = sqlite3.connect('example.db')
  cursor = connection.cursor()

  if not exists_table(cursor, 'quotes'):
    cursor.execute("""create table quotes
    (author text, content text, year integer, popularity integer)""")  

    save_quote(cursor, ('Yoda', 'Que la fuerza, contigo esté', 3790, 5))
    save_quote(cursor, ('Darth Vader', 'Yo soy tu padre', 3800, 3))

  connection.commit()
  connection.close()

  con = sqlite3.connect('example.db')
  cur = con.cursor()

  with con:

    update_quote(con, {'content':'La fuerza, fuerte en tí es'}, {'author': 'Yoda'})
    delete_quotes(con)
    # quotes = get_quotes(con, filters={'author':'author 1'}, order_by=['popularity'])
    quotes = get_quotes(con)


  print('Quotes')
  for q in quotes:
    print(f'  Author: {q[0]}')
    print(f'  Content: {q[1]}')
    print(f'  year: {q[2]}')
    print()


if __name__ == '__main__':
  main()