from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, JSON, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class UserProfile(Base):
    __tablename__ = 'user_profile'
    user_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(VARCHAR(length=255))
    last_name = Column(VARCHAR(length=255))
    department = Column(VARCHAR(length=255))
    designation = Column(VARCHAR(length=255))
    tenant_id = Column(Integer, ForeignKey('tenant_profile.tenant_id'))
    image_url = Column(VARCHAR(length=255))
    city = Column(VARCHAR(length=255))
    country = Column(VARCHAR(length=255))
    bio = Column(VARCHAR(length=255))
    social_links = Column(JSON)
    employee_id = Column(Integer)

    tenant = relationship("Tenant", back_populates="tenant_profile")

    def serialize(self):
        return {
            'user_id': self.user_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'department': self.department,
            'designation': self.designation,
            'tenant_id': self.tenant_id,
            'image_url': self.image_url,
            'city': self.city,
            'country': self.country,
            'bio': self.bio,
            'social_links': self.social_links,
            'employee_id': self.employee_id
        }


class TenantProfile(Base):
    __tablename__ = 'tenant_profile'
    tenant_id = Column(Integer, primary_key=True, index=True)
    tenant_name = Column(VARCHAR(length=255))
    address = Column(JSON)
    city = Column(VARCHAR(length=255))
    state = Column(VARCHAR(length=255))
    country = Column(VARCHAR(length=255))
    zip_code = Column(VARCHAR(length=255))
    phone = Column(VARCHAR(length=255))
    web_url = Column(VARCHAR(length=255))

DB_URL = 'postgresql://postgres:postgres@http://localhost:8090:4000/social'

engine = create_engine(DB_URL)
Base.metadata.create_all(engine)
engine.dispose()