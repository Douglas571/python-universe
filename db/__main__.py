import sqlite3

def save_author(c, author):
  pass

def exists_table(c, name):
  res = c.execute('select name from sqlite_master where type="table" and name=:name', { "name": name }).fetchall()
  return len(res) > 0

def ensure_table(c, name):
  if not exists_table(c, name):
    c.execute("""create table (?)
    (author text, content text, year integer, popularity integer)""", (name,))  

def delete_quotes(c, filters={}):
  query = 'delete from quotes'

  if filters:
    query += 'where '
    for k in filters.keys():
      query += f'{k}=:{k} '

  res = c.execute(query, filters).fetchall()

  print(query)
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

  print(query)
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
    
  quotes = c.execute(query, filters).fetchall()
  
  print(query)
  return quotes  

def save_quote(c, quote):
  c.execute("insert into quotes values (?, ?, ?, ?)", quote)  

def main():
  connection = sqlite3.connect('example.db')
  cursor = connection.cursor()

  ensure_table(cursor, 'quotes')

  save_quote(cursor, ('Darth Sidious', 'El dolor lleva al miedo, el miedo lleva al odio...', 3790, 5))
  save_quote(cursor, ('Darth Vader', 'Yo soy tu padre', 3800, 3))

  save_quote(cursor, ('Yoda', 'La fuerza, fuerte en tí es', 2970, 2))

  connection.commit()
  connection.close()

  # Read and update phase

  con = sqlite3.connect('example.db')
  cur = con.cursor()
  with con:
    update_quote(con, {'content':'Cuándo veas hacia el lado oscuro, cuidadoso debes de ser...'}, {'author': 'Yoda'})
    # delete_quotes(con)
    quotes = get_quotes(con, filters={}, order_by=['popularity'])
    # quotes = get_quotes(con)


  print('Quotes')
  for q in quotes:
    print(f'  Author: {q[0]}')
    print(f'  Content: {q[1]}')
    print(f'  year: {q[2]}')
    print()


if __name__ == '__main__':
  main()