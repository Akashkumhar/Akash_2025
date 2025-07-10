from sqlalchemy import Integer, String, Column, ForeignKey, JSON
from sqlalchemy.orm import relationship
from database import Base
from .schema_workspace import Workspace

class QnaTable(Base):
    __tablename__ = "qnatable"
    id = Column(Integer, primary_key=True, nullable=False)
    work_id = Column(Integer, ForeignKey("workspace.workspace_id"), nullable=False)
    qna_data = Column(JSON, nullable=True)


