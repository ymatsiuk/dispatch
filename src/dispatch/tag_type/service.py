from typing import Optional
from fastapi.encoders import jsonable_encoder

from dispatch.project import service as project_service
from .models import TagType, TagTypeCreate, TagTypeUpdate


def get(*, db_session, tag_type_id: int) -> Optional[TagType]:
    """Gets a tag type by its id."""
    return db_session.query(TagType).filter(TagType.id == tag_type_id).one_or_none()


def get_by_name(*, db_session, project_id: int, name: str) -> Optional[TagType]:
    """Gets a tag type by its name."""
    return (
        db_session.query(TagType)
        .filter(TagType.name == name)
        .filter(TagType.project_id == project_id)
        .one_or_none()
    )


def get_all(*, db_session):
    """Gets all tag types."""
    return db_session.query(TagType)


def create(*, db_session, tag_type_in: TagTypeCreate) -> TagType:
    """Creates a new tag type."""
    project = project_service.get_by_name(db_session=db_session, name=tag_type_in.project.name)
    tag_type = TagType(**tag_type_in.dict(exclude={"project"}), project=project)
    db_session.add(tag_type)
    db_session.commit()
    return tag_type


def get_or_create(*, db_session, tag_type_in: TagTypeCreate) -> TagType:
    """Gets or creates a new tag type."""
    q = (
        db_session.query(TagType)
        .filter(TagType.name == tag_type_in.name)
        .filter(TagType.project_id == tag_type_in.project.id)
    )

    instance = q.first()
    if instance:
        return instance

    return create(db_session=db_session, tag_type_in=tag_type_in)


def update(*, db_session, tag_type: TagType, tag_type_in: TagTypeUpdate) -> TagType:
    """Updates a tag type."""
    tag_type_data = jsonable_encoder(tag_type)
    update_data = tag_type_in.dict(skip_defaults=True)

    for field in tag_type_data:
        if field in update_data:
            setattr(tag_type, field, update_data[field])

    db_session.add(tag_type)
    db_session.commit()
    return tag_type


def delete(*, db_session, tag_type_id: int):
    """Deletes a tag type."""
    tag = db_session.query(TagType).filter(TagType.id == tag_type_id).one_or_none()
    db_session.delete(tag)
    db_session.commit()
