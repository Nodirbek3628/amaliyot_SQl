from datetime import datetime
from sqlalchemy import Connection,DateTime,Insert,select,Delete,update
from models import tasks


def created_tasks(
    conn: Connection,
    title: str,
    description: str|None=None, due_date: DateTime |None=None
    ):
    try:
        query = Insert(tasks).values(
            title=title,
            description=description,
            due_date=due_date,
        )  
        conn.execute(query)
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()
    finally:
        conn.close() 


def get_tasks(conn: Connection,):
    result = []
    try:
        query = select(tasks)
        result = conn.execute(query)
        conn.commit()
    except Exception as e:
        print(e)

    finally:
        conn.close() 

    return result


def delete_tasks( conn: Connection,task_id: int ):
    try:
        query = Delete(tasks).where(tasks.c.id == task_id)

        conn.execute(query)
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()
    finally:
        conn.close() 


def update_task(
        conn: Connection, 
        task_id: int, 
        title: str | None = None,
        description: str | None = None,
        due_date: datetime | None = None
    ):
    try:
        query = select(tasks).where(tasks.c.id == task_id)

        result = conn.execute(query)
        task = result.fetchone() # (1, title, desc, completed, due-date, created-at)

        query = update(tasks).where(tasks.c.id == task_id).values(
            title=title or task[1],
            description=description or task[2],
            due_date=due_date or task[4],
            updated_at=datetime.now()
            
        )
        conn.execute(query)

        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()
    finally:
        conn.close()

def change_task_status(conn: Connection, task_id: int ):
    try:
        query = select(tasks).where(tasks.c.id == task_id)

        result = conn.execute(query)
        task = result.fetchone() # (1, title, desc, completed, due-date, created-at)

        query = update(tasks).where(tasks.c.id == task_id).values(
            completed=not task[3])
        
        conn.execute(query)

        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()
    finally:
        conn.close()



