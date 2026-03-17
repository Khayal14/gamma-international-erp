from sqlalchemy import Column, String, Text, Date, DateTime, Enum as SAEnum
from sqlalchemy.dialects.postgresql import UUID
from app.shared.base_model import UUIDBase, TimestampMixin
from app.shared.enums import ShipmentStatus

class Shipment(UUIDBase, TimestampMixin):
    __tablename__ = "shipments"
    supplier_po_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    branch_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    tracking_reference = Column(String(100), nullable=True)
    shipping_method = Column(String(50), nullable=True)
    status = Column(SAEnum(ShipmentStatus), nullable=False, default=ShipmentStatus.AWAITING_DISPATCH)
    origin_country = Column(String(100), nullable=True)
    estimated_arrival_date = Column(Date, nullable=True)
    actual_arrival_date = Column(Date, nullable=True)
    customs_cleared_at = Column(DateTime(timezone=True), nullable=True)
    received_at = Column(DateTime(timezone=True), nullable=True)
    notes = Column(Text, nullable=True)
