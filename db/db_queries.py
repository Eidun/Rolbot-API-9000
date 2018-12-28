# Creation queries
CREATE_ROLL_TABLE ='CREATE TABLE ROLL (' \
                   'id SERIAL PRIMARY KEY,' \
                   ' diceType INTEGER, dices INTEGER,  author text, repeats INTEGER, seen BOOLEAN,' \
                   ' result text);'

# Check if table exists
CHECK_ROLL_EXISTS = 'select exists(select * from information_schema.tables where table_name=%s);'


# Insert values queries
INSERT_ROLL = "INSERT INTO ROLL" \
              "(author, dices, diceType, result, repeats, seen)" \
              "VALUES (%s, %s, %s, %s, %s, %s);"


# Get result queries
GET_ROLL = "SELECT result, repeats FROM ROLL WHERE NOT result='unresolved' AND seen=FALSE AND author=%s;"

SEE_ROLL = "UPDATE ROLL SET seen=TRUE WHERE seen=FALSE AND author=%s;"

