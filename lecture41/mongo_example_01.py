from pymongo import MongoClient

def connect_to_atlas_cluster():
  connection_string = 'mongodb+srv://chavdar:q2F9yAS1@cluster0.kupvfos.mongodb.net/'
  return MongoClient(connection_string)


if __name__ == '__main__':
  
  atlas_client = connect_to_atlas_cluster()

  #list databases
  print(atlas_client.list_database_names())
  
  #list_own = ['mongodb+srv://cluster0.kupvfos.mongodb.net/',' ','--username chavdar']
  #connection_string = ''.join(list_own)
  #print(type(connection_string))
