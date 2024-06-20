# from sqlalchemy import Column, Integer, String, Text, DateTime
# from sqlalchemy.ext.declarative import declarative_base
# from datetime import datetime, timezone
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# Base = declarative_base()

# class Task(Base):
#     __tablename__ = 'tasks'

#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     description = Column(Text, nullable=True)
#     status = Column(String, default='pending')
#     created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    


    # Add code here to interact with the database using the session object