from sqlalchemy import Column, String, Numeric, Enum as SAEnum, Boolean
from sqlalchemy.dialects.postgresql import UUID
from app.shared.base_model import UUIDBase, TimestampMixin
from app.shared.enums import BranchCode, DocumentType, Language

class Branch(UUIDBase, TimestampMixin):
    __tablename__ = "branches"
    code = Column(SAEnum(BranchCode), unique=True, nullable=False)
    legal_name_en = Column(String(255), nullable=False)
    legal_name_ar = Column(String(255), nullable=False)
    address_en = Column(String, nullable=True)
    address_ar = Column(String, nullable=True)
    phone = Column(String(30), nullable=True)
    email = Column(String(255), nullable=True)
    logo_url = Column(String, nullable=True)
    vat_number = Column(String(50), nullable=True)
    default_vat_rate = Column(Numeric(5, 2), nullable=False, default=14)

class BranchBankAccount(UUIDBase):
    __tablename__ = "branch_bank_accounts"
    branch_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    bank_name = Column(String(255), nullable=False)
    account_name = Column(String(255), nullable=False)
    account_number = Column(String(100), nullable=False)
    iban = Column(String(50), nullable=True)
    swift = Column(String(20), nullable=True)
    currency = Column(String(3), nullable=False)
    is_default = Column(Boolean, nullable=False, default=False)

class TCTemplate(UUIDBase, TimestampMixin):
    __tablename__ = "tc_templates"
    branch_id = Column(UUID(as_uuid=True), nullable=True)
    document_type = Column(SAEnum(DocumentType), nullable=False)
    language = Column(SAEnum(Language), nullable=False, default=Language.EN)
    content_en = Column(String, nullable=True)
    content_ar = Column(String, nullable=True)
    is_default = Column(Boolean, nullable=False, default=False)
