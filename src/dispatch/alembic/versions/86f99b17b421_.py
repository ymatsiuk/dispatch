"""Adds default values and metric flags to incident_type model

Revision ID: 86f99b17b421
Revises: 50972429e3f0
Create Date: 2020-06-24 10:44:47.542780

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "86f99b17b421"
down_revision = "50972429e3f0"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("incident_priority", sa.Column("default", sa.Boolean(), nullable=True))
    op.add_column("incident_type", sa.Column("default", sa.Boolean(), nullable=True))
    op.add_column("incident_type", sa.Column("exclude_from_metrics", sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("incident_type", "default")
    op.drop_column("incident_priority", "default")
    op.drop_column("incident_priority", "exclude_from_metrics")
    # ### end Alembic commands ###