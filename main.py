from database import engine,metadata_obj
import models

metadata_obj.create_all(engine)


