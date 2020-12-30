#COMMANDS FOR ACCESS 
#RUN THE MAIN FILE & IMPORT MAIN FILE AS LIBRARY
import crd as a 
a.create("some_x_name",20) #CREATING A KEY WITH KEY_NAME,VALUE GIVEN AND WITH NO TIME-TO-LIVE PROPERTY
a.create("some_y_name",50,3600)  #CREATING A KEY WITH KEY_NAME,VALUE GIVEN AND WITH TIME-TO-LIVE PROPERTY VALUE 
a.read("myname") #RETURNS KEY IN  JASON OBJECT FORMAT KEY_NAME:VALUE
a.read("hi") #RETURNS THE VALUE OF THE RESPECTIVE KEY IN JASONOBJECT FORMAT IF TIME-TO-LIVE IS NOT EXPIRED ELSE RETURNS ERROR
a.create("myname",50) #RETURNS AN ERROR SINCE THE KEY_NAME ALREADY EXISTS IN THE DATABASE
a.modify("myname",55) #REPLACES THE INITIAL VALUE OF THE RESPECTIVE KEY WITH NEW VALUE 
a.delete("myname") #DELETES THE RESPECTIVE KEY AND ITS VALUE FROM THE DATABASE
t1=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #WE CAN ACCESS THESE USING MULTIPLE THREADS
t1.start()
t1.sleep()
t2=Thread(target=(create or read or delete),args=(key_name,value,timeout))
t2.start()
t2.sleep()

#AFTER THE GIVE TIME TO LIVE THE VALUE WILL EXPIRE , CANNOT READ & DELETE


#the data store will support the following functional requirements.
#1. It can be initialized using an optional file path. If one is not provided,
#it will reliably create itself in a reasonable location on the laptop.

#2. Anew key-value pair can be added to the data store using the Create operation.
# The keyis always a string - capped at 32chars. The value is always a JSON object - capped at16KB.

#3. If Create is invoked for an existing key, an appropriate error must be returned.

#4. A Read operation on a key can be performed by providing the key, and receiving the
#value in response, as a JSON object.

#5. A Delete operation can be performed by providing the key.

#6. Every key supports setting a Time-To-Live property when it is created. This property is
#optional. If provided, it will be evaluated as an integer defining the number of seconds
#the key must be retained in the data store. Once the Time-To-Live for a key has expired,
#the key will no longer be available for Read or Delete operations.

#7. Appropriate error responses must always be returned to a client if it uses the data store inunexpected ways or breaches any limits.

#The data store will also support the following non-functional requirements.

#1. The size of the file storing data must never exceed 1GB.

#2. More than one client process cannot be allowed to use the same file as a data store at any
#given time.

#3. Aclient process is allowed to access the data store using multiple threads, if it desires to. The data store must therefore be thread-safe.

#4. The client will bear as little memory costs as possible to use this data store, while
#deriving maximum performance with respect to response times for accessing the datastore. /*
