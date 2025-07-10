from sqlalchemy import Integer, String, Column, ForeignKey, Text, Boolean
from sqlalchemy.orm import relationship
from database import Base



class Node(Base):
    __tablename__ = 'nodes'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)       
    description = Column(Text) 
    parent_id = Column(Integer, ForeignKey("nodes.id"))  
    children = relationship("Node", backref="parent", remote_side=[id])
    is_completed = Column(Boolean, default=False)

class Roadmap(Base):
    __tablename__ = "roadmaps"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    root_node_id = Column(Integer, ForeignKey("nodes.id"), nullable=False)
    root_node = relationship("Node", foreign_keys=[root_node_id])