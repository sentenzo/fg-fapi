from sqlalchemy import (
    TIMESTAMP,
    Column,
    ForeignKey,
    Integer,  # Table,
    MetaData,
    String,
    Text,
    UniqueConstraint,
    Uuid,
)
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql.expression import text

metadata = MetaData()

Base = declarative_base(metadata=metadata)


class AbstractEntity(Base):
    __abstract__ = True

    id = Column(
        Uuid,
        primary_key=True,
        nullable=False,
        server_default=text("gen_random_uuid ()"),
    )
    creation_order = Column(Integer, primary_key=True, nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("NOW()")
    )


class User(AbstractEntity):
    __tablename__ = "user"

    username = Column(String(150), unique=True)
    hashed_password = Column(String, nullable=False)
    email = Column(String(254), unique=True)
    first_name = Column(String(150))
    last_name = Column(String(150))


class RefTagItem(Base):
    __tablename__ = "ref_tag_item"

    tag_id = Column(ForeignKey("tag.id"), nullable=False)
    item_id = Column(ForeignKey("item.id"), nullable=False)

    __table_args__ = (
        UniqueConstraint("tag_id", "item_id", name="unique_ref_tag_item"),
    )


class RefComponentItem(Base):
    __tablename__ = "ref_component_item"

    component_id = Column(ForeignKey("component.id"), nullable=False)
    item_id = Column(ForeignKey("item.id"), nullable=False)
    amount = Column(Integer, nullable=False)

    __table_args__ = (
        UniqueConstraint(
            "component_id", "item_id", name="unique_ref_component_item"
        ),
    )


class Tag(AbstractEntity):
    __tablename__ = "tag"

    name = Column(String(200), unique=True)
    color = Column(String(7), unique=True)
    slug = Column(String(200), unique=True)

    items = relationship(
        "item", secondary="ref_tag_item", back_populates="tags"
    )


class Item(AbstractEntity):
    __tablename__ = "item"

    name = Column(String(200))
    text = Column(Text)

    tags = relationship(
        "tag", secondary="ref_tag_item", back_populates="items"
    )


class Component(AbstractEntity):
    __tablename__ = "component"

    name = Column(String(200))
    unit = Column(String(200))

    __table_args__ = (
        UniqueConstraint("name", "unit", name="unique_component"),
    )
