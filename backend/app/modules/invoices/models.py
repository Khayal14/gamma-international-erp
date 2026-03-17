from sqlalchemy import Column, String, Numeric, Text, Date, DateTime, Enum as SAEnum
from sqlalchemy.dialects.postgresql import UUID
from app.shared.base_model import UUIDBase, TimestampMixin
from app.shared.enums import Category, InvoiceStatus, PaymentType

class Invoice(UUIDBase, TimestampMixin):
    __tablename__ = "invoices"
    invoice_number = Column(String(30), nullable=False, index=True)
    branch_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    category = Column(SAEnum(Category), nullable=False)
    client_id = Column(UUID(as_uuid=True), nullable=False)
    sales_order_id = Column(UUID(as_uuid=True), nullable=False)
    status = Column(SAEnum(InvoiceStatus), nullable=False, default=InvoiceStatus.DRAFT)
    sell_currency = Column(String(3), nullable=False, default="EGP")
    fx_rate_used = Column(Numeric(12, 6), nullable=True)
    subtotal = Column(Numeric(14, 2), nullable=False, default=0)
    vat_rate = Column(Numeric(5, 2), nullable=False, default=14)
    vat_amount = Column(Numeric(14, 2), nullable=False, default=0)
    total = Column(Numeric(14, 2), nullable=False, default=0)
    payment_type = Column(SAEnum(PaymentType), nullable=False, default=PaymentType.SINGLE)
    deposit_amount = Column(Numeric(14, 2), nullable=True)
    deposit_paid_at = Column(DateTime(timezone=True), nullable=True)
    final_amount = Column(Numeric(14, 2), nullable=True)
    final_paid_at = Column(DateTime(timezone=True), nullable=True)
    issue_date = Column(Date, nullable=False)
    due_date = Column(Date, nullable=False)
    bank_account_id = Column(UUID(as_uuid=True), nullable=True)
    tc_content_en = Column(Text, nullable=True)
    tc_content_ar = Column(Text, nullable=True)
    notes_en = Column(Text, nullable=True)
    notes_ar = Column(Text, nullable=True)
    created_by = Column(UUID(as_uuid=True), nullable=False)
