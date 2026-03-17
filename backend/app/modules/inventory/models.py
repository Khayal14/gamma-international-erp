from sqlalchemy import Column, String, Numeric, Text, DateTime, Enum as SAEnum
from sqlalchemy.dialects.postgresql import UUID
from app.shared.base_model import UUIDBase, TimestampMixin
from app.shared.enums import StockMovementType, TransferStatus

class StockLevel(UUIDBase):
    __tablename__ = "stock_levels"
    branch_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    product_variant_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    quantity_on_hand = Column(Numeric(14, 4), nullable=False, default=0)
    quantity_reserved = Column(Numeric(14, 4), nullable=False, default=0)
    quantity_available = Column(Numeric(14, 4), nullable=False, default=0)
    last_updated_at = Column(DateTime(timezone=True), nullable=True)

class StockMovement(UUIDBase, TimestampMixin):
    __tablename__ = "stock_movements"
    branch_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    product_variant_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    movement_type = Column(SAEnum(StockMovementType), nullable=False)
    quantity = Column(Numeric(14, 4), nullable=False)
    reference_type = Column(String(50), nullable=True)
    reference_id = Column(UUID(as_uuid=True), nullable=True)
    notes = Column(Text, nullable=True)
    created_by = Column(UUID(as_uuid=True), nullable=True)

class BranchStockTransfer(UUIDBase, TimestampMixin):
    __tablename__ = "branch_stock_transfers"
    from_branch_id = Column(UUID(as_uuid=True), nullable=False)
    to_branch_id = Column(UUID(as_uuid=True), nullable=False)
    status = Column(SAEnum(TransferStatus), nullable=False, default=TransferStatus.REQUESTED)
    requested_by = Column(UUID(as_uuid=True), nullable=False)
    approved_by = Column(UUID(as_uuid=True), nullable=True)
    notes = Column(Text, nullable=True)

class BranchStockTransferLine(UUIDBase):
    __tablename__ = "branch_stock_transfer_lines"
    transfer_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    product_variant_id = Column(UUID(as_uuid=True), nullable=False)
    quantity_requested = Column(Numeric(14, 4), nullable=False)
    quantity_approved = Column(Numeric(14, 4), nullable=True)
    quantity_received = Column(Numeric(14, 4), nullable=True)
