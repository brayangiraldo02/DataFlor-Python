from config.database import Base

from sqlalchemy import Column, Integer, String, Enum

class FlowerShop(Base):
    __tablename__ = "flowershops"

    idflowershops = Column(Integer, primary_key=True, autoincrement=True)
    fullname = Column(String(255), nullable=False)
    address = Column(String, nullable=False)
    phone = Column(String(15), nullable=False)
    state = Column(Enum('Activate', 'Inactive'), default='Activate', nullable=False)
