from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from .schema_map_modes import Node, Roadmap
from .schema_user import User


class Workspace(Base):
    __tablename__ = "workspace"
    workspace_id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    prior_knowledge = Column(String, nullable=False)
    progress = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    roadmap_id = Column(Integer, ForeignKey('roadmaps.id'), nullable=False)
    roadmap = relationship("Roadmap", back_populates="workspace")
    current_node_id = Column(Integer, ForeignKey("nodes.id"))
    current_node = relationship("Node", foreign_keys=[current_node_id])

