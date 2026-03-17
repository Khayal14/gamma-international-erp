from sqlalchemy import Column, String, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID, JSONB
from app.shared.base_model import UUIDBase, TimestampMixin

class DeliveryNote(UUIDBase, TimestampMixin):
    __tablename__ = "delivery_notes"
    delivery_number = Column(String(30), nullable=False, index=True)
    branch_id = Column(UUID(as_uuid=True), nullable=False)
    sales_order_id = Column(UUID(as_uuid=True), nullable=False)
    invoice_id = Column(UUID(as_uuid=True), nullable=True)
    client_id = Column(UUID(as_uuid=True), nullable=False)
    delivery_address = Column(JSONB, nullable=True)
    dispatched_at = Column(DateTime(timezone=True), nullable=True)
    received_by = Column(String(255), nullable=True)
    notes = Column(Text, nullable=True)
    created_by = Column(UUID(as_uuid=True), nullable=False)
