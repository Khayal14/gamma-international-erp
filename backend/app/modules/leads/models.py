from sqlalchemy import Column, String, Boolean, Text, Numeric, Enum as SAEnum
from sqlalchemy.dialects.postgresql import UUID
from app.shared.base_model import UUIDBase, TimestampMixin
from app.shared.enums import Category, LeadStatus

class Lead(UUIDBase, TimestampMixin):
    __tablename__ = "leads"
    branch_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    category = Column(SAEnum(Category), nullable=False)
    client_id = Column(UUID(as_uuid=True), nullable=True)
    prospect_name = Column(String(255), nullable=True)
    prospect_contact = Column(Text, nullable=True)
    product_description = Column(Text, nullable=True)
    estimated_quantity = Column(Numeric(14, 4), nullable=True)
    status = Column(SAEnum(LeadStatus), nullable=False, default=LeadStatus.NEW)
    source = Column(String(100), nullable=True)
    assigned_to = Column(UUID(as_uuid=True), nullable=True)
    notes = Column(Text, nullable=True)
